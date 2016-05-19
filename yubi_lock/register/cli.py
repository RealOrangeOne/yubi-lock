import click
from yubi_lock.api.yubikey import get_all_yubikeys, generate_ident
from yubi_lock.api.user import store_key


@click.command('register', short_help='Add a device')
def cli():
    print("Scanning for keys...")
    keys = get_all_yubikeys(False)

    if not keys:
        print("No YubiKeys detected!")
        return 1
    elif len(keys) > 1:
        print("Please only insert the YubiKey you wish to register. Found {}.".format(len(keys)))
        return 1

    key = keys[0]
    print("Found {} with Serial {}.".format(key.description, key.serial()))
    ident = generate_ident(key)
    store_key(ident)
    print("YubiKey has been stored, you can now use it to login")
