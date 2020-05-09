import os

from invoke import task

# Parameterizing tasks with invoke
# https://docs.pyinvoke.org/en/0.11.1/getting_started.html#parameterizing-tasks


@task
def t(c):
    """
    Train Rasa bot
    """
    c.run(f"rasa train", pty=True)


@task
def s(c):
    """
    Rasa shell
    """
    c.run(f"rasa shell", pty=True)


@task
def sh(c):
    """
    Rasa shell and server
    """
    c.run(f"rasa run actions & rasa shell", pty=True)


@task
def sv(c):
    """ Start Rasa server """
    c.run(f"rasa run actions", pty=True)


@task
def stop(c):
    """
    Stop Rasa server
    """
    c.run("pkill -f rasa", pty=True)
    print("Rasa server stopped.")



@task
def dm(c):
    """
    Remove all models on models folder
    """
    c.run("rm -f models/*", pty=True)
    print("All model files removed.")

@task
def dt(c):
    """
    Remove all models on models folder and retrain
    """
    c.run("rm -f models/*", pty=True)
    print("All model files removed.")
    t(c)
