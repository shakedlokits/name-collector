from flask import Flask, request
from sqlite3 import connect

app = Flask(__name__)

# Initialize db.
with connect("names.db") as connection:
    db = connection.cursor()
    db.execute('''create table if not exists names (name text)''')

page = """
<html>
    <body>
        <div>
            <p>Names: %s</p>
        </div>
        <form method="post" action="http://localhost:3000">
            Name: <input type="text" name="name"/>
            <input type="submit" value="Submit"/>
        </form>
    </body>
</html>
"""


@app.route("/", methods=["GET"])
def get_names():
    with connect("names.db") as connection:
        db = connection.cursor()

        names = [name[0] for name in list(db.execute("select name from names"))]
        return page % ", ".join(names)


@app.route('/', methods=["POST"])
def add_name():
    with connect("names.db") as connection:
        db = connection.cursor()
        new_name = request.form["name"].strip()

        if new_name:
            db.execute("insert into names values (\'%s\')" % new_name)
            connection.commit()

        names = [name[0] for name in list(db.execute("select name from names"))]
        return page % ", ".join(names)


app.run(port=3000)
