# https://flask.palletsprojects.com/en/3.0.x/quickstart/
# flask --app hello run --debug (source venv first)

from flask import Flask
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

from models.postgre import db, DummyTable, ArticlesTable


app = Flask(__name__)

# Configure the PostgreSQL connection
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://root:root@localhost:6543/test_db"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://root:root@db:5432/test_db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.get("/")
def index():
    return "<p>Index_Page</p>"


@app.get("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


@app.get("/db_conn")
def db_test_connection():
    try:
        results = DummyTable.query.order_by(DummyTable.id.asc()).all()

        # Convert the results to a list of dictionaries
        results_list = [
            {"id": result.id, "name": result.name, "age": result.age}
            for result in results
        ]

        return jsonify(results_list), 200

        # db.session.query(text("1")).from_statement(text("SELECT 1")).all()
        # return jsonify({"message": "Connection successful!"}), 200

    except Exception as e:
        return jsonify({"message": "Connection failed!", "error": str(e)}), 500


@app.get("/nyt_fetch_top")
def db_insert_top():

    result = ArticlesTable.save_top_articles()
    return jsonify(result), 200

@app.get("/top")
def db_get_top():
    articles = ArticlesTable.get_top()

    # Convert articles to a list of dictionaries
    results_list = [
        {
            "id": article.id,
            "publisher": article.publisher,
            "title": article.title,
            "abstract": article.abstract,
            "byline": article.byline,
            "url": article.url,
            # "media": article.media,  # Uncomment this if you include the media column
            "published_date": article.published_date.isoformat() if article.published_date else None
        }
        for article in articles
    ]

    return jsonify(results_list), 200

# @app.cli.command("initdb")
# def initdb_command():
#     """Creates the database tables."""
#     with app.app_context():
#         db.create_all()
#     print('Initialized the database.')