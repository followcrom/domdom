import sqlalchemy

from sqlalchemy import create_engine, text

import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                    connect_args={ # extra arguments required to connect to PlanetScale db
                        "ssl": {
                            "ssl_ca": "/etc/ssl/cert.pem"
                        }
                    })

def load_domdoms_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from domdoms")) # any sql query
        domdoms = []
        for row in result.all():
            domdoms.append(dict(row))
        return domdoms


def load_domdom_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(
        text("select * from domdoms where id = :val"), # sqlalchemy formatting for creating a variable
        val = id
        )
        rows = result.all()
        if len(rows) == 0: # check to see if the db row exsists
            return None
        else:
            return dict(rows[0]) # if so, return as dictionary



def add_to_db(data):
    with engine.connect() as conn:
        query = text("INSERT INTO domdoms (title, date_created, quote, attribution) VALUES (:title, :date, :quote, :attribution)")
        conn.execute(query,
        title=data['title'],
        quote=data['quote'],
        attribution=data['attribution'],
        date=data['date']
        )
