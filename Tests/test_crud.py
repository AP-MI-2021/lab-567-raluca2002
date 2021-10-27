from typing import List, Dict, Any

from Domain.librarie import creeaza_librarie, get_id
from Logic.crud import create, read, update, delete


def get_data():
    return [creeaza_librarie(1, 't1', 'gen1', 100, 'silver'),
            creeaza_librarie(2, 't2', 'gen2', 50, 'gold'),
            creeaza_librarie(3, 't3', 'gen3', 150, 'none'),
            creeaza_librarie(4, 't4', 'gen4', 350, 'gold'),
            creeaza_librarie(5, 't5', 'gen5', 560, 'silver'),
            ]
def test_create():
    librarii = get_data()
    params = (100, 'tnew', 'gen new', 2021, 'gold')
    t_new = creeaza_librarie(*params)
    new_librarii: object = create(librarii, *params)
    assert len(new_librarii) == len(librarii)+1
    found = False
    for librarii in new_librarii:
        if librarii == t_new:
            return True
    assert found

def test_read():
    librarii = get_data()
    some_t = librarii[2]
    assert read(librarii, get_id(some_t)) == some_t
    assert read(librarii, None) == librarii

def test_update():
    librarii = get_data()
    t_updated = creeaza_librarie(1, 'new titlu', 'new gen', 111, 'silver')
    updated = update(librarii, t_updated)
    assert t_updated in updated
    assert t_updated not in librarii
    assert len(updated) == len(librarii)

def test_delete():
    librarii = get_data()
    to_delete = 3
    t_deleted = read(librarii, to_delete)
    deleted = delete(librarii, to_delete)
    assert t_deleted not in deleted
    assert t_deleted in librarii
    assert len(deleted) == len(librarii)-1

def test_crud():
    test_create()
    test_read()
    test_update()
    test_delete()