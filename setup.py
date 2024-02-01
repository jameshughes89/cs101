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
        python_requires=">=3.11",
        packages=find_packages(),
        install_requires=[
            "black[jupyter]==23.12.1",
            "flake8==7.0.0",
            "flake8-black==0.3.6",
            "flake8-isort==6.1.1",
            "isort==5.13.2",
            "mdformat==0.7.17",
            "mdformat-gfm==0.3.5",
            "mdformat-black==0.1.1",
            "sphinx==7.2.6",
            "sphinx-rtd-theme==2.0.0",
        ],
        entry_points={
            "console_scripts": [
                f"format = setup:{run_code_formatters.__name__}",
                f"validate = setup:{run_code_verification.__name__}",
                f"site = setup:{run_sphinx_build.__name__}",
            ]
        },
    )
