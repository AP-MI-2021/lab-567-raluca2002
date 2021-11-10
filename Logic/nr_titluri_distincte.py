from Domain.librarie import get_gen_carte, get_titlu_carte

def nr_titluri_gen(gen, carti):
    lst_titluri = []
    for carte in carti:
        if get_gen_carte(carte) == gen:
            lst_titluri.append(get_titlu_carte(carte))
    set_lst_titluri = set(lst_titluri)
    lista_fara_duplicare =list(set_lst_titluri)
    return len(lista_fara_duplicare)


def nr_titluri_distincte(carti):
    '''
    Afisarea numarului de titluri distincte pentru fiecare gen
    :param carti: lista titlurilor
    :return: numarul de titluri distincte pentru fiecare gen
    '''
    rez = {}
    for carte in carti:
        gen = get_gen_carte(carte)
        if gen not in rez:
            rez[gen] = nr_titluri_gen(gen, carti)

    return rez