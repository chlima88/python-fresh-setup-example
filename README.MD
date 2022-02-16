# What is this?

This repository contains my basic setup for python development environment under Windows

## Fresh instalation

```
git init -q
python -m venv venv
source ./venv/Scripts/activate
pip install pylint
pip3 install black
pip3 install flake8
pip3 install pytest
pip3 install pre-commit
pip3 freeze > requirements.txt
pylint --generate-rcfile > .pylintrc
touch .flake8
touch .editorconfig
touch .pre-commit-config.yaml
```

## `.editorconfig` setup

```
[*]
indent_style = space
indent_size = 4
end_of_line = crlf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true
```


## `.pylint` setup

The following command will generate a `.pylintrc` file. Use him to configure the lint options.
```
pylint --generate-rcfile > .pylintrc
```

Edit `.pylintrc` and perform the following changes:


- Add these lines:

```
disable=
    C0114 # missing-module-docstring
```

- Change this line

```
max-line-length=120
```


## `.flake8` setup

Create a .flake8 file, edit it like bellow.

```
[flake8]
ignore = E722, W503
max-line-lenght = 120
per-file-ignore =
    __init__.py: F401
```

## `pre-commit` setup

```
pip install pre-commit
pre-commit install
```
Create a `.pre-commit-conig.yaml` files and paste the content bellow.

Warning: the last hook is configured to my environment. You should change it as needed.

```
repos:
-   repo: https://github.com/ambv/black
    rev: stable
    hooks:
    - id: black
      language_version: python3.9
      stages: [commit]
-   repo: https://gitlab.com/pycqa/flake8
    rev: 3.7.9
    hooks:
    - id: flake8
      stages: [commit]
-   repo: local
    hooks:
    - id: pytest
      name: pytest
      language: system
      entry: pytest -v
      always_run: true
      pass_filenames: false
      stages: [commit]
-   repo: local
    hooks:
      - id: requirements
        name: requirements
        entry: bash -c 'venv/Scripts/pip3 freeze > requirements.txt; git add requirements.txt'
        language: system
        pass_filenames: false
        stages: [commit]

```
