import sqlalchemy

from sqlalchemy import create_engine, text

import random

db_connection_string = 'mysql+pymysql://ms6jfg2xcfyx:pscale_pw_QmnAiq_CC7aQPsH--HIXD8H3CPGGJ7nb2xWwJMBVsjk@a2akbakyduhe.eu-west-2.psdb.cloud/joviancareers?charset=utf8mb4'

engine = create_engine(db_connection_string,
                    connect_args={ # extra arguments required to connect to PlanetScale db
                        "ssl": {
                            "ssl_ca": "/etc/ssl/cert.pem"
                        }
                    })

def load_domdoms_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from domdoms")) # any sql query
        domdoms_lst = []
        for row in result.all():
            domdoms_lst.append(dict(row))
        return domdoms_lst


def load_domdom_from_db(dom_id):
    numdoms = len(load_domdoms_from_db())
    with engine.connect() as conn:
        result = conn.execute(
        text("select * from domdoms where id = :val"),
        val=dom_id
        )
        rows = result.all()
        return dict(rows[0])



def add_to_db(data):
    with engine.connect() as conn:
        query = text("INSERT INTO domdoms (title, date_created, quote, attribution) VALUES (:title, :date, :quote, :attribution)")
        conn.execute(query,
        title=data['title'],
        quote=data['quote'],
        attribution=data['attribution'],
        date=data['date']
        )
