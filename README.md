# Test Driven Development - Simple Transcript Analytics


## Setup

- Install dependencies: `uv sync`
- Start the Test watcher `uv run ptw .`
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