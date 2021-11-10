
def creeaza_carte(id_carte, titlu_carte, gen_carte, pret, tip_reducere_client):
    '''
    Creeaza o lista ce reprezinta o vanzare
    :param id_carte: string
    :param tiltu_carte: string
    :param gen_carte: string
    :param pret: float
    :param tip_reducere_client: string
    :return: o lista ce contine o vanzare
    '''

    return [
        id_carte,
        titlu_carte,
        gen_carte,
        pret,
        tip_reducere_client,
        ]



def get_id(carte):
    '''
    Da id-ul unei vanzari:
    :param carte: lista ce contine o vanzare
    :return: id-ul vanzarii
    '''

    return carte[0]


def get_titlu_carte(carte):
    '''
    Da titlul cartii
    :param carte: lista ce contine o vanzare
    :return: titlul cartii
    '''

    return carte[1]


def get_gen_carte(carte):
    '''
    Da genul cartii
    :param carte: lista ce contine o vanzare
    :return: genul cartii
    '''

    return carte[2]


def get_pret(carte):
    '''
    Da pretul cartii
    :param carte: lista ce contine o vanzare
    :return: pretul cartii
    '''

    return carte[3]


def get_tip_reducere_client(carte):
    '''
    Da tipul reducerii clientului
    :param carte: lista ce contine o vanzare
    :return: tipul reducerii
    '''

    return carte[4]


def get_str(carte):
    return "Id: {}, titlul: {}, gen: {}, pret: {}, reducere: {}".format(
        get_id(carte),
        get_titlu_carte(carte),
        get_gen_carte(carte),
        get_pret(carte),
        get_tip_reducere_client(carte)
    )
