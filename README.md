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
Write tests and implement the following feature.
Assert that the script allows for an argument that provides a transcript file or a string of data.
Assert that the script counts the frequency of each word from the data received.
Assert that the output of the script displays the word frequencies using a number (example: hello (2)).
Assert that only words with count > 3 are counted.
```

Implement the feature.
```
Generate a sample transcript.txt file that contains a transcript of the benefits of TDD for python code and has at a minimum 5000 words.
Ensure the script passes the test case by passing the transcript.txt file as an argument with the command `uv run main`
```

```
# Generate 2 transcript files
Create a transcript.txt file with a Sample Transcript of a single person explaining how to use the tool aider.  The transccript should be about 3000 words long with valid sentences but no paragraphs.
```

```
Change the printed output to Word frequency count:
```

```
Update main to read ./transcript.txt to a variable.
```

```
count the frequency of each word using a dict to store counts
```

```
display the word frequencies by printing # for each count
```

```
remove the hello world print
```

```
only show words with count > 3 use a variable. after word before # show the total for the word.
```

```
update main to accept a cli arg transcript_file or alternately a string with the data.
```

