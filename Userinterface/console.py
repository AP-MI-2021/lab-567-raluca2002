from Domain.librarie import get_str
from Logic.crud import create, update, delete
from Logic.functionalitati import discount_pt_reducere


def show_menu():
    print('1. CRUD')
    print('2. Aplicare discount la anumite reduceri')
    print('3. Aplica discount de 5% si 10% pentru reducerile de tip silver si gold')
    print('x. Exit')


def handle_add(librarii):
     id_librarie = input('Dati id-ul librariei: ')
     titlu_carte = input('Dati numele cartii: ')
     gen_carte = input('Dati genul cartii: ')
     pret = float(input('Dati pretul cartii: '))
     tip_reducere_client = input('Dati tipul reducerii: ')
     return create(librarii, id_librarie, titlu_carte, gen_carte, pret, tip_reducere_client)

def handle_update(librarii):
    id_librarie = input('Dati id-ul librariei care se actualizeaza: ')
    titlu_carte = input('Dati noul nume al cartii: ')
    gen_carte = input('Dati noul gen al cartii: ')
    pret = float(input('Dati noul pret al cartii: '))
    tip_reducere_client = input('Dati noul tip al reducerii: ')
    return update(librarii, id_librarie)

def handle_discount(librarii):
    return discount_pt_reducere(librarii)

def handle_delete(librarii):
    id_librarie = input('Dati id-ul librariei care se va sterge: ')
    librarii = delete(librarii, id_librarie)
    print('Stergerea a fost efectuata cu succes')
    return librarii




def handle_show_all(librarii):
     for librarie in librarii:
         print(get_str(librarie))


def handle_crud(librarii):

    while True:
        print('1. Adaugare')
        print('2. Modificare')
        print('3. Stergere')
        print('4. Discount')
        print('a. Afisare')
        print('b. Revenire')

        optiune = input('Optiune aleasa')
        if optiune == '1':
            librarii = handle_add(librarii)
        elif optiune == '2':
            librarii = handle_update(librarii)
        elif optiune == '3':
            librarii = handle_delete(librarii)
        elif optiune == '4':
            librarii = handle_discount(librarii)
        elif optiune == 'a':
            handle_show_all(librarii)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida')
    return librarii


def run_ui(librarii):
    while True:
        show_menu()
        optiune = input('Optiune aleasa: ')
        if optiune == '1':
            librarii = handle_crud(librarii)
        elif optiune == '2':
            pass
        elif optiune == 'x':
            break
        else:
           print('Optiune invalida')
    return librarii
