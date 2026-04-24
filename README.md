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
python3 -m venv --clear --prompt cs101 venv
. venv/bin/activate
pip install -e .
```

# Formatter

Automatically format Python and Markdown files.

```sh
format # just type this
```

# Verifier

Checks for code style, RST issues, and spelling errors.

```sh
verify # just type this
```

# Link Checker

Checks all URLs in the site for broken or redirected links.

```sh
links # just type this
```

# Unit Tests

Runs the project unit tests.

```sh
python -m unittest # May need python3
```

# Build

Builds the course website to `out/`.

```sh
site # just type this
```

Alternatively, use sphinx's `sphinx-build` to specify the built type and the source and output directories.

```sh
sphinx-build -b html "$SOURCEDIR" "$OUTPUTDIR"
```

# Contribute

Check out the [CONTRIBUTING](CONTRIBUTING.md) guidelines.
