import Domain.librarie


def create(lst_librarie, id_librarie, titlu_carte, gen_carte, pret, tip_reducere_client) -> object:
    '''
    Creeaza o librarie
    :rtype: object
    :param lst_librarie:
    :param id_librarie:
    :param titlu_carte:
    :param gen_carte:
    :param pret:
    :param tip_reducere_client:
    :return: o noua lista formata din lst_librarie si noua librarie adaugata
    '''
    librarie = Domain.librarie.creeaza_librarie(id_librarie, titlu_carte, gen_carte, pret, tip_reducere_client)
    return lst_librarie + [librarie]


def read(lst_librarie, id_librarie=None):
    '''
    Citeste o librarie din baza de date
    :param lst_librarie: lista librariilor
    :param id_librarie: id-ul librariilor dorite
    :return: libraria cu id-ul id_librarie sau lista cu toate librariile , daca id_librarie=None
    '''
    librarie_cu_id = None
    for librarie in lst_librarie:
        if Domain.librarie.get_id(librarie) == id_librarie:
            librarie_cu_id = librarie
    if librarie_cu_id:
        return librarie_cu_id
    return lst_librarie



def update(lst_librarie, new_librarie):
    '''
    Modifica o librarie
    :rtype: object
    :param carte: 
    :param carte1: 
    :param pret: 
    :param client: 
    :param lst_librarie: lista de librarii
    :param new_librarie: libraria care se va actualiza, id-ul trebuie sa fie unul existent
    :return: o lista cu libraria actualizata
    '''
    #lst_librarie = [p1:(1,cartea1), p2:(2, cartea2)], librarie=(2, cartea3)
    new_librarii = []
    for librarie in lst_librarie:
        if Domain.librarie.get_id(librarie) != Domain.librarie.get_id(new_librarie):
            new_librarii.append(new_librarie)
        else:
            new_librarii.append(librarie)
    return new_librarii

def delete(lst_librarie, id_librarie):
    '''
    TO DO
    :param lst_librarie:
    :param id_librarie:
    :return: o lista cu librarii fara librarii cu id-ul id_librarie
    '''
    new_librarie = []
    for librarie in lst_librarie:
        if Domain.librarie.get_id(librarie) != id_librarie:
            new_librarie.append(librarie)
    return new_librarie