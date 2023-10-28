from flask_sqlalchemy import SQLAlchemy
from pynytimes import NYTAPI

db = SQLAlchemy()

# nytimes api
api_key = ""
nyt = NYTAPI(api_key, parse_dates=True)


class ArticlesTable(db.Model):

    __tablename__ = "articles_table"

    id = db.Column(db.Integer, primary_key=True)
    publisher = db.Column(db.String)
    title = db.Column(db.String)
    abstract = db.Column(db.String)
    byline = db.Column(db.String)
    url = db.Column(db.String)
    # media = db.Column(db.String) #list of image urls
    # rank - what rank the story was
    published_date = db.Column(db.DateTime(timezone=True))

    @classmethod
    def save_top_articles(cls):
        top_stories = nyt.top_stories()
        for i, top_story in enumerate(top_stories):
        
            # top_story has "title", "publisher", etc. key-value pairs in it

            new_article = ArticlesTable(
                publisher="nytimes",
                title=top_story.get("title"),
                abstract=top_story.get("abstract"),
                byline=top_story.get("byline"),
                url=top_story.get("url"),
                # media=article_data.get("media"),  # Uncomment this if you include the media column
                # rank - what rank the story was
                published_date=top_story.get("published_date")
            )

            try:
                db.session.add(new_article)
            except Exception as e:
                db.session.rollback()
                return f"An error occurred: {str(e)}"

        db.session.commit()

        return "Succesful"

    @classmethod
    def get_top(cls, n=100):
        try:
            # Order by published_date descending and limit to top n
            articles = cls.query.order_by(cls.published_date.desc()).limit(n).all()
            return articles
        except Exception as e:
            return f"An error occurred: {str(e)}"


class DummyTable(db.Model):
    __tablename__ = "dummy_table"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
