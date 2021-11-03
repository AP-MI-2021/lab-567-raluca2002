def creeaza_carte(id_carte: int,tiltu_carte,gen_carte,pret,tip_reducere_client ):
    """
    Creeaza o vanzare pentru carte
    :param id_carte: Id ul cartii
    :param tiltu_carte: Titlul cartii
    :param gen_carte: Genul cartii
    :param pret: Pretul cartii
    :param tip_reducere_client: Tip reducere client(none,silver,gold)
    :return: O vanzare
    """

    return {
        'id': id_carte,
        'titlu': tiltu_carte,
        'gen': gen_carte,
        'pret': pret,
        'reducere':  tip_reducere_client,
    }


def get_id(carte):
    """
    Getter pentru id ul librariei
    :param vanzare: cartea
    :return: id ul librariei
    """
    return carte['id']

def get_titlu_carte(carte):
    '''
    TO DO
    :param librarie:
    :return:
    '''
    return carte['titlu']

def get_gen_carte(carte):
    '''
    TO DO
    :param librarie:
    :return:
    '''
    return carte['gen']

def get_pret(carte):
    '''
    TO DO
    :param librarie:
    :return:
    '''
    return carte['pret']

def get_tip_reducere_client(carte):
    '''
    TO DO
    :param librarie:
    :return:
    '''
    return carte['reducere']

def get_str(carte):
    return "Id: {}, titlul: {}, gen: {}, pret: {}, reducere: {}".format(
        get_id(carte),
        get_titlu_carte(carte),
        get_gen_carte(carte),
        get_pret(carte),
        get_tip_reducere_client(carte)
    )