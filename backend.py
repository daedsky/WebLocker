from porn_sites import all as ps
import json
import os
from dns_changer import DnsChanger


class PornBlocker:
    porn_sites = ps

    hostfile = r'C:\Windows\System32\drivers\etc\hosts' if os.name == 'nt' else '/etc/hosts'

    @classmethod
    def make_copy_of_hostfile(cls):
        with open(cls.hostfile, 'r') as f:
            data = f.read()
            with open(f'{cls.hostfile}_copy', 'w') as f2:
                f2.write(data)

    @classmethod
    def block_all_porn_sites(cls):
        # to check if porn sites have already been added to hostfile
        with open(cls.hostfile, 'r') as f:
            data = f.read()

        if not '# Generated with WebLocker' in data:
            with open(cls.hostfile, 'a') as f:
                f.write('\n')
                f.write('# Generated with WebLocker (https://github.com/daedsky/WebLocker\n')
                f.write('# begin porn website blocklist\n')
                for porn_site in cls.porn_sites:
                    with_www = f"0.0.0.0     www.{porn_site}\n"
                    without_www = f"0.0.0.0     {porn_site}\n"
                    f.write(with_www)
                    f.write(without_www)
                f.write('# end porn website blocklist\n')

            DnsChanger.change_dns('1.1.1.3', '1.0.0.3', 'block')

    @classmethod
    def unblock_all_porn_sites(cls):
        with open(cls.hostfile, 'r') as f:
            whole_file = f.read()

        with open(cls.hostfile, 'r') as f:
            data = f.readlines()

        with open(cls.hostfile, 'w') as f:
            for porn_site in cls.porn_sites:
                if porn_site in whole_file:
                    data.remove(f"0.0.0.0     www.{porn_site}\n")
                    data.remove(f"0.0.0.0     {porn_site}\n")

            data.remove("# Generated with WebLocker (https://github.com/daedsky/WebLocker\n")
            data.remove('# begin porn website blocklist\n')
            data.remove('# end porn website blocklist\n')

            f.write(''.join(data))

            DnsChanger.change_dns('192.168.1.254', '192.168.1.254', 'unblock')

    @classmethod
    def reset_hostfile(cls):
        with open(f"{cls.hostfile}_copy", 'r') as f:
            data = f.read()
            with open(cls.hostfile, 'w') as f2:
                f2.write(data)

    @staticmethod
    def clean_the_url(url: str):
        url = url.strip()
        url = url.removesuffix('/')
        if url.startswith('https://'):
            url = url.removeprefix('https://').strip()
        elif url.startswith('http://'):
            url = url.removeprefix('http://').strip()

        if url.startswith('www.'):
            url = url
        else:
            url = f"www.{url}"

        return url

    @classmethod
    def add_web_to_hostfile(cls, raw_url):
        with_www = cls.clean_the_url(raw_url)
        with open(cls.hostfile, 'a') as f:
            f.write('\n')
            f.write(f"0.0.0.0     {with_www}\n")
            f.write(f"0.0.0.0     {with_www.removeprefix('www.').strip()}\n")
            # f.write(f"0.0.0.0     {raw_url.strip()}\n")

    @classmethod
    def remove_web_from_hostfile(cls, url):
        with_www = cls.clean_the_url(url)
        with open(cls.hostfile, 'r') as f:
            whole_file = f.read()

        with open(cls.hostfile, 'r') as f:
            data = f.readlines()

        with open(cls.hostfile, 'w') as f:
            if url in whole_file:
                www = f"0.0.0.0     {with_www}\n"
                without_www = f"0.0.0.0     {with_www.removeprefix('www.').strip()}\n"
                # raw_url = f"0.0.0.0     {url}\n"

                data.remove(www)
                data.remove(without_www)
                # data.remove(raw_url)

            f.write(''.join(data))


class TimedBlocker:
    etc_folder = 'C:/Windows/System32/drivers/etc' if os.name == 'nt' else '/etc'
    # for how long the porn sites should be banned
    porn_ban_time_file = f'{etc_folder}/pornban_time.json'

    # for how long the the website should be banned
    web_ban_time_file = f'{etc_folder}/webban_time.json'

    @staticmethod
    def read_json(fp):
        with open(fp, 'r') as f:
            x = json.load(f)
            return x

    @staticmethod
    def write_json(fp, data):
        with open(fp, 'w') as f:
            y = json.dumps(data, indent=4)
            f.write(y)

    @classmethod
    def block_porn_sites_until(cls, strdatetime):
        PornBlocker.block_all_porn_sites()

        cls.write_json(cls.porn_ban_time_file, {'datetime': strdatetime})

    @classmethod
    def unblock_porn_sites(cls):
        PornBlocker.unblock_all_porn_sites()
        os.remove(cls.porn_ban_time_file)

    @classmethod
    def block_a_web_until(cls, url, strdatetime):
        if os.path.isfile(cls.web_ban_time_file):
            with open(cls.web_ban_time_file, 'r') as f:
                __data = f.read()
                if url in __data:
                    return

        PornBlocker.add_web_to_hostfile(url)

        # if the file does not exists then create a new file
        if not os.path.isfile(cls.web_ban_time_file):
            cls.write_json(cls.web_ban_time_file, {})

        data = cls.read_json(cls.web_ban_time_file)

        # adding the web and and its ban time to the file
        data[url] = strdatetime
        cls.write_json(cls.web_ban_time_file, data)

    @classmethod
    def unblock_a_web(cls, url):
        PornBlocker.remove_web_from_hostfile(url)
        data = cls.read_json(cls.web_ban_time_file)
        # remove the website from the "web_ban_time_file"
        del data[url]
        cls.write_json(cls.web_ban_time_file, data)


if __name__ == "__main__":
    pass
