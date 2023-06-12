from . models import TaskModel
from . schemas import TaskSchema
from . import db
import datetime
from flask_restful import Resource, reqparse


def non_empty_string(s):
    if not s:
        raise ValueError('String must be non empty')
    return s


class TaskLCView(Resource):
    
    def get(self):
        tasks = TaskModel.query.all()
        return TaskSchema(many=True).dump(tasks)

    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True, trim=True)
        parser.add_argument('title', type=non_empty_string, required=True, nullable=False)
        parser.add_argument('description', type=non_empty_string, required=True, nullable=False)
        parser.add_argument('due_date', type=datetime.datetime.fromisoformat, required=True, nullable=False)
        parser.add_argument('status', type=int, choices=[0,1,2])
        args = parser.parse_args()
        task = TaskModel(title = args['title'],
                         description = args['description'],
                         due_date = args['due_date'],
                         status = args['status'])
        db.session.add(task)
        db.session.commit()
        return TaskSchema().dump(task)


class TaskRUDView(Resource):

    def get(self, pk):
        task = TaskModel.query.filter_by(id=pk).first()
        return TaskSchema().dump(task)

    def put(self, pk):
        task = TaskModel.query.filter_by(id=pk).first()
        if task:
            parser = reqparse.RequestParser(bundle_errors=True, trim=True)
            parser.add_argument('title', type=non_empty_string)
            parser.add_argument('description', type=non_empty_string)
            parser.add_argument('due_date', type=datetime.datetime.fromisoformat)
            parser.add_argument('status', type=int, choices=[0,1,2])
            args = parser.parse_args()
            if args['title']:
                task.title = args['title'] 
            if args['description']:
                task.description = args['description']
            if args['due_date']:
                task.due_date = args['due_date']
            if args['status'] or args['status']==0:
                task.status = args['status']
            db.session.commit()
        return TaskSchema().dump(task)

    def delete(self, pk):
        task = TaskModel.query.filter_by(id=pk).first()
        if task:
            db.session.delete(task)
            db.session.commit()
        return TaskSchema().dump(task)