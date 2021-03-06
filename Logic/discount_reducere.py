from Domain.librarie import get_tip_reducere_client, creeaza_carte, get_pret, get_gen_carte, get_titlu_carte, get_id


def discount_pt_reducere(carti, undo_list, redo_list):
    '''
    Aplicam un discount de 5% pentru reducerile silver si un discount de 10% pentru reducerile gold
    :param carti:
    :param lst: lista cartilor
    :undo_list: o lista care memoreaza lista de vanzari inainte de modificare
    :redo_list: o lista care memoreaza lista de vanzari dupa modificari
    :return: lista cartilor cu modificarile cerute
    '''
    new_lst = []
    for vanz in carti:
        if get_tip_reducere_client(vanz)  == 'silver':
            vanz_noua = creeaza_carte( get_id(vanz),
                                     get_titlu_carte(vanz),
                                     get_gen_carte(vanz),
                                     get_pret(vanz)-get_pret(vanz)*0.05,
                                     get_tip_reducere_client(vanz),
                                   )
            new_lst.append(vanz_noua)
        elif get_tip_reducere_client(vanz) == 'gold':
            carte_noua = creeaza_carte(get_id(vanz),
                                     get_titlu_carte(vanz),
                                     get_gen_carte(vanz),
                                     get_pret(vanz)-get_pret(vanz)*0.1,
                                     get_tip_reducere_client(vanz),
                                    )
            new_lst.append(carte_noua)
        else:
            new_lst.append(vanz)

    undo_list.append(carti)
    redo_list.clear()
    return new_lst