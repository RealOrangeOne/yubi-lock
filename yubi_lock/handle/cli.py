import click, subprocess, os
from yubi_lock.api.yubikey import get_all_yubikeys, generate_ident
from yubi_lock.api.user import has_ident, get_username


@click.command('handle', short_help='Handler for inserting and removing drives')
@click.argument('action', type=click.Choice(["enable", "disable"]))
def cli(action):
    ident = generate_ident(get_all_yubikeys(False)[0])
    if not has_ident(ident):
        return 1

    session_id = subprocess.check_output(
        "/bin/loginctl list-sessions | grep USER | awk '{print $1}'".replace('USER', get_username()),
        shell=True
    ).decode().replace('\n', '')
    if action == 'enable':
        os.system("/bin/loginctl lock-session {}".format(session_id))
    elif action == 'disable':
        os.system("/bin/loginctl unlock-session {}".format(session_id))
    else:
        return 1
