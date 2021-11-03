
def creeaza_carte(id_carte, tiltu_carte, gen_carte, pret, tip_reducere_client):

    return [str(id_carte), str(tiltu_carte), str(gen_carte), pret, str(tip_reducere_client)]


def get_id(carte):

    return carte[0]


def get_titlu_carte(carte):

    return carte[1]


def get_gen_carte(carte):

    return carte[2]


def get_pret(carte):

    return carte[3]


def get_tip_reducere_client(carte):

    return carte[4]


def get_str(carte):
    return "Id: {}, titlul: {}, gen: {}, pret: {}, reducere: {}".format(
        get_id(carte),
        get_titlu_carte(carte),
        get_gen_carte(carte),
        get_pret(carte),
        get_tip_reducere_client(carte)
    )
