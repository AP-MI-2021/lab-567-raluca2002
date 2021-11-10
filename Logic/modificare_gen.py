from Domain.librarie import get_titlu_carte, creeaza_carte, get_id, get_pret, get_tip_reducere_client


def modifica_gen_carte(carti, titlu, gen_carte, undo_list, redo_list):
    '''
    Modifica genul cartii pentru un titlu dat
    :param gen_carte: string
    :param titlu: string
    :param carti: lista cartilor
    :undo_list:
    :redo_list:
    :return: genul modificat al cartii
    '''
    if titlu_in_lst(carti, titlu) is None:
        raise  ValueError('Ati introdus un titlu care nu se gaseste in lista')
    new_lst = []
    for vanz in carti:
        if get_titlu_carte(vanz) == titlu:
            carte_noua = creeaza_carte(get_id(vanz),
                                    get_titlu_carte(vanz),
                                    gen_carte,
                                    get_pret(vanz),
                                    get_tip_reducere_client(vanz),
                                    )
            new_lst.append(carte_noua)
        else:
            new_lst.append(vanz)
    undo_list.append(carti)
    redo_list.clear()
    return new_lst

def titlu_in_lst(lst_carti, titlu):
    '''
    verificam daca titlu dat se gaseste in lista de vanzari
    :param lst_carti: lista de carti
    :param titlu: titlu de verificat
    :return: id-ul vanzarii, daca exista in lista sau None in caz contrar
    '''
    vanzare_id =None
    for carte in lst_carti:
        if get_titlu_carte(carte) == titlu:
            vanzare_id = get_id(carte)
    if vanzare_id:
        return vanzare_id
    return None