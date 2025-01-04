from src.tdd_project.main import main
from io import StringIO
import sys

def test_true_is_true():
     assert True is True

def test_main_function(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, Big World!\n"
