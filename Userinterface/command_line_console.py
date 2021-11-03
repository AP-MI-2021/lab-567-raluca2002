from Logic.crud import create, update, delete, creeaza_carte
from Domain.librarie import get_str
from Logic.modificare_gen import modifica_gen_carte


def show_menu():
    print('1. CRUD')
    print('2. Aplica discount de 5% si 10% pentru reducerile de tip silver si gold')
    print('3. Modifica genul pentru un titlu dat.')
    print('4. Determina pretul minim pentru fiecare gen')
    print('y. Comand line console')
    print('x. Exit')


def handle_add(carti, command_line):
    id_carte = command_line[1]
    titlu_carte = command_line[2]
    gen_carte = command_line[3]
    pret = float(command_line[4])
    tip_reducere_client = command_line[5]
    return create(carti, id_carte, titlu_carte, gen_carte, pret, tip_reducere_client)


def handle_update(carti, command_line):
    id_carte = command_line[1]
    titlu_carte = command_line[2]
    gen_carte = command_line[3]
    pret = float(command_line[4])
    tip_reducere_client = command_line[5]
    return update(carti, creeaza_carte(id_carte, titlu_carte, gen_carte, pret, tip_reducere_client))


def handle_delete(carti, command_line):
    id_carte = command_line[1]
    carti = delete(carti, id_carte)
    print('Stergerea a fost efectuata cu succes')
    return carti



def handle_modificare(carti, command_line):
    titlu = command_line[1]
    gen_carte = command_line[2]
    print('Modificarea a fost efectuata cu succes')
    return modifica_gen_carte(gen_carte, titlu, carti)


def handle_show_all(carti):
    for carte in carti:
        print(get_str(carte))


def handle_crud():
            print(
                """
                Adaugare carti :id_obiect,nume, descriere, pret_achizitie, locatie
                Stergere carti : id_obiect
                Modificare obiect id_obiect,nume, descriere, pret achizitie, locatie
                Muta toate obiectele dintr-o locatie in alta: locatiedata, locatienoua
                Concateneaza un string la toate descrierile obiectelor cu un pret mai mare decat o anumita valoare : descriere, valoare" 
                Show all
                Iesire
                """
            )

def runMenu2(lista):
            while True:
                handle_crud()
                comenzi = input(
                    "Introduceti comenzile separate prin ';', iar detaliile pentru fiecare comanda separate prin ',': ")
                comenzi = comenzi.split(sep=";")

                for comanda in comenzi:
                    comanda = comanda.split(sep=",")
                    command_line = []

                    for command_line in comanda:
                        command_line.append(command_line)

                    if command_line[0] == "Adaugare obiect":
                        lista = handle_add(lista, command_line)

                    elif command_line[0] == "Stergere obiect":
                        handle_delete(lista, command_line)

                    elif command_line[0] == "Modificare obiect":
                        command_line(lista, command_line)

                    elif command_line[0] == "Show all":
                        handle_show_all(lista)

                    elif command_line[0] == "Iesire":
                        break

                    else:
                        print("Nu ati introdus o comanda valida!"
                              "Reincarcati.")


