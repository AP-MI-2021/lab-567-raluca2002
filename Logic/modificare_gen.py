from Domain.carte import get_titlu_carte, creeaza_carte, get_id, get_pret, get_tip_reducere_client


def modifica_gen_carte(carti, titlu, gen_carte):
    '''
    Modifica genul cartii pentru un titlu dat
    :param gen_carte: string
    :param titlu: string
    :param carti: lista cartilor
    :return: genul modificat al cartii
    '''
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
    return new_lst