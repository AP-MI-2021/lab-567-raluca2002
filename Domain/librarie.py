

def creeaza_librarie(id_carte: int,tiltu_carte: str,gen_carte: str,pret: int,tip_reducere_client: str):
    lista_librarie= [id_carte, tiltu_carte, gen_carte, pret, tip_reducere_client]
    return lista_librarie


def get_id(lista_librarie):

    return lista_librarie[0]

def get_titlu_carte(lista_librarie):

    return lista_librarie[1]

def get_gen_carte(lista_librarie):

    return lista_librarie[2]

def get_pret(lista_librarie):

     return lista_librarie[3]

def get_tip_reducere_client(lista_librarie):

    return lista_librarie[4]

def get_str(librarie):
    return f'Libraria cu id-ul {get_id(librarie)}, cu titlul {get_titlu_carte(librarie)}, genul {get_gen_carte(librarie)}, pretul {get_pret(librarie)} si tipul de reducere {get_tip_reducere_client(librarie)}'
