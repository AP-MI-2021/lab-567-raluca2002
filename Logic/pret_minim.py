from Domain.librarie import get_gen_carte, get_pret


def pret_minim(carti):
    '''
    Sa se determine pretul minim pentru fiecare gen
    :param carti: lista de carti
    :return: pretul minim pentru fiecare gen
    '''
    rez = {}
    for vanz in carti:
        gen = get_gen_carte(vanz)
        pret_minim = get_pret(vanz)
        if gen in rez:
            if pret_minim < rez[gen]:
                rez[gen] = pret_minim
        else:
            rez[gen] = pret_minim
    return rez
