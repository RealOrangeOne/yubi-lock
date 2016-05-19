import click
from sh import sudo
import os


BASE_DIR = os.path.dirname(os.path.realpath(__file__))


@click.command('install', short_help='Install required files for insertion detection')
@click.option('-v', '--verbose')
def cli(verbose):
    if verbose:
        print("Exporting UDEV rule...")
    sudo.cp(BASE_DIR + "../data/85-yubikey-screen-lock.rules", "/etc/udev/rules.d/85-yubikey-screen-lock.rules")
    print('Export complete!')
