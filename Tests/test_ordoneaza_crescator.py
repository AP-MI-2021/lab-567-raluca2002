from Domain.librarie import creeaza_carte, get_id
from Logic.ordodeaza_crescator import ordoneaza_crescator


def get_data():
    return [
        creeaza_carte(1, 'v1', 'gen1', 60, 'silver'),
        creeaza_carte(2, 'v2', 'gen1', 20, 'none'),
        creeaza_carte(3, 'v3', 'gen2', 12, 'gold'),
        creeaza_carte(4, 'v5', 'gen3', 23.02, 'none'),
    ]
def test_ordoneaza_crescator():
    carti = get_data()
    carti = ordoneaza_crescator(carti)
    assert len(carti) == 4
    assert get_id(carti[0]) == 3
    assert get_id(carti[1]) == 2
    assert get_id(carti[2]) == 4
    assert get_id(carti[3]) == 1