# cs101

CS 101: Introduction to Computer Science --- Python

The course can be found [here](http://modsurski.com/csci161)

Your typical CS101 class covering:

- Types
- Variables
- I/O
- Functions
- Conditionals
- Loops
- Objects
- Linear collection (List)

# Setup

## Windows

Have administrative privileges and run from cmd

```sh
python -m venv --clear --prompt cs101 venv
venv\Scripts\activate.bat
pip install -e .
```

## Bash

```sh
python3.11 -m venv --clear --prompt cs101 venv
. venv/bin/activate
pip install -e .
```

# Formatter

```sh
format # just type this
```

# Unit Tests

```sh
python -m unittest # May need python3
```

# Build

```sh
sphinx-build -b html "$SOURCEDIR" "$OUTPUTDIR"
```

# Contribute

Check out the [CONTRIBUTING](CONTRIBUTING.md) guidelines.
