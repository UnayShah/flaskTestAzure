from os import environ

import flask
from psycopg2.pool import SimpleConnectionPool

app = flask.Flask(__name__)

pool = SimpleConnectionPool(1, 3, database=environ['POSTGRES_DATABASE'],
                            host=environ['POSTGRES_DATABASE_HOST'],
                            user=environ['POSTGRES_DATABASE_USER'],
                            password=environ['POSTGRES_DATABASE_PASSWORD'],
                            port=environ['POSTGRES_DATABASE_PORT'])


@app.route('/', methods=['GET'])
def index():
    return 'New build for testing 1'


@app.route('/db', methods=['GET'])
def db():
    conn = pool.getconn()
    cur = conn.cursor()
    cur.execute('SELECT 1')
    result = cur.fetchone()
    pool.putconn(conn)
    return str(result)


if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0')
    except Exception:
        pass
