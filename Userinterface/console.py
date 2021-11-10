from Domain.librarie import get_str, creeaza_carte
from Logic.crud import create, update, delete
from Logic.discount_reducere import discount_pt_reducere
from Logic.modificare_gen import modifica_gen_carte
from Logic.nr_titluri_distincte import nr_titluri_distincte
from Logic.pret_minim import pret_minim
from Logic.ordodeaza_crescator import ordoneaza_crescator
from Logic.undo_redo import do_undo, do_redo


def show_menu():
     print('1. CRUD')
     print('2. Aplica discount de 5% si 10% pentru reducerile de tip silver si gold')
     print('3. Modifica genul pentru un titlu dat.')
     print('4. Determina pretul minim pentru fiecare gen')
     print('5. Ordoneaza crescator dupa pret')
     print('6. Afisarea numarului de titluri distincte pentru fiecare gen')
     print('u. Undo')
     print('r. Redo')
     print('x. Exit')


def handle_add(carti, undo_list, redo_list):
    '''
    Adauga in lista de carti o carte creata de utilizator
    :param carti: lista de carti
    :return:
    '''
    try:
        id_carte = input('Dati id-ul cartii: ')
        titlu_carte = input('Dati numele cartii: ')
        gen_carte = input('Dati genul cartii: ')
        pret = float(input('Dati pretul cartii: '))
        tip_reducere_client = input('Dati tipul reducerii: ')
        return create(carti, id_carte, titlu_carte, gen_carte, pret, tip_reducere_client, undo_list, redo_list)
    except ValueError as ve:
        print('Eroare: ', ve)
    return carti

def handle_update(carti, undo_list, redo_list):
    '''
    Actualizeaza detaliile unei vanzari al carui id este dat de utilizator
    :param carti:
    :return:
    '''
    try:
        id_carte = input('Dati id-ul cartii care se actualizeaza: ')
        titlu_carte = input('Dati noul nume al cartii: ')
        gen_carte = input('Dati noul gen al cartii: ')
        pret = float(input('Dati noul pret al cartii: '))
        tip_reducere_client = input('Dati noul tip al reducerii: ')
        return update(carti, creeaza_carte(id_carte, titlu_carte, gen_carte, pret, tip_reducere_client), undo_list, redo_list)
    except ValueError as ve:
        print('Eroare: ', ve)
    return carti


def handle_delete(carti, undo_list, redo_list):
    '''
    Sterge din lista de carti, cartea cu id-ul dat de utilizator
    :param carti:
    :return:
    '''
    try:
        id_carte = input('Dati id-ul cartii care se va sterge: ')
        carti = delete(carti, id_carte, undo_list, redo_list)
        print('Stergerea a fost efectuata cu succes')
        return carti
    except ValueError as ve:
        print('Eroare: ', ve)
    return carti



def handle_discount(carti, undo_list, redo_list):
    return discount_pt_reducere(carti, undo_list, redo_list)


def handle_modificare(carti, undo_list, redo_list):
    titlu = input('Dati titlul cartii: ')
    gen_carte = input('Dati noul gen al cartii: ')
    print('Modificarea a fost efectuata cu succes')
    return modifica_gen_carte(carti, gen_carte, titlu, undo_list, redo_list )


def handle_pret_minim(carti):
    rez = pret_minim(carti)
    for gen in rez:
        print(f'Pretul minim pentru genul {gen} este {rez[gen]}')


def handle_ordoneaza_crescator(carti, undo_list, redo_list):
    return handle_show_all(ordoneaza_crescator(carti, undo_list, redo_list))


def handle_nr_titluri_distincte(carti):
    rez = nr_titluri_distincte(carti)
    for gen in rez:
        print(f'Pentru genul {gen} sunt {rez[gen]} titluri distincte')


def handle_show_all(carti):
    for carte in carti:
        print(get_str(carte))

def handle_undo(carti, undo_list, redo_list):
    undo_rez = do_undo(undo_list, redo_list, carti)
    if undo_rez is not None:
        return undo_rez
    return carti

def handle_redo(carti, undo_list, redo_list):
    redo_rez = do_redo(undo_list, redo_list, carti)
    if redo_rez is not None:
        return redo_rez
    return carti


def handle_crud(carti, undo_list, redo_list):

    while True:

        print('1. Adaugare')
        print('2. Modificare')
        print('3. Stergere')
        print('4. Discount')
        print('5. Modificare')
        print('6. Determina')
        print('7. Ordoneaza')
        print('8. Numar titluri distincte')
        print('u. Undo')
        print('r. Redo')
        print('y. Command')
        print('a. Afisare')
        print('b. Revenire')

        optiune = input('Optiune aleasa')
        if optiune == '1':
            carti = handle_add(carti,undo_list, redo_list)
        elif optiune == '2':
            carti = handle_update(carti, undo_list, redo_list)
        elif optiune == '3':
            carti = handle_delete(carti, undo_list, redo_list)
        elif optiune == '4':
            carti = handle_discount(carti, undo_list, redo_list)
        elif optiune == '5':
            carti = handle_modificare(carti, undo_list, redo_list)
        elif optiune == '6':
            carti = handle_pret_minim(carti)
        elif optiune == '7':
            carti = handle_ordoneaza_crescator(carti,undo_list, redo_list)
        elif optiune == '8':
            carti = handle_nr_titluri_distincte(carti)
        elif optiune == 'u':
            carti = handle_undo(carti, undo_list, redo_list)
        elif optiune == 'r':
            carti =  handle_redo(carti, undo_list, redo_list)
        elif optiune == 'a':
            handle_show_all(carti)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida')
    return carti


def run_ui(carti, undo_list, redo_list):
    while True:
        show_menu()
        optiune = input('Optiune aleasa: ')
        if optiune == '1':
            carti = handle_crud(carti, undo_list, redo_list)
        elif optiune == '2':
            carti = handle_discount(carti, undo_list, redo_list)
        elif optiune == '3':
            carti = handle_modificare(carti, undo_list, redo_list)
        elif optiune == '4':
            carti = handle_pret_minim(carti)
        elif optiune == '5':
            carti = handle_ordoneaza_crescator(carti, undo_list, redo_list)
        elif optiune == '6':
            carti = handle_nr_titluri_distincte(carti)
        elif optiune == 'u':
            carti = handle_undo(carti, undo_list, redo_list)
        elif optiune == 'r':
            carti =  handle_redo(carti, undo_list, redo_list)
        elif optiune == 'x':
            break
        else:
           print('Optiune invalida')
    return carti
