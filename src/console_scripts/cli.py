import subprocess


def run_formatters():
    for tool in ["isort .", "black .", "mdformat ."]:
        print(f"running `{tool}`")
        subprocess.run(tool, shell=True)


def run_verification():
    for tool in ["flake8 src/ test/", "sphinx-lint site/", "codespell site/ src/ test/"]:
        print(f"running `{tool}`")
        subprocess.run(tool, shell=True)


def run_linkcheck():
    tool = "sphinx-build -b linkcheck site/ out/"
    print(f"running `{tool}`")
    subprocess.run(tool, shell=True)

def run_unittest():
    tool = "python -m unittest"
    print(f"running `{tool}`")
    subprocess.run(tool, shell=True)

def run_sphinx_build():
    tool = "sphinx-build -b html site/ out/"
    print(f"running `{tool}`")
    subprocess.run(tool, shell=True)
