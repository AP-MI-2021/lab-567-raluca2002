from Domain.librarie import get_pret
from Logic.crud import read, create
from Logic.discount_reducere import discount_pt_reducere


def test_discount_pt_reducere():
    lst_carte = []
    lst_carte = create(lst_carte,'1', 'Mara', 'Drama', 44, 'none')
    lst_carte = create(lst_carte,'2', 'Razbunarea', 'Fictiune', 15, 'gold')
    lst_carte = create(lst_carte,'3', 'Ion', 'Dragoste', 30, 'silver')
    lst_carte = discount_pt_reducere(lst_carte)
    assert get_pret(read(lst_carte, '1' )) == 44
    assert get_pret(read(lst_carte, '2')) == 13.50
    assert get_pret(read(lst_carte, '3')) == 28.50