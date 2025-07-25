import sys


def str2int(value):
    try:
        logical_xlog, segment = value.rsplit('/', 1)
    except ValueError:
        return 'invalid value'

    logical_xlog = int(logical_xlog, 16)
    segment = int(segment, 16)

    return (logical_xlog << 32) | segment


def int2str(value):
    logical_xlog = (value >> 32) & 0xffffffff
    segment = value & 0xffffffff
    return f'{logical_xlog:X}/{segment:X}'


def transfer(value):
    try:
        value = int(value)
    except ValueError:
        print_value(value, str2int(value))
    else:
        print_value(value, int2str(value))


def print_help():
    print(f'Usage: python {__file__} [lsn] ...')
    print('Converts PostgreSQL LSNs (Log Sequence Numbers) to integers and vice-versa. ')
    print(
        'For instance, the string 5/559D8D30 becomes 22911225136, and 22911225136 converts back to 5/559D8D30.')


def print_value(raw, new):
    print(raw, ': ', new, sep='')


def main():
    if len(sys.argv) < 2:
        return print_help()

    for value in sys.argv[1:]:
        transfer(value)


if __name__ == '__main__':
    main()
