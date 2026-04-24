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

# Project CLI Scripts

| Command  | Description                                            |
|----------|--------------------------------------------------------|
| `format` | Automatically format Python and Markdown files         |
| `verify` | Check for code style, RST issues, and spelling errors  |
| `links`  | Check  URLs in the site for broken or redirected links |
| `site`   | Build the course website to `out/`                     |
----------------------------------------------------------------------

Alternatively, use `sphinx-build` directly to specify the build type and directories.

```sh
sphinx-build -b html "$SOURCEDIR" "$OUTPUTDIR"
```

# Unit Tests

Runs the project unit tests.

```sh
python -m unittest # May need python3
```

# Contribute

Check out the [CONTRIBUTING](CONTRIBUTING.md) guidelines.
