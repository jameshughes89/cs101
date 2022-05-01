import subprocess

from setuptools import find_packages, setup


def run_code_formatters():
    for tool in ["isort .", "black .", "mdformat ."]:
        print(f"running `{tool}`")
        subprocess.run(tool, shell=True)


def run_code_verification():
    tool = "flake8 src/ test/"
    print(f"running `{tool}`")
    subprocess.run(tool, shell=True)


def run_sphinx_build():
    tool = "sphinx-build -b html site/ out/"
    print(f"running `{tool}`")
    subprocess.run(tool, shell=True)


if __name__ == "__main__":
    setup(
        name="cs101",
        version="1.0",
        url="https://github.com/jameshughes89/cs101",
        python_requires=">=3.10",
        packages=find_packages(),
        install_requires=[
            "black[jupyter]==22.3.0",
            "flake8==4.0.1",
            "flake8-black==0.3.2",
            "flake8-isort==4.1.1",
            "isort==5.10.1",
            "mdformat==0.7.14",
            "mdformat-gfm==0.3.5",
            "mdformat-black==0.1.1",
            "sphinx==4.5.0",
            "sphinx-rtd-theme==1.0.0",
        ],
        entry_points={
            "console_scripts": [
                f"format = setup:{run_code_formatters.__name__}",
                f"validate = setup:{run_code_verification.__name__}",
                f"site = setup:{run_sphinx_build.__name__}",
            ]
        },
    )
