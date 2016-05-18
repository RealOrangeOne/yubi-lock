import yubico


def get_all_yubikeys(debug):
    keys = []
    try:
        skip = 0
        while skip < 255:
            key = yubico.find_yubikey(debug=debug, skip=skip)
            keys.append(key)
            skip += 1
    except yubico.yubikey.YubiKeyError:
        pass
    return keys
