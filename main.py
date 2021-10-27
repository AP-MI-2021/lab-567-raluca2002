from Logic.crud import create
from Tests.test_crud import test_crud
from Userinterface.console import run_ui


def main():
    librarii = []
    librarii = create(librarii, 1,'poezii', 'romatic', 45, 'gold')
    librarii = run_ui(librarii)

if __name__=='__main__':
    test_crud()
    main()