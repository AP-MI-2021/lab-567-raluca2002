from Logic.crud import create
from Userinterface.console import handle_undo, handle_redo


def test_undo_si_redo():
    carti = []
    undo_list = []
    redo_list = []
    carti = create(carti, 1, 'poezii', 'romatic', 45, 'gold', undo_list, redo_list)
    assert len(carti) == 1
    carti = create(carti, 2, 'Enigma Otiliei', 'realist', 55, 'silver', undo_list, redo_list)
    assert len(carti) == 2
    carti = create(carti, 3, 'Harap-Alb', 'basm', 34, 'gold', undo_list, redo_list)
    assert len(carti) == 3
    carti = handle_undo(carti, undo_list, redo_list)
    assert  len(carti) == 2
    carti = handle_undo(carti, undo_list, redo_list)
    assert len(carti) == 1
    carti = handle_undo(carti, undo_list, redo_list)
    assert len(carti) == 0
    carti = handle_undo(carti, undo_list, redo_list)
    assert  len(carti) == 0
    carti = create(carti,  1, 'poezii', 'romatic', 45, 'gold', undo_list, redo_list)
    carti = create(carti, 2, 'Enigma Otiliei', 'realist', 55, 'silver', undo_list, redo_list)
    carti = create(carti, 3, 'Harap-Alb', 'basm', 34, 'gold', undo_list, redo_list)
    assert len(carti) == 3
    carti = handle_redo(carti, undo_list, redo_list)
    assert len(carti) == 3
    carti = handle_undo(carti, undo_list, redo_list)
    assert len(carti) == 2
    carti = handle_undo(carti, undo_list, redo_list)
    assert len(carti) == 1
    carti = handle_redo(carti, undo_list, redo_list)
    assert len(carti) == 2
    carti = handle_redo(carti, undo_list, redo_list)
    assert len(carti) == 3
    carti = handle_undo(carti, undo_list, redo_list)
    assert len(carti) == 2
    carti = handle_undo(carti, undo_list, redo_list)
    assert len(carti) == 1
    carti = create(carti, 4, 'Moara cu noroc', 'Roman', 20, 'gold', undo_list, redo_list)
    assert len(carti) == 2
    carti = handle_redo(carti, undo_list, redo_list)
    assert len(carti) == 2
    carti = handle_undo(carti, undo_list, redo_list)
    assert len(carti) == 1
    carti = handle_undo(carti, undo_list, redo_list)
    assert len(carti) == 0
    carti = handle_redo(carti, undo_list, redo_list)
    assert len(carti) == 1
    carti = handle_redo(carti, undo_list, redo_list)
    assert len(carti) == 2
    carti = handle_redo(carti, undo_list, redo_list)
    assert len(carti) == 2