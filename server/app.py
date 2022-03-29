from src import app
from src.model import connect_to_db

if __name__ == "__main__":
    app.config["ENV"] = "development"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    connect_to_db(app)
    app.run(port=5000, debug=False)