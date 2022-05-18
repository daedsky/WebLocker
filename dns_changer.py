import subprocess
import os


class DnsChanger:
    @classmethod
    def change_dns(cls, dns1: str, dns2: str, cmd: str):
        if os.name == 'nt':
            cls.change_dns_windows(dns1, dns2, cmd)
        else:
            cls.change_dns_linux(dns1, dns2, cmd)

    @classmethod
    def change_dns_windows(cls, dns1: str, dns2: str, cmd: str):
        interface_names = cls.get_interfaces()
        if cmd == 'block':
            for interface in interface_names:
                subprocess.call(['netsh', 'interface', 'ip', 'set', 'dns', interface, 'static', dns1, 'primary'])
                subprocess.call(['netsh', 'interface', 'ip', 'add', 'dns', interface, dns2, 'index=2'])
        elif cmd == 'unblock':
            for interface in interface_names:
                subprocess.call(['netsh', 'interface', 'ip', 'set', 'dns', interface, 'dhcp'])
        elif cmd == 'set':
            for interface in interface_names:
                subprocess.call(['netsh', 'interface', 'ip', 'set', 'dns', interface, 'static', dns1, 'primary'])

    @staticmethod
    def change_dns_linux(dns1: str, dns2: str, cmd: str):
        def create_backup():
            with open('/etc/resolv.conf', 'r') as f:
                data = f.read()
                with open('/etc/resolv.conf.backup', 'w') as file:
                    file.write(data)
        def write():
            with open('/etc/resolv.conf', 'w') as f:
                f.write('# Generated with WebLocker (https://github.com/daedsky/WebLocker)\n')
                f.write(f'nameserver {dns1}\n')
                f.write(f'nameserver {dns2}\n')

        if cmd == 'block':
            create_backup()
            subprocess.call(['sudo', 'rm', '/etc/resolv.conf'])
            write()
            subprocess.call(['sudo', 'chattr', '+i', '/etc/resolv.conf'])

        elif cmd == 'unblock':
            subprocess.call(['sudo', 'chattr', '-i', '/etc/resolv.conf'])
            with open('/etc/resolv.conf.backup', 'r') as f:
                data = f.read()
                with open('/etc/resolv.conf', 'w') as file:
                    file.write(data)
            subprocess.call(['sudo', 'rm', '/etc/resolv.conf.backup'])

        elif cmd == 'set':
            subprocess.call(['sudo', 'chattr', '-i', '/etc/resolv.conf'])
            write()
            subprocess.call(['sudo', 'chattr', '+i', '/etc/resolv.conf'])

    @staticmethod
    def get_interfaces():
        interface_names = []
        output = subprocess.check_output('netsh interface ip show config').decode('utf-8').split('\n')
        for line in output:
            if 'Loopback Pseudo-Interface 1' in line:
                pass
            elif 'Configuration for interface' in line:
                interface = line[29:-2]
                interface_names.append(interface)

        return interface_names

if __name__ == '__main__':
    pass