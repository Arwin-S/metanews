# https://flask.palletsprojects.com/en/3.0.x/quickstart/
# flask --app hello run (source venv first)

from flask import Flask
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)


# Configure the PostgreSQL connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@localhost:6543/test_db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
@app.get("/")
def index():
    return "<p>Index Page</p>"

@app.get("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

class DummyTable(db.Model):
    __tablename__ = 'dummy_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)

@app.get("/db_conn")
def db_connect():
    try:
        results = DummyTable.query.order_by(DummyTable.id.asc()).all()
        
        # Convert the results to a list of dictionaries
        results_list = [{"id": result.id, "name": result.name, "age": result.age} for result in results]
        
        return jsonify(results_list), 200

        # db.session.query(text("1")).from_statement(text("SELECT 1")).all()
        # return jsonify({"message": "Connection successful!"}), 200
    
    except Exception as e:
        return jsonify({"message": "Connection failed!", "error": str(e)}), 500