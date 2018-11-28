## Create Python project with Cookie Cutter

[back...](../../README.md)


## Installation 
Installing Cookiecutter
Follow the installation instructions (and setting of the PATH etc...) on the [cookiecutter tutorial](https://cookiecutter.readthedocs.io/en/latest/installation.html)

#### tl;dr (OSX)
```bash

brew install python3
export PATH=$HOME/.local/bin:$PATH
pip install --user cookiecutter

# Or, with brew
brew install cookiecutter
```


## Creating a base template

Follow instructions on creating your cookiecutter base template on the [cookiecutter tutorial page](https://cookiecutter.readthedocs.io/en/latest/usage.html)


## References

+ [Cookiecutter tutorial](https://cookiecutter.readthedocs.io/en/latest/installation.html)
+ https://github.com/Yelp/cookiecutter-boto-cli/blob/master/%7B%7Bcookiecutter.project_slug%7D%7D/Makefile


## Usage

```bash
cookiecutter <path to repo>/simple-python-template/
```

#### In the newly created project
```
virtualenv venv
source venv/bin/activate
make install
make clean-build
make test
```