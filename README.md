# Test Driven Development - Simple Transcript Analytics


## Setup

- Install dependencies: `uv sync`
- Test the application `uv run pytest`
- Run the script: `uv run main`

## Initial Python Code.

main.py
```
def main():
    print("Hello, Cruel World!")

if __name__ == "__main__":
    main()
```

test_main.py
```
from src.tdd_project.main import main

def test_main_function(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, Cruel World!\n"
```

## Enable TDD Watcher.

- Start the Test watcher `uv run ptw .`

## Prompts

Write the feature test.
```
Write tests for the following feature:
Assert that the script allows for an argument that provides a transcript file or a string of data.
Assert that the script counts the frequency of each word from the data received.
Assert that the output of the script displays the word frequencies using a number (example: hello (2)).
Assert that only words with count > 3 are counted.
```

Implement the feature.
```
Generate a sample transcript.txt file that contains a transcript of the benefits of TDD for python code and has at a minimum 5000 words.
Implement the code defined by the test cases then run the tests using the command `'uv run pytest'.
Fix the code.
The code should pass lint checks using ruff 'uv run ruff check {file}'
Ensure the script successfully runs by passing the transcript.txt file as an argument with the command `uv run main`
```