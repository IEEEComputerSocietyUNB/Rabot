from invoke import task


@task
def travis(c):
    """ Runs all tests on Travis CI """
    style(c)
    c.run('coverage run arquivo.py test -v')
    # lint(c)


@task
def style(c):
    """ Checks if your code is well formatted for this project """
    c.run('pycodestyle bot scripts --ignore=E402,E501,W504')


@task()
def run_cli(c):
    """ Runs bot """
    c.run('python3 -m rasa_core.run -d models/dialogue -u models/nlu/current --debug --endpoints endpoints.yml')


@task()
def run_telegram(c):
    """"Runs bot on telegram. Requires a credentials.yaml to work"""
    c.run("python3 -m rasa_core.run -d models/dialogue -u models/nlu/current --port 5002 --credentials credentials.yml")


@task
def install(c):
    """ Installs the requirements necessary for this project """
    c.run('pip3 install -r bot.requirements.txt')


@task
def lint(c):
    """ NOT TESTED: Checks yaml file structure """
    c.run('yamllint bot scripts')
