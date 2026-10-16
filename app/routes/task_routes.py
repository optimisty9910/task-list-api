from flask import Blueprint, request, Response
from .route_utilities import retrieve_model, create_model, get_models_with_filters
from ..models.task import Task
from ..db import db

bp = Blueprint('task', __name__, url_prefix='/tasks')

@bp.post("")
def create_task():
    request_body = request.get_json()
    return create_model(Task, request_body)

@bp.get("")
def get_all_tasks():    
    return get_models_with_filters(Task, request.args)

@bp.get("/<task_id>")
def get_one_task(task_id):
    return retrieve_model(Task, task_id).to_dict()

@bp.put("/<task_id>")
def update_task(task_id):
    task = retrieve_model(Task, task_id)
    request_body = request.get_json()

    task.title = request_body["title"]
    task.description = request_body["description"]
    db.session.commit()

    return Response(status=204, mimetype='application/json')

@bp.delete("/<task_id>")
def delete_task(task_id):
    task = retrieve_model(Task, task_id)
    db.session.delete(task)
    db.session.commit()
    return Response(status=204, mimetype='application/json')