from typing import List, Dict, Any

from Domain.carte import creeaza_carte, get_id
from Logic.crud import create, read, update, delete
from Tests.test_discount_reducere import test_discount_pt_reducere
from Tests.test_modificare_gen import  test_modifica_gen_carte
from Tests.test_pret_minim import test_pret_minim


def get_data():
    return [creeaza_carte(1, 't1', 'gen1', 100, 'silver'),
            creeaza_carte(2, 't2', 'gen2', 50, 'gold'),
            creeaza_carte(3, 't3', 'gen3', 150, 'none'),
            creeaza_carte(4, 't4', 'gen4', 350, 'gold'),
            creeaza_carte(5, 't5', 'gen5', 560, 'silver'),
            ]
def test_create():
    carti = get_data()
    params = (100, 'tnew', 'gen new', 2021, 'gold')
    t_new = creeaza_carte(*params)
    new_carti = create(carti, *params)
    assert len(new_carti) == len(carti)+1
    found = False
    for carti in new_carti:
        if carti == t_new:
            return True
    assert found

def test_read():
    carti = get_data()
    some_t = carti[2]
    assert read(carti, get_id(some_t)) == some_t
    assert read(carti, None) == carti

def test_update():
    carti = get_data()
    t_updated = creeaza_carte(1, 'new titlu', 'new gen', 111, 'silver')
    updated = update(carti, t_updated)
    assert t_updated in updated
    assert t_updated not in carti
    assert len(updated) == len(carti)

def test_delete():
    carti = get_data()
    to_delete = 3
    t_deleted = read(carti, to_delete)
    deleted = delete(carti, to_delete)
    assert t_deleted not in deleted
    assert t_deleted in carti
    assert len(deleted) == len(carti)-1

def test_crud():
    test_create()
    test_read()
    test_update()
    test_delete()
    test_discount_pt_reducere()
    test_modifica_gen_carte()
    test_pret_minim()