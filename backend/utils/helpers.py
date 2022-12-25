import psycopg2
import datetime
import json
import re
from functools import partial


def connect_to_database():
    server = "localhost"
    database = "poggers"
    username = "postgres"
    cnxn = psycopg2.connect(
        user=username,
        password="root",
        host=server,
        database=database,
        port="5432"
    )
    return cnxn


def get_stop_words():
    f = open("data/stop_words.txt", "r", encoding="utf-8")
    stop_words = [i.strip() for i in f.readlines()]
    stop_words = "'" + "', '".join(stop_words) + "', ''"
    return stop_words


def get_min_year(chat_id):
    db = connect_to_database()
    c = db.cursor()
    c.execute(f"""
        SELECT min(extract(year from timestamp))
        FROM messenger_message
    """)
    try:
        year = c.fetchone()[0]
        return year
    except:
        return 2000


def get_curr_year():
    return datetime.datetime.now().year


def get_senders(min_date, max_date, chat_id, db):
    c = db.cursor()
    c.execute(f"""
        SELECT distinct sender
        FROM messenger_message
        WHERE timestamp >= '{min_date}' 
        AND timestamp <= '{max_date}'
        ORDER BY sender asc
    """)
    senders = [i[0] for i in c.fetchall()]
    senders.insert(0, "Allir")
    return senders


def get_id_from_name(name):
    db = connect_to_database()
    c = db.cursor()
    c.execute(f"""
        SELECT distinct id
        FROM messenger_chatidentifier
        WHERE chat_name like '%{name}%'
    """)
    chat_id = c.fetchone()
    if chat_id:
        return chat_id[0]
    return None


def fix_text(path):  # Fix encoded text to UTF-8 format
    try:
        fix_mojibake_escapes = partial(
            re.compile(rb'\\u00([\da-f]{2})').sub,
            lambda m: bytes.fromhex(m.group(1).decode()))
        with open(path, 'rb') as f:
            repaired = fix_mojibake_escapes(f.read())
        return json.loads(repaired.decode('utf8'))
    except:
        return {}
