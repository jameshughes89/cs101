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
            "black[jupyter]==25.1.0",
            "flake8==7.1.2",
            "flake8-black==0.3.6",
            "flake8-isort==6.1.2",
            "isort==5.13.2",
            "mdformat==0.7.22",
            "mdformat-gfm==0.4.1",
            "mdformat-black==0.1.1",
            "sphinx==8.1.3",
            "sphinx-rtd-theme==3.0.2",
        ],
        entry_points={
            "console_scripts": [
                f"format = setup:{run_code_formatters.__name__}",
                f"validate = setup:{run_code_verification.__name__}",
                f"site = setup:{run_sphinx_build.__name__}",
            ]
        },
    )
