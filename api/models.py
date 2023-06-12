from . import db
import enum
from sqlalchemy import Enum



class TaskStatus(enum.IntEnum):
    incomplete = 0
    in_progress = 1
    completed = 2


class TaskModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(2000))
    due_date = db.Column(db.DateTime)
    status = db.Column(Enum(TaskStatus), default=TaskStatus.incomplete)

    def __repr__(self):
        return self.title