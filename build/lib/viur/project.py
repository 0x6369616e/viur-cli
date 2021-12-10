import click

from .cli import cli


@cli.group(help='Develop the gcloud projects')
def project():
    click.echo("Na")


@project.command(name="add", help="Add a new gcloud project to the config.")
def _add():
    pass


@project.command(name="remove", help="Remove a new gcloud project from the config.")
def _remove():
    pass


@project.command(name="list", help="Display all registered gcloud projects.")
def _list():
    pass


cli.add_command(project)
