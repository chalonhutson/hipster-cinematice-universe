from .model import Admin


def add_admin(admin):
    new_admin = Admin(username=admin["username"], password=admin["password"])
    db.session.add(new_admin)
    
    try:
        db.session.commit()
        return True
    except:
        return False