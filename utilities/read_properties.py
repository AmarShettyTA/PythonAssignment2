import configparser

config_path = "config.ini"

config_parser = configparser.RawConfigParser()
config_parser.read(config_path)


def get_url():
    return config_parser.get('url', 'login_url')


def get_username():
    return config_parser.get('credentials', 'username')


def get_password():
    return config_parser.get('credentials', 'password')
