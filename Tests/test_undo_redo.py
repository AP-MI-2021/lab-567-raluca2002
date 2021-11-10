from Domain.librarie import creeaza_carte
from Logic.crud import create
from Logic.undo_redo import do_undo, do_redo


def get_data():
    return [
        creeaza_carte(1, 'v1', 'gen1', 60, 'silver'),
        creeaza_carte(2, 'v2', 'gen2', 20, 'none'),
        creeaza_carte(3, 'v3', 'gen3', 12, 'gold'),
        creeaza_carte(4, 'v4', 'gen4', 34, 'silver'),
    ]


def test_undo_redo():
    carti = get_data()
    undo_lst = []
    redo_lst = []
    v_new = create(carti, 5, 'vnew', 'gen new', 27, 'gold', undo_lst, redo_lst)
    v_new = do_undo(undo_lst, redo_lst, v_new)
    assert len(v_new) == len(carti)
    v_new = do_undo(undo_lst, redo_lst, v_new)
    assert v_new == None
    v_new = do_redo(undo_lst, redo_lst, v_new)
    assert len(v_new) == len(carti) + 1