import os
import webbrowser

from invoke import task


@task
def test(c, vv=False):
    """ NOT TESTED: Runs all tests """
    detail = ""
    if vv:
        detail = '-vv'
    c.run(f'green3 {first_test}')
    c.run(f'green3 {app_test} {comm_test} {linter_test} {config_test} {detail}')


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
    style(c)
    lint(c)
    test(c)
    cov(c)


@task
def install(c):
    """ Installs the requirements necessary for this project """
    c.run('pip3 install -r bot.requirements.txt')


@task
def cov(c):
    """ NOT TESTED: Checks how much of the program is covered by tests """
    c.run(f'coverage run -m py.test\
          {app_test} {comm_test} {linter_test} {config_test}')
    c.run(f'coverage report -m {app} {comm} {linter} {config}')
    c.run(f'coverage html {app} {comm} {linter} {config}')


@task
def lint(c):
    """ NOT TESTED: Checks yaml file structure """
    c.run('yamllint bot')
