from . models import TaskModel
from . schemas import TaskSchema
from . import db
from flask_restful import Resource, request


class TaskLCView(Resource):
    
    def get(self):
        tasks = TaskModel.query.all()
        return TaskSchema(many=True).dump(tasks)

    def post(self):
        data = request.get_json()
        try:
            task_data = TaskSchema().load(data)
        except Exception as error:
            return error.normalized_messages(), 400
        task = TaskModel(**task_data)
        db.session.add(task)
        db.session.commit()
        return TaskSchema().dump(task)


class TaskRUDView(Resource):

    def get(self, pk):
        task = TaskModel.query.filter_by(id=pk).first()
        return TaskSchema().dump(task)

    def patch(self, pk):
        task = TaskModel.query.filter_by(id=pk).first()
        if task:
            data = request.get_json()
            try:
                task_data = TaskSchema(partial=True).load(data)
            except Exception as error:
                return error.normalized_messages(), 400
            task.query.update(task_data)
            db.session.commit()
        return TaskSchema().dump(task)

    def delete(self, pk):
        task = TaskModel.query.filter_by(id=pk).first()
        if task:
            db.session.delete(task)
            db.session.commit()
        return TaskSchema().dump(task)