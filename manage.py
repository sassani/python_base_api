# pylint: disable=unused-import, wrong-import-position, E0611
import click

from flask_migrate import Migrate

from src.application import create_app, create_settings
from src.database import DB

import src.database.user as user
import src.database.client as client
import src.database.login

APP_SETTINGS = create_settings()
APP = create_app(APP_SETTINGS)

migrates = Migrate(app=APP, db=DB)

@click.group()
def manage():
    pass

@click.command('seed')
def seed():
    click.echo('Seeding Database ...')
    APP.app_context().push()

    # delete all rows
    DB.session.query(user.User).delete()
    DB.session.query(client.Client).delete()

    # add seed data
    DB.session.add(user.seed(APP_SETTINGS))
    DB.session.add(client.seed())

    # save
    DB.session.commit()
    click.echo('Seeding Database done')

manage.add_command(seed)

if __name__ == '__main__':
    manage()
