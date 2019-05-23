from flask import Flask, request
app = Flask(__name__)

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

# http://nowthatsnifty.blogspot.com/2010/05/list-of-prank-names.html :)
names = ["Al Gore-Rhythm", "Amy Stake", "Cal Culator"]


@app.route("/", methods=["GET"])
def get_names():
    return page % ", ".join(names)


@app.route('/', methods=["POST"])
def add_name():
    new_name = request.form["name"].strip()
    if new_name:
        names.append(new_name)

    return page % ", ".join(names)

app.run(port=3000)
