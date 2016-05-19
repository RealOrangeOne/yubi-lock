import click
import os
from yubi_lock.api import BASE_DIR


@click.command('install', short_help='Install required files for insertion detection')
def cli():
    exit_code = os.system("sudo cp {} {}".format(BASE_DIR + "../data/85-yubikey-screen-lock.rules", "/etc/udev/rules.d/85-yubikey-screen-lock.rules"))
    if exit_code == 0:
        print('Export complete!')
    else:
        print('Something went wrong!')
