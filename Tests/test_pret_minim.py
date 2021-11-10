from Domain.librarie import creeaza_carte
from Logic.pret_minim import pret_minim


def get_data():
    return [
        creeaza_carte(1, 'v1', 'gen1', 60, 'silver'),
        creeaza_carte(2, 'v2', 'gen1', 20, 'none'),
        creeaza_carte(3, 'v3', 'gen2', 12, 'gold'),
        creeaza_carte(4, 'v4', 'gen2', 34, 'silver'),
        creeaza_carte(5, 'v5', 'gen3', 23.02, 'none'),
    ]

def test_pret_minim():
    carti = get_data()
    rez = pret_minim(carti)
    assert rez['gen1'] == 20
    assert rez['gen2'] == 12
    assert rez['gen3'] == 23.02