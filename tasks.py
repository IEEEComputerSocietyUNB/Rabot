import os
import webbrowser

from invoke import task


@task()
def train_nlu(c):
    c.run(
        'python3 -m rasa_nlu.train -c nlu_config.yml '
        '--fixed_model_name current --data data/intents/ -o models --project nlu --verbose')


@task()
def train_core(c):
    c.run('python3 train.py')


@task()
def train(c):
    c.run('train-nlu train-core')


@task
def test(c, vv=False):
    """ NOT TESTED: Runs all tests """
    pass


@task
def style(c):
    """ NOT TESTED: Checks if your code is well formatted for this project """
    c.run('pycodestyle bot/. tests/. --ignore=E402,W504')


@task
def doc(c):
    """ NOT TESTED: Checks if your code is well documented """
    c.run('make --directory docs/ html')
    webbrowser.open('file://' + os.path.realpath('docs/_build/html/index.html'))
    c.run('pydocstyle bot/. tests/.')


@task()
def run(c):
    """ Runs bot """
    c.run('python3 -m rasa_core.run -d models/dialogue -u models/nlu/current --debug --endpoints endpoints.yml')


@task()
def travis(c):
    """ NOT TESTED: Runs the tests checked by Travis """
    pass


@task
def install(c):
    """ Installs the requirements necessary for this project """
    c.run('pip3 install -r bot.requirements.txt')


@task
def cov(c):
    """ NOT TESTED: Checks how much of the program is covered by tests """
    pass


@task
def lint(c):
    """ NOT TESTED: Checks yaml file structure """
    c.run('yamllint bot')
