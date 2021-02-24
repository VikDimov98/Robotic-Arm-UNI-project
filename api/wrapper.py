import os
import json
import requests
from api import _config


def _create_request_url():
    """
    Generates the request URL from the current configuration
    :return: Request URL as string
    """
    url = 'http'
    if _config['save']:
        url += 's'
    url += '://{}:{}/move'.format(_config['ip'], _config['port'])
    return url


def _send_request(f1=None, f2=None, f3=None, f4=None, f5=None):
    """
    Internally used to send a request. Gets request URL and sends a request using the request package.
    Fingers for which no parameter is passed are not moved
    :param f1: Finger 1 extend
    :param f2: Finger 2 extend
    :param f3: Finger 3 extend
    :param f4: Finger 4 extend
    :param f5: Finger 5 extend
    :return: None
    """
    payload = {}
    if f1 is not None:
        payload['f1'] = _clamp_percent(f1)
    if f2 is not None:
        payload['f2'] = _clamp_percent(f2)
    if f3 is not None:
        payload['f3'] = _clamp_percent(f3)
    if f4 is not None:
        payload['f4'] = _clamp_percent(f4)
    if f5 is not None:
        payload['f5'] = _clamp_percent(f5)
    try:
        r = requests.get(_create_request_url(), params=payload)
        print("Request returned status: {}".format(r.status_code))
    except:
        print("Unable to connect")


def _clamp_percent(value):
    """
    Clamps a given value between 0 and 100.
    :param value: Value to clamp
    :return: Clamped value
    """
    if value < 0:
        print("Less than 0 percent specified for extension. Clamping to 0")
        value = 0
    elif value > 100:
        print("More than 100 percent specified for extension. Clamping to 100")
        value = 100
    return value


def move_finger1(percent):
    """
    Moves only finger 1
    :param percent: Extension percent
    :return: None
    """
    percent = _clamp_percent(percent)
    _send_request(f1=percent)


def move_finger2(percent):
    """
    Moves only finger 2
    :param percent: Extension percent
    :return: None
    """
    percent = _clamp_percent(percent)
    _send_request(f2=percent)


def move_finger3(percent):
    """
    Moves only finger 3
    :param percent: Extension percent
    :return: None
    """
    percent = _clamp_percent(percent)
    _send_request(f3=percent)


def move_finger4(percent):
    """
    Moves only finger 4
    :param percent: Extension percent
    :return: None
    """
    percent = _clamp_percent(percent)
    _send_request(f4=percent)


def move_finger5(percent):
    """
    Moves only finger 5
    :param percent: Extension percent
    :return: None
    """
    percent = _clamp_percent(percent)
    _send_request(f5=percent)


def move_hand(f1, f2, f3, f4, f5):
    """
    Moves the whole hand
    :param f1: Finger 1 extend
    :param f2: Finger 2 extend
    :param f3: Finger 3 extend
    :param f4: Finger 4 extend
    :param f5: Finger 5 extend
    :return:
    """
    _send_request(f1=f1, f2=f2, f3=f3, f4=f4, f5=f5)


def move_fingers(f1=None, f2=None, f3=None, f4=None, f5=None):
    """
    Moves all fingers specified. Unspecified fingers are not moved
    :param f1: Finger 1 extend
    :param f2: Finger 2 extend
    :param f3: Finger 3 extend
    :param f4: Finger 4 extend
    :param f5: Finger 5 extend
    :return: None
    """
    _send_request(f1=f1, f2=f2, f3=f3, f4=f4, f5=f5)
