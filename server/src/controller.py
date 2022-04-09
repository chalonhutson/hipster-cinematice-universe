from werkzeug.security import check_password_hash
from src import db
from src.model import Admin, Viewer, Chat_message


def add_admin(admin):
    new_admin = Admin(username=admin["username"], password=admin["password"])
    db.session.add(new_admin)
    db.session.flush()
    try:
        db.session.commit()
        return True
    except:
        return False

def get_viewer_messages(viewer_id):
    messages = Chat_message.query.filter_by(viewer_id = viewer_id).all()

    return [
        {
            "message_id": message.id,
            "message_content": message.message_content,
            "message_datetime": message.message_datetime
        }

        for message in messages
    ]
