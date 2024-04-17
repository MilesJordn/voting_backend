from flask import Blueprint, request

from controllers.votes import *
from models.exceptions import ModelNotFoundError

from .utils import parse_request_data
from .responses import JSONResponse

candidates_view = Blueprint('votes', __name__, url_prefix='/votes')

@votes_view.route('/', methods=['GET', 'POST'])
def list_or_create():
    if request.method == 'GET':
        return get_all_votes()
    else:
        submitted_data = parse_request_data(requests=request)

        subject = save_subject(submitted_data['name'])
        response = JSONResponse(status=201, content_type="application/json", data=subject)

        return response

@subjects_view.route('/<id_vote>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def get_or_update_instance(id_vote):
    instance = None
    try:
        instance = get_subject_with_id_vote(id_vote, return_object=True)
    except ModelNotFoundError:
        return JSONResponse("<h1>Instance not found</h1>", status=404)
    
    if request.method == 'GET':
        return instance
    elif request.method == 'PATCH':
        data = parse_request_data(request)
        return JSONResponse(data=save_subject(name=data['name'], id=instance.id_vote), status=201)
    elif request.method == 'DELETE':
        return JSONResponse(data=delete_subject(id_vote), status=201)
