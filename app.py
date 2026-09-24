import os
from flask import Flask
from flaskext.mysql import MySQL      # For newer versions of flask-mysql
# from flask.ext.mysql import MySQL   # For older versions of flask-mysql
app = Flask(__name__)

mysql = MySQL()

mysql_database_host = 'MYSQL_DATABASE_HOST' in os.environ and os.environ['MYSQL_DATABASE_HOST']

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'db_user'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Passw0rd'
app.config['MYSQL_DATABASE_DB'] = 'employee_db'
app.config['MYSQL_DATABASE_HOST'] = mysql_database_host
mysql.init_app(app)

conn = mysql.connect()

cursor = conn.cursor()

@app.route("/")
def main():
    return "Welcome!"

@app.route("/birthday-invitation")
def main():
return """
<div style="text-align:center; font-family:Arial; padding:50px;">
<h1>You're Invited!</h1>

    <h2>Birthday Eve Celebration</h2>

    <p>
        Come join us as we celebrate another year of
        <strong>fun, laughter and great memories!</strong>
    </p>

    <h3>26th September 08:00 PM IST</h3>

    <p>
        Get ready for an evening filled with good vibes,
        delicious food and unforgettable moments.
    </p>

    <h2>Let's Celebrate!</h2>

    <p>We'd love to have you there.</p>
</div>
"""

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

@app.route('/read from database')
def read():
    cursor.execute("SELECT * FROM employees")
    row = cursor.fetchone()
    result = []
    while row is not None:
      result.append(row[0])
      row = cursor.fetchone()

    return ",".join(result)

if __name__ == "__main__":
    app.run()
