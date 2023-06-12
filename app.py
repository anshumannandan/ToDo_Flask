from flask import Flask
import os, dotenv, enum, datetime
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import Enum
from flask_restful import Api, Resource, reqparse



# application configuration
dotenv.load_dotenv()
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG', bool)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)
api = Api(app)
ma = Marshmallow(app)



# database models
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
    


# model serializer
class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TaskModel
    

# application views

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



# application endpoints
api.add_resource(TaskLCView, "/task")
api.add_resource(TaskRUDView, "/task/<int:pk>")



if __name__ == '__main__':
    app.run(debug=DEBUG)