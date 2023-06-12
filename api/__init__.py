from app import db, ma, app
from . views import TaskLCView, TaskRUDView
from flask_restful import Api


api = Api(app)


api.add_resource(TaskLCView, "/task")
api.add_resource(TaskRUDView, "/task/<int:pk>")