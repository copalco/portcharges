import configparser


def read_ini(path):
    parser = configparser.ConfigParser()
    parser.read(path)
    return parser['DEFAULT']
