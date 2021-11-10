from Domain.librarie import get_str
from Logic.crud import create, delete, update


from Domain.librarie import creeaza_carte
from Logic.crud import create, delete, update
from Userinterface.console import handle_show_all


def read_list():
    lst = []
    lst_str = input("Introduceti comanda respectand instructiunile date: ")
    lst_str_split = lst_str.split('; ')
    for comanda in lst_str_split:
        lst.append(comanda)
    return lst


def handle_n_add(carti, comanda):
    try:
        id_carte = int(comanda[1])
        titlu_carte = comanda[2]
        gen_carte = comanda[3]
        pret = float(comanda[4])
        tip_reducere_client = comanda[5]
        return create(carti, id_carte, titlu_carte, gen_carte, pret, tip_reducere_client)
    except ValueError as ve:
        print('Eroare: ', ve)

    return carti


def handle_n_delete(carti, comanda):
    try:
        id_carte = int(comanda[1])
        carti = delete(carti, id_carte)
        return carti
    except ValueError as ve:
        print('Eroare: ', ve)
    return carti


def handle_n_update(carti, comanda):
    try:
        id_carte = int(comanda[1])
        titlu_carte = comanda[2]
        gen_carte = comanda[3]
        pret = float(comanda[4])
        tip_reducere_client = comanda[5]
        return update(carti, creeaza_carte(id_carte, titlu_carte, gen_carte, pret, tip_reducere_client))
    except ValueError as ve:
        print('Eroare:', ve)
    return carti


def new_menu(carti):
    while True:
        print("Intr-o linie de comanda se vor scrie comenzile "
              "care se vor aplica listei, separate prin ';', elementele acestora fiind separate prin ','.")
        print("Atentie ! Comanda se face prin scrierea cu majuscula si dupa fiecare separator(; si ,) se va pune un spatiu.")
        print("O comanda care nu se regaseste in lista de mai jos nu va duce la modificarea listei.")
        print("O comanda trebuie sa aiba toate campurile nenule \n ")

        print("1.Pentru a adauga in lista tastati: Adaugare, id_vanzare(valoare intreaga), titlu, gen, "
              "pret(valoare reala), tip(none, silver sau gold)")
        print("2.Pentru stergerea unei carti tastati: Sterge, id_vanzare(valoare intreaga)")
        print("3.Pentru modificarea unei carti tastati: Modificare, id_vanzare(valoare intreaga), titlu, gen, "
              "pret(valoare reala), tip(none, silver sau gold)")
        print("4.Pentru afisarea tuturor cartilor tastati: ShowAll")
        print("5. Pentru iesire din meniu: Exit ")
        lst_cmd = read_list()
        for comanda in lst_cmd:
            comanda = comanda.split(', ')
            if (comanda[0] == 'Adaugare'):
                carti = handle_n_add(carti, comanda)
            elif (comanda[0] == 'Sterge'):
                carti = handle_n_delete(carti, comanda)
            elif (comanda[0] == 'Modificare'):
                carti = handle_n_update(carti, comanda)
            elif (comanda[0] == 'ShowAll'):
                handle_show_all(carti)
        if 'Exit' in lst_cmd:
            break






