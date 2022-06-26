from utrello import model

import pytest


def test_csv():
    pass


def test_card_from_args():
    card = model.Card(name='Test card', desc='Empty desc', idList='abc123')

    args = {'name': 'Test card', 'desc': 'Empty desc', 'idList': 'abc123'}
    new_card = model.card_from_dict(args)

    assert card == new_card