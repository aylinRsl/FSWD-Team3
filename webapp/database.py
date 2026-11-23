import os
import sqlite3
import click
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
        current_app.config['DATABASE'],
        detect_types= sqlite3.PARSE_DECLTYPES
    )
        g.db.row_factory = sqlite3.Row
        g.db.execute('Pragma foreign_keys = ON;')
    return g.db

def close_db(e=None):
    db = g.pop('db' , None)
    if db is not None:
        db.close()

@click.command('init-db')
def init_db():
    try:
        os.makedirs(current_app.instance_path)
    except OSError:
        pass
    db = get_db()
    with current_app.open_resource('sql/drop_tables.sql') as f:
        db.executescript(f.read().decode('utf8'))
    with current_app.open_resource('sql/create_tables.sql') as f:
        db.executescript(f.read().decode('utf8'))
    click.echo('Database has been initialized.')

    with current_app.open_resource('sql/insert_base_data.sql') as f:
        db.executescript(f.read().decode('utf8'))