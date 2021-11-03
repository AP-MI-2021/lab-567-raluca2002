from Domain.carte import get_gen_carte
from Logic.crud import create, read
from Logic.discount_reducere import discount_pt_reducere
from Logic.modificare_gen import modifica_gen_carte



def test_modifica_gen_carte():
   lst_carte = []
   lst_carte = create(lst_carte,'1', 'Mara', 'Drama', 44, 'none')
   lst_carte = create(lst_carte,'2', 'Razbunarea', 'Fictiune', 15, 'gold')
   lst_carte = create(lst_carte,'3', 'Ion', 'Romantic', 30, 'silver')
   lst_carte = modifica_gen_carte(lst_carte, 'Mara', 'Fictiune')

   assert get_gen_carte(read(lst_carte, '1')) == 'Fictiune'
   assert get_gen_carte(read(lst_carte, '3')) == 'Romantic'