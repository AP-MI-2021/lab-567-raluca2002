from Domain.carte import creeaza_carte, get_id


def create(lst_carte, id_carte, titlu_carte, gen_carte, pret, tip_reducere_client):
    '''
    Creeaza o carte
    :param lst_carte: lista de vanzari
    :param id_carte: string
    :param titlu_carte: string
    :param gen_carte: string
    :param pret: float
    :param tip_reducere_client: string
    :return: o noua lista formata din lst_carte si noua carte adaugata
    '''
    carte = creeaza_carte(id_carte, titlu_carte, gen_carte, pret, tip_reducere_client)
    return lst_carte + [carte]


def read(lst_carte, id_carte=None):
    '''
    Citeste o carte din baza de date
    :param lst_carte: lista cartilor
    :param id_carte: id-ul cartilor dorite
    :return: cartea cu id-ul id_carte sau lista cu toate cartile , daca id_carte=None
    '''
    carte_cu_id = None
    for carte in lst_carte:
        if get_id(carte) == id_carte:
            carte_cu_id = carte
    if carte_cu_id:
        return carte_cu_id
    return lst_carte



def update(lst_carte, new_carte):
    '''
    Modifica o carte
    :param lst_carte: lista cartilor
    :param new_carte: cartea care se va actualiza, id-ul trebuie sa fie unul existent
    :return: o lista cu cartea actualizata
    '''
    #lst_librarie = [p1:(1,cartea1), p2:(2, cartea2)], librarie=(2, cartea3)
    new_carti = []
    for carte in lst_carte:
        if get_id(carte) != get_id(new_carte):
            new_carti.append(new_carte)
        else:
            new_carti.append(carte)
    return new_carti

def delete(lst_carte, id_carte):
    '''
    TO DO
    :param lst_carte:
    :param id_carte:
    :return: o lista cu carti fara carti cu id-ul id_carte
    '''
    new_carte = []
    for carte in lst_carte:
        if get_id(carte) != id_carte:
            new_carte.append(carte)
    return new_carte