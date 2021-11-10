from Domain.librarie import get_pret


def ordoneaza_crescator(carti):
    '''
    Ordoneaza vanzarile crescator dupa pret
    :param carti: lista vanzarilor
    :return: lista vanzarilor ordonate crescator dupa pret
    '''
    lst_carti = sorted(carti, key=lambda i: get_pret(i))
    return lst_carti