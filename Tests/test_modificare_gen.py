from Domain.librarie import get_gen_carte, creeaza_carte
from Logic.modificare_gen import modifica_gen_carte, titlu_in_lst


def get_data():
    return [
        creeaza_carte(1, 'v1', 'gen1', 60, 'silver'),
        creeaza_carte(2, 'v2', 'gen2', 20, 'none'),
        creeaza_carte(3, 'v3', 'gen3', 12, 'gold'),
        creeaza_carte(4, 'v4', 'gen4', 34, 'silver'),
    ]

def test_modificare_gen():
    carti = get_data()
    carti = modifica_gen_carte(carti, 'v1', 'gennou1', [], [])
    carti = modifica_gen_carte(carti, 'v2', 'gennou2', [], [])
    assert get_gen_carte(carti[0]) == 'gennou1'
    assert get_gen_carte(carti[1]) == 'gennou2'
    try:
        _ = modifica_gen_carte(carti, 'v8' , 'gennou8', [], [])
        assert False
    except ValueError:
        assert True  # sau pass

def test_titlu_in_lst():
    carti = get_data()
    assert titlu_in_lst(carti, 'v1') == 1
    assert titlu_in_lst(carti, 'v2') == 2
    assert titlu_in_lst(carti, 'v7') is None

def test_modifica_gen():
    test_modificare_gen()
    test_titlu_in_lst()