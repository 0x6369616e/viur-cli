import click
from .cli import cli

@cli.group(help='Develop the gcloud projects')
def project():
    pass


@project.command(name="add", help="Add a new gcloud project to the config.")
def project_add():
    pass


@project.command(name="remove", help="Remove a new gcloud project from the config.")
def project_remove():
    pass


@project.command(name="list", help="Display all registered gcloud projects.")
def project_list():
    pass


cli.add_command(project)

__all__ = ['project']
