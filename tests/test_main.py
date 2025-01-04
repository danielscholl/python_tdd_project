from src.tdd_project.main import main

def test_main_function(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, Cruel World!\n"
