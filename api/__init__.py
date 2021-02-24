import os
import json


_config_path = './config.json'


def _create_config():
    """
    Creates a default config file
    :return: None
    """
    data = {'ip': '192.0.0.1', 'port': '1880', 'save': False, 'flag': True}

    with open(_config_path, 'w') as conf_file:
        json.dump(data, conf_file)


"""
This code is run whenever parts of the api package are imported.
It makes sure a config file exists. First checking if one is already present and creating one if not
"""
if not os.path.isfile(_config_path):
    print("No configuration file found. Creating default configuration file")
    _create_config()

with open(_config_path) as config_file:
    _config = json.load(config_file)


def _write_config():
    """
    Writes the current configuration as json file and therefore saves it
    :return: None
    """
    if os.path.isfile(_config_path):
        os.remove(_config_path)

    with open(_config_path, 'w') as config_file:
        json.dump(_config, config_file)


def set_ip(ip, store=False):
    """
    Change the ip of the current config
    :param ip: New ip to use
    :param store: Should it save the new configuration in json?
    :return: None
    """
    _config['ip'] = ip
    if store:
        _write_config()


def set_port(port, store=False):
    """
    Change the port of the current config
    :param port: new port to use
    :param store: Should it save the new configuration in json?
    :return: None
    """
    _config['port'] = port
    if store:
        _write_config()


def set_use_save_connection(use_save_connection, store=False):
    """
    Determines the usage of HTTP or HTTPS
    :param use_save_connection: Should HTTPS be used?
    :param store: Should it save the new configuration in json?
    :return: None
    """
    _config['save'] = use_save_connection
    if store:
        _write_config()


def first_time():
    """
    Used to determine if this package has already been worked with before or if it is the first time using it.
    :return: Is it first time use?
    """
    flag = _config['flag']
    if flag:
        _config['flag'] = False
        _write_config()
    return flag
