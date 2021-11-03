from Logic.crud import create
from Tests.test_crud import test_crud
from Tests.test_discount_reducere import test_discount_pt_reducere
from Userinterface.console import run_ui


def main():
    carti = []
    carti = create(carti, 1, 'poezii', 'romatic', 45, 'gold')
    run_ui(carti)


if __name__ == '__main__':
    test_crud()
    main()
