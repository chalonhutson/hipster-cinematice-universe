from werkzeug.security import check_password_hash
from src import db
from src.model import Admin


def add_admin(admin):
    print(admin)
    new_admin = Admin(username=admin["username"], password=admin["password"])
    print(new_admin)
    db.session.add(new_admin)
    print("added")
    db.session.flush()
    try:
        db.session.commit()
        return True
    except:
        return False
