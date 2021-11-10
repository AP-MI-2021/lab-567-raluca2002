from Domain.librarie import creeaza_carte
from Logic.nr_titluri_distincte import nr_titluri_distincte


def get_data():
    return [
        creeaza_carte(1, 'v1', 'gen1', 60, 'silver'),
        creeaza_carte(2, 'v2', 'gen2', 20, 'none'),
        creeaza_carte(3, 'v3', 'gen2', 12, 'gold'),
        creeaza_carte(4, 'v4', 'gen4', 34, 'silver'),
        creeaza_carte(5, 'v2', 'gen2', 34, 'silver'),
        creeaza_carte(6, 'v4', 'gen4', 34, 'silver'),
        creeaza_carte(7, 'v4', 'gen4', 34, 'silver'),
    ]


def test_nr_titluri_distincte():
    carti = get_data()
    rez = nr_titluri_distincte(carti)
    assert rez['gen1'] == 1
    assert rez['gen2'] == 2
    assert rez['gen4'] == 1
