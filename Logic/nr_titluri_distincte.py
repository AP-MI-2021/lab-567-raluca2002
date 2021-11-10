from Domain.librarie import get_gen_carte, get_titlu_carte


def nr_titluri_distincte(carti):
    '''
    Afisarea numarului de titluri distincte pentru fiecare gen
    :param carti: lista titlurilor
    :return: numarul de titluri distincte pentru fiecare gen
    '''
    rez = {}
    lst_carti = []
    for carte in carti:
        gen = get_gen_carte(carte)
        titlu = get_titlu_carte(carte)
        if gen in rez:
            if titlu not in lst_carti:
                lst_carti.append(titlu)
                rez[gen] = rez[gen] + 1
        else:
            rez[gen] = 1
            lst_carti.append(titlu)
    return rez