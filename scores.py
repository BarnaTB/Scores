import click
from models import User

users = []


@click.command()
@click.option('--username', prompt="your username")
@click.option('--email', prompt="your email", help='Enter your email')
@click.option('--password', prompt="your password", help='Enter your password')
def cli(username, email, password):
    user = User(username, email, password)
    user.register_user()
    click.echo(username)
    click.echo(password)
    click.echo(email)
    click.echo(users)

