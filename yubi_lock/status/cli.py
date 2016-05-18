import click
from yubi_lock.api.yubikey import get_all_yubikeys


@click.command('status', short_help='List connected devices.')
def cli():
    print('Scanning for keys...')
    keys = get_all_yubikeys(False)
    for key in keys:
        print("Found {}!".format(key.description))
