import click
from models import User

users = []


@click.command()
@click.argument('username')
@click.option('--email', default='', help='Enter your email')
@click.option('--password', default='', help='Enter your password')
def cli():
    username = input("Enter username: ")
    password = input("Enter password: ")
    email = input("Enter email: ")
    user = User(username, email, password)
    user.register_user()
    click.echo(users)

