from src import db
from src.model import Admin, Viewer, Chat_message, Redemption


def add_admin(admin):
    new_admin = Admin(username=admin["username"], password=admin["password"])
    db.session.add(new_admin)
    db.session.flush()
    try:
        db.session.commit()
        return True
    except:
        return False

def check_admin(admin):
    try:
        admin = Admin.query.filter_by(username=admin["username"]).one()
        return True
    except:
        return False

def get_viewer_messages(viewer_id):
    messages = Chat_message.query.filter_by(viewer_id = viewer_id).all()

    return [
        {
            "id": message.id,
            "content": message.content,
            "datetime": message.datetime,
            "hipster-points": message.hipster_points,
            "fulfilled": message.fulfilled,
        }

        for message in messages
    ]

def get_viewer_redemptions(viewer_id):
    redemptions = Redemption.query.filter_by(viewer_id = viewer_id).all()

    return [
        {
            "id": redemption.id,
            "content": redemption.redemption,
            "datetime": redemption.datetime
        }

        for redemption in redemptions
    ]

def get_viewer_id(name):
    try:
        viewer = Viewer.query.filter_by(twitch_name = name).one()
        return {"viewer_id": viewer.id}
    except:
        return {"viewer_id": None}
