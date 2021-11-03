from Logic.crud import create
from Logic.pret_minim import pret_minim


def test_pret_minim():
    lst_carte = []
    lst_carte = create(lst_carte, 1, "Enigma Otiliei", "Roman realist", 12, "Gold")
    lst_carte = create(lst_carte, 2, "Harap-Alb", "basm", 15, "None")
    lst_carte = create(lst_carte, 3, "Ion", "Roman realist", 30, "Gold")
    rez = pret_minim(lst_carte)
    assert rez["basm"] == 15
    assert rez["Roman realist"] == 12