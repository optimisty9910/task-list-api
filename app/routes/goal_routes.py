from flask import Blueprint
from ..models.goal import Goal
from ..db import db
from flask import request, Response
from .route_utilities import create_model, delete_model, get_models_with_filters, retrieve_model

bp = Blueprint("goal", __name__, url_prefix="/goals")

@bp.post("")
def create_goal():
    request_body = request.get_json()
    return create_model(Goal, request_body)

@bp.get("")
def get_all_goals():
    return get_models_with_filters(Goal, request.args)

@bp.get("/<goal_id>")
def get_one_goal(goal_id):
    return retrieve_model(Goal, goal_id).to_dict()

@bp.put("/<goal_id>")
def update_goal(goal_id):
    goal = retrieve_model(Goal, goal_id)
    request_body = request.get_json()

    goal.title = request_body["title"]
    db.session.commit()

    return Response(status=204, mimetype='application/json')

@bp.delete("/<goal_id>")
def delete_goal(goal_id):
    return delete_model(Goal, goal_id)


