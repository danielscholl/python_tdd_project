from src.tdd_project.main import main

def test_main_function(capsys):
    sample_data = "apple apple apple apple banana banana orange orange orange orange"
    main(transcript_content=sample_data)
    captured = capsys.readouterr()
    expected_output = (
        "Word frequency count:\n"
        "apple (4): ####\n"
        "orange (4): ####\n"
    )
    assert captured.out == expected_output
