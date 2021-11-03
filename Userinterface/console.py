from Domain.carte import get_str, creeaza_carte
from Logic.crud import create, update, delete
from Logic.discount_reducere import discount_pt_reducere
from Logic.modificare_gen import modifica_gen_carte
from Logic.pret_minim import pret_minim


def show_menu():
     print('1. CRUD')
     print('2. Aplica discount de 5% si 10% pentru reducerile de tip silver si gold')
     print('3. Modifica genul pentru un titlu dat.')
     print('4. Determina pretul minim pentru fiecare gen')
     print('x. Exit')


def handle_add(carti):
     id_carte = input('Dati id-ul cartii: ')
     titlu_carte = input('Dati numele cartii: ')
     gen_carte = input('Dati genul cartii: ')
     pret = float(input('Dati pretul cartii: '))
     tip_reducere_client = input('Dati tipul reducerii: ')
     return create(carti, id_carte, titlu_carte, gen_carte, pret, tip_reducere_client)

def handle_update(carti):
     id_carte = input('Dati id-ul cartii care se actualizeaza: ')
     titlu_carte = input('Dati noul nume al cartii: ')
     gen_carte = input('Dati noul gen al cartii: ')
     pret = float(input('Dati noul pret al cartii: '))
     tip_reducere_client = input('Dati noul tip al reducerii: ')
     return update(carti, creeaza_carte(id_carte, titlu_carte, gen_carte, pret, tip_reducere_client))



def handle_delete(carti):
     id_carte = input('Dati id-ul cartii care se va sterge: ')
     carti = delete(carti, id_carte)
     print('Stergerea a fost efectuata cu succes')
     return carti


def handle_discount(carti):
    return discount_pt_reducere(carti)


def handle_modificare(carti):
     titlu = input('Dati titlul cartii: ')
     gen_carte = input('Dati noul gen al cartii: ')
     print('Modificarea a fost efectuata cu succes')
     return modifica_gen_carte(gen_carte, titlu, carti)

def handle_pret_minim(carti):
    rez = pret_minim(carti)
    for gen in rez:
        print('Genul {} are pretul minim de {} '.format(gen, rez[gen]))

def handle_show_all(carti):
     for carte in carti:
         print(get_str(carte))


def handle_crud(carti):

    while True:
        print('1. Adaugare')
        print('2. Modificare')
        print('3. Stergere')
        print('4. Discount')
        print('5. Modificare')
        print('6. Determina')
        print('a. Afisare')
        print('b. Revenire')

        optiune = input('Optiune aleasa')
        if optiune == '1':
            carti = handle_add(carti)
        elif optiune == '2':
            carti = handle_update(carti)
        elif optiune == '3':
            carti = handle_delete(carti)
        elif optiune == '4':
            carti = handle_discount(carti)
        elif optiune == '5':
            carti = handle_modificare(carti)
        elif optiune == '6':
            carti = handle_pret_minim(carti)
        elif optiune == 'a':
            handle_show_all(carti)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida')
    return carti


def run_ui(carti):
    while True:
        show_menu()
        optiune = input('Optiune aleasa: ')
        if optiune == '1':
            carti = handle_crud(carti)
        elif optiune == '2':
            carti = handle_discount(carti)
        elif optiune == '3':
            carti = handle_modificare(carti)
        elif optiune == '4':
            carti = handle_pret_minim(carti)
        elif optiune == 'x':
            break
        else:
           print('Optiune invalida')
    return carti
