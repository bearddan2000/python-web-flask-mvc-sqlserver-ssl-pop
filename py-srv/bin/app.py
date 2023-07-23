from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(
    __name__,
    instance_relative_config=False,
    template_folder="templates"
)
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pymssql://sa:z!x<?oB1ab@db/master"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class PopModel(db.Model):
    __tablename__ = 'pop'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    color = db.Column(db.String())

    def __init__(self, name, color):
        self.name = name
        self.color = color

@app.route('/', methods=['GET'])
def hello():
    return render_template("index.html")

@app.route('/pop', methods=['GET'])
def handle_beverages():
    beverages = PopModel.query.all()
    results = [
        {
            "id": pop.id,
            "name": pop.name,
            "color": pop.color
        } for pop in beverages]

    return {"results": results}

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)
