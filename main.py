from Logic.crud import create
from Tests.test_crud import test_crud
from Tests.test_discount_reducere import test_discount_pt_reducere
from Tests.test_modificare_gen import test_modifica_gen
from Tests.test_nr_titluri_distincte import test_nr_titluri_distincte
from Tests.test_ordoneaza_crescator import test_ordoneaza_crescator
from Tests.test_pret_minim import test_pret_minim
from Userinterface.command_line_console import meniu
from Userinterface.console import run_ui
from Tests.test_undo_redo import test_undo_redo

def menus():
    print('1. Meniul standard')
    print('2. Meniul nou')
    print('x. Exit')


def main():
    carti = []
    undo_list = []
    redo_list = []
    carti = create(carti, 1, 'poezii', 'romatic', 45, 'gold', undo_list, redo_list)

    while True:
        menus()
        optiune = input('Alegeti meniul: ')
        if optiune == '1':
            carti = run_ui(carti, undo_list, redo_list)
        elif optiune == '2':
            carti = meniu(carti)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida ')

if __name__ == '__main__':
    test_crud()
    test_discount_pt_reducere()
    test_modifica_gen()
    test_pret_minim()
    test_ordoneaza_crescator()
    test_nr_titluri_distincte()
    test_undo_redo()
    main()
