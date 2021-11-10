from Domain.librarie import get_pret


def ordoneaza_crescator(carti, undo_list, redo_list):
    '''
    Ordoneaza vanzarile crescator dupa pret
    :param carti: lista vanzarilor
    :return: lista vanzarilor ordonate crescator dupa pret
    '''
    undo_list.append(carti)
    redo_list.clear()
    lst_carti = sorted(carti, key=lambda i: get_pret(i))
    return lst_carti