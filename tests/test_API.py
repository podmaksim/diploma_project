from pages.api.api_def import create_user
from pages.api.api_def import choice_user
from pages.api.api_def import update_user
from pages.api.api_def import choice_new_user
from conftest import api_user_config_data

import random
import pytest

id = ''.join([random.choice('12345') for x in range(3)])
user_name, password, new_user_name = api_user_config_data()


def test_POST():
    assert create_user(id, user_name, password) == \
           {'code': 200, 'type': 'unknown', 'message': id}


def test_GET_positive_1():
    assert choice_user(user_name) == 200


def test_GET_positive_2():
    assert choice_user('1') == 404


@pytest.mark.xfail
def test_GET_negative():
    assert choice_user('') == 200


def test_PUT_positive():
    assert update_user(id, user_name, new_user_name) == \
           {'code': 200, 'type': 'unknown', 'message': id}


@pytest.mark.xfail
def test_PUT_negative():
    assert update_user(id, '', new_user_name) == \
           {'code': 200, 'type': 'unknown', 'message': id}


def test_GET_new_user_positive():
    assert choice_new_user(new_user_name) == 200


@pytest.mark.xfail
def test_GET_new_user_negative():
    assert choice_new_user('IlonMask') == 200
