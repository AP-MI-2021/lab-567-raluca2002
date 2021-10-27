def creeaza_librarie(id_librarie: int,tiltu_carte,gen_carte,pret,tip_reducere_client ) :
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
        'id': id_librarie,
        'titlu': tiltu_carte,
        'gen': gen_carte,
        'pret': pret,
        'reducere':  tip_reducere_client,
    }


def get_id(librarie):
    """
    Getter pentru id ul prajiturii
    :param vanzare: cartea
    :return: id ul cartii
    """
    return librarie['id']

def get_titlu_carte(librarie):
    '''
    TO DO
    :param librarie:
    :return:
    '''
    return librarie['titlu']

def get_gen_carte(librarie):
    '''
    TO DO
    :param librarie:
    :return:
    '''
    return librarie['gen']

def get_pret(librarie):
    '''
    TO DO
    :param librarie:
    :return:
    '''
    return librarie['pret']

def get_tip_reducere_client(librarie):
    '''
    TO DO
    :param librarie:
    :return:
    '''
    return librarie['reducere']

def get_str(librarie):
    return f'Libraria cu id-ul {get_id(librarie)}, cu titlul {get_titlu_carte(librarie)}, genul {get_gen_carte(librarie)}, pretul {get_pret(librarie)} si tipul de reducere {get_tip_reducere_client(librarie)}'
