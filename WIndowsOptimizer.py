import os
from tkinter import *

import psutil


def ip_config():
    os.system('cls')
    print('Running IP Config...')
    try:
        os.system('ipconfig /release')
        os.system('ipconfig /renew')
        os.system('ipconfig /flushdns')
        os.system('netsh int tcp set global ecncapability=disabled')
        os.system('netsh winsock reset')
        os.system('netsh interface ipv4 add dnsserver "Ethernet" address=1.1.1.1 index=1')
        os.system('netsh interface ipv4 add dnsserver "Ethernet" address=1.0.0.1 index=2')
        os.system('netsh interface ipv4 add dnsserver "Ethernet" address=8.8.8.8 index=3')
        os.system('netsh interface ipv4 add dnsserver "Ethernet" address=8.8.4.4 index=4')
        os.system('ipconfig /all')

    except Exception as e:
        print(f'Need a admin permission | Exception {e}')


def disk_config():
    os.system('cls')
    print('Running Disk Config...')
    try:
        total_ram = psutil.virtual_memory().total
        total_ram_mb = total_ram * 0.000001
        os.system(f'bcdedit /set increaseuserva {total_ram_mb} ')
        os.system('bcdedit /set useplatformtick yes')
        os.system('bcdedit /set disabledynamictick yes')
    except Exception as e:
        print(f'Need a admin permission | Exception {e}')


def file_config():
    os.system('cls')
    print('Running File Config...')
    try:
        os.system('fsutil behavior query memoryusage')
        os.system('fsutil behavior set memoryusage 2')
    except Exception as e:
        print(f'Need a admin permission | Exception {e}')


def upgade_apps():
    os.system('cls')
    print('Running Upgrade Apps...')
    try:
        os.system('winget upgrade -r --all --force --include-unknown --accept-package-agreements')
    except Exception as e:
        print(f'Need a admin permission | Exception {e}')


root = Tk()
root.title = 'Optmizer'
root.geometry('200x300')

config_ip = Button(root, text='Config IP', command=ip_config)
config_ip.pack(side=TOP, padx=5, pady=10, ipadx=30, ipady=10, expand=True)

config_disk = Button(root, text='Config Disk', command=disk_config)
config_disk.pack(side=TOP, padx=5, pady=10, ipadx=30, ipady=10, expand=True)

config_file = Button(root, text='Config Files', command=file_config)
config_file.pack(side=TOP, padx=5, pady=10, ipadx=30, ipady=10, expand=True)

upgrade_apps = Button(root, text='Upgrade Apps', command=upgade_apps)
upgrade_apps.pack(side=TOP, padx=5, pady=10, ipadx=30, ipady=10, expand=True)

root.mainloop()
