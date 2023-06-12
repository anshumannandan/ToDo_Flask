from . models import TaskModel
from . import ma

class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TaskModel