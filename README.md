# Python Workspace

A beginner-focused collection of short Python examples and practice problems, organized by chapter. This repository is designed to help new learners explore core Python concepts (printing, variables, types, strings) through concise scripts and small exercises.

## Table of Contents
- [What you'll learn](#what-youll-learn)
- [Repository structure](#repository-structure)
- [Prerequisites](#prerequisites)
- [How to run examples](#how-to-run-examples)
- [Suggested workflows](#suggested-workflows)
- [Contributing](#contributing)
- [Planned improvements](#planned-improvements)
- [License](#license)
- [Author](#author)

## What you'll learn
- Basic input/output and commenting style
- Variable assignment and fundamental operators
- Built-in types and simple type operations
- Core string operations and escape sequences
- Hands-on practice via short, self-contained problems

## Repository structure
Top-level chapters group related examples and exercises:

```text
Chapter 1/        Intro-level examples (print, comments, variables)
  01_first.py
  02_Variables&Datatypes.py

Chapter 2/        Basic types, input, and practice problems
  01_type.py
  02_input.py
  Practice Problems/
    01.py
    02.py
    03.py
    04.py
    05.py
    06.py

Chapter 3/        Strings and string functions plus exercises
  01_IntroToStrings.py
  02_SkippingCharacters.py
  03_StrFunctions.py
  04_EscSeq.py
  Practice Problems/
    01.py
    02.py
    03.py
    04.py
    05.py
```

Each chapter contains short, runnable scripts that demonstrate a single topic. The "Practice Problems" folders contain small exercises you can run to reinforce learning.

## Prerequisites
- Python 3.8+ installed (3.10+ recommended)
- A command-line shell (bash, PowerShell, etc.)
- Optional: an editor such as VS Code, or Jupyter if you prefer notebooks

No external packages are required — all examples use the Python standard library and core language features.

## How to run examples
Run any example directly with the Python interpreter. Example commands:

- Run a chapter example:
```bash
python "Chapter 1/01_first.py"
python "Chapter 3/01_IntroToStrings.py"
```

- Run a practice problem:
```bash
python "Chapter 2/Practice Problems/01.py"
```

- Run all files in a chapter (simple bash loop):
```bash
# Unix-like shells
for f in Chapter\ 1/*.py; do python "$f"; done
```

Notes:
- Some scripts may prompt for input (see Chapter 2/02_input.py); run them interactively.
- Windows users may need to adapt quote/escape syntax for paths.

## Suggested workflows
- Learning path: work through Chapter 1 → Chapter 2 → Chapter 3, then attempt the practice problems in each chapter.
- Interactive exploration: open a chapter in a Jupyter notebook and paste/modify cells to experiment with behavior.
- Automated verification (recommended enhancement): convert practice problems into pytest tests and add a CI workflow to ensure solutions run as expected.

## Contributing
Contributions are welcome. Suggested contribution types:
- Improve examples for clarity and correctness
- Add unit tests for practice problems (pytest)
- Convert examples into Jupyter notebooks
- Add a CI workflow that runs linting and tests

If you'd like to contribute:
1. Fork the repository
2. Create a topic branch (e.g., feature/readme or feat/tests)
3. Open a pull request with a clear description of changes

## Planned improvements (ideas)
- Add a top-level README (this file) and commit it to the repo
- Add a `requirements.txt` or `pyproject.toml` only if external deps are needed in the future
- Add automated tests and a GitHub Actions workflow that runs them
- Provide a single "start here" notebook per chapter to support interactive learners

## License
This repository does not include an explicit license file. If you want to make the code reusable by others, consider adding an open-source license (MIT, Apache-2.0, etc.). Example: add a `LICENSE` file with the MIT license.

## Author
Repository: tasbeeh479/python-workspace  
Author: tasbeeh (tasbeeh479)

---
If you'd like, I can:
- Commit this README.md to the repository and open a pull request, or
- Convert the practice problems into pytest tests and add a CI workflow to run them automatically.
