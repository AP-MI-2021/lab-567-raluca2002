from typing import List, Dict, Any

from Domain.librarie import creeaza_carte, get_id
from Logic.crud import create, read, update, delete
from Tests.test_discount_reducere import test_discount_pt_reducere
from Tests.test_modificare_gen import  test_modifica_gen
from Tests.test_nr_titluri_distincte import test_nr_titluri_distincte
from Tests.test_ordoneaza_crescator import test_ordoneaza_crescator
from Tests.test_pret_minim import test_pret_minim
from Tests.test_undo_redo import test_undo_redo


def get_data():
    return [creeaza_carte(1, 't1', 'gen1', 100, 'silver'),
            creeaza_carte(2, 't2', 'gen2', 50, 'gold'),
            creeaza_carte(3, 't3', 'gen3', 150, 'none'),
            creeaza_carte(4, 't4', 'gen4', 350, 'gold'),
            creeaza_carte(5, 't5', 'gen5', 560, 'silver'),
            ]


def test_create():
    carti = get_data()
    params = (6, 'tnew', 'gen new', 474, 'none', [], [])
    t_new = creeaza_carte(*params[:-2])
    new_carti = create(carti, *params)
    assert len(new_carti) == len(carti) + 1
    assert t_new in new_carti


    params2 = (6, 'tnew', 'gen new', 474, 'none', [], [])
    try:
        some_t = create(new_carti, *params2)
        assert False
    except ValueError:
        assert True


def test_read():
    carti = get_data()
    some_t = carti[2]
    assert read(carti, get_id(some_t)) == some_t
    assert read(carti, None) == carti


def test_update():
    carti = get_data()
    t_updated = creeaza_carte(1, 'new titlu', 'new gen', 111, 'silver')
    updated = update(carti, t_updated, [], [])
    assert t_updated in updated
    assert t_updated not in carti
    assert len(updated) == len(carti)
    try:
        params2 = (7, 'new titlu', 'gen new', 26, 'none', [], [])
        t_updated = creeaza_carte(*params2[:-2])
        some_t = update(carti, t_updated, [], [])
        assert False
    except ValueError:
        assert True


def test_delete():
    carti = get_data()
    to_delete = 3
    t_deleted = read(carti, to_delete)
    deleted = delete(carti, to_delete, [], [])
    assert t_deleted not in deleted
    assert t_deleted in carti
    assert len(deleted) == len(carti) - 1
    try:
        to_delete = 7
        some_t = delete(carti, to_delete, [], [])
        assert False
    except ValueError:
        assert True


def test_crud():
    test_create()
    test_read()
    test_update()
    test_delete()
