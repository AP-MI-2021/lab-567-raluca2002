from Domain.librarie import creeaza_carte, get_pret
from Logic.discount_reducere import discount_pt_reducere


def get_data():
    return [
        creeaza_carte(1, 'v1', 'gen1', 60, 'silver'),
        creeaza_carte(2, 'v2', 'gen2', 20, 'none'),
        creeaza_carte(3, 'v3', 'gen3', 12, 'gold'),
        creeaza_carte(4, 'v4', 'gen4', 34, 'silver'),
    ]

def test_discount_pt_reducere():
    carti = get_data()
    new_carti = discount_pt_reducere(carti, [], [])
    assert len(new_carti) == 4
    assert get_pret(new_carti[0]) == 57
    assert get_pret(new_carti[1]) == 20
    assert get_pret(new_carti[2]) == 10.8