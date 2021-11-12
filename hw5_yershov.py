# Создать VIEW функцию, которая выводит количество записей в таблице `Tracks`.
#
# def get_tracks_count() -> '/tracks_count'
# Можно решить задачу средствами Python, а можно и через SQL если воспользоваться агрегирующей функцией `count()`

from flask import Flask
from db import execute_query

app = Flask(__name__)


@app.route('/tracks_count')
def get_tracks_count():
    sql = 'select * from Tracks'

    records = execute_query(sql)

    return f'<p>There are {len(records)} records in Tracks.</p>'


@app.route('/tracks_count_sql')
def get_tracks_count_sql():
    sql = 'select count(*) from Tracks'

    records = execute_query(sql)

    return f'<p>There are {records[0][0]} records in Tracks.</p>'


app.run(debug=True)
