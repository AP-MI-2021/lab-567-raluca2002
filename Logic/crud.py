from Domain.librarie import creeaza_carte, get_id


def create(lst_carte, id_carte, titlu_carte, gen_carte, pret, tip_reducere_client, undo_list, redo_list):
    f'''
    Creeaza o carte
    :param lst_carte: lista de vanzari
    :param id_carte: string
    :param titlu_carte: string
    :param gen_carte: string
    :param pret: float
    :param tip_reducere_client: string
    :undo_list: 
    :redo_list:
    :return: o noua lista formata din lst_carte si noua carte adaugata
    '''
    if read(lst_carte, id_carte) is not None:
        raise ValueError(f'Exista deja o vanzare cu id-ul {id_carte}')
    if tip_reducere_client != 'silver' and tip_reducere_client != 'gold' and tip_reducere_client != 'none':
        raise ValueError('Ati introdus un tip de reducere care nu exista')
    if pret < 0:
        raise ValueError('Pretul nu poate sa fie negativ')

    carte = creeaza_carte(id_carte, titlu_carte, gen_carte, pret, tip_reducere_client)
    undo_list.append(lst_carte)
    redo_list.clear()
    return lst_carte + [carte]


def read(lst_carte, id_carte=None):
    '''
    Citeste o carte din baza de date
    :param lst_carte: lista cartilor
    :param id_carte: id-ul cartilor dorite
    :return: cartea cu id-ul id_carte sau lista cu toate cartile , daca id_carte=None
    '''

    if not id_carte:
        return lst_carte
    carte_cu_id = None

    for carte in lst_carte:
        if get_id(carte) == id_carte:
            carte_cu_id = carte
    if carte_cu_id:
        return carte_cu_id
    return None


def update(lst_carte, new_carte, undo_list, redo_list):
    '''
    Modifica o carte
    :param lst_carte: lista cartilor
    :param new_carte: cartea care se va actualiza, id-ul trebuie sa fie unul existent
    :undo_list:
    :refo_list:
    :return: o lista cu cartea actualizata
    '''
    if read(lst_carte, get_id(new_carte)) is None:
        raise ValueError(f'Nu exita o vanzare cu id-ul {get_id(new_carte)}')
    #lst_librarie = [p1:(1,cartea1), p2:(2, cartea2)], librarie=(2, cartea3)
    new_carti = []
    for carte in lst_carte:
        if get_id(carte) != get_id(new_carte):
            new_carti.append(carte)
        else:
            new_carti.append(new_carte)
    undo_list.append(lst_carte)
    redo_list.clear()
    return new_carti

def delete(lst_carte, id_carte, undo_list, redo_list):
    '''
    Sterge o carte
    :param lst_carte: lista cartilor
    :param id_carte: id-ul cartii care o sa fie sterse
    :undo_list:
    :redo_list:
    :return: o lista cu carti fara carti cu id-ul id_carte
    '''
    if read(lst_carte, id_carte) is None:
        raise ValueError(f'Nu exista o carte cu id-ul {id_carte}')
    new_carte = []
    for carte in lst_carte:
        if get_id(carte) != id_carte:
            new_carte.append(carte)
    undo_list.append(lst_carte)
    redo_list.clear()
    return new_carte

def generare():
    carti = []
    carti = create(carti, '1', 'Harry Potter', 'Fictiune', 45, 'silver', [], [])
    carti = create(carti, '2', 'La rascruce de vanturi', 'Roman', 35, 'none', [], [])
    carti = create(carti, '3', 'Moara cu noroc', 'Fictiune', 20, 'gold', [], [])
    carti = create(carti, '4', 'Ion', 'Realism', 30, 'none', [], [])
    carti = create(carti, '5', 'Descult', 'Roman', 50, 'silver', [], [])

    return carti