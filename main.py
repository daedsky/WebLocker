import ctypes
import sys
import os
import subprocess
from frontend import start_app


def is_admin():
    if os.name == 'nt':
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    else:
        if os.getuid() == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    if is_admin():
        start_app()
    else:
        # Re-run the program with admin rights
        if os.name == 'nt':
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        else:
            subprocess.call(['sudo', sys.executable, sys.argv[0]])