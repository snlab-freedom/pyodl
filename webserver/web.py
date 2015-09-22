from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.phtml", name = "Beraldo")

@app.route('/node/<node_id>')
def node(node_id):
    return "Hello node %s" % node_id

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
