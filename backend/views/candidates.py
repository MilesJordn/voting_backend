from flask import Blueprint, request

from controllers.candidates import *  
from models.exceptions import ModelNotFoundError   

from .utils import parse_request_data   
from .responses import JSONResponse, instance_not_found_response

exams_view = Blueprint('candidates', __name__, url_prefix='/candidates')

@candidates_view.route('/', methods=['GET', 'POST'])
def list_or_create():
    if request.method == 'GET':
        return JSONResponse(data=get_all_candiddates())
    else:
        submitted_data = request.form    
        #files = request.files.getlist("files")

        name, post, candidate_class, id_session = (
            submitted_data['name'], submitted_data['post'], 
            submitted_data['candidate_class'], submitted_data['id_session']
        )

        return JSONResponse(data=save_session(name, post, candidate_class, id_session, uploaded_files=files), status=201)
    
@candidates_view.route('/<id>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def get_or_update_instance(candidate_id):
    instance = None
    try:
        instance = get_candidate_with_candidate_id(candidate_id, return_object=True)
    except ModelNotFoundError:
        return instance_not_found_response
    
    if request.method == 'GET':
        return JSONResponse(data=instance)
    elif request.method == 'PATCH':
        submitted_data = request.form
      #s  files = request.files.getlist("files")

        name, post, candidate_class, id_sessions = (
            submitted_data['name'], submitted_data['post'], 
            submitted_data['candidate_class'], submitted_data['id_session']
        )

        return JSONResponse(data=save_candidate(name, post, candidate_class, id_session, uploaded_files=files, id=instance.id), status=201)
    elif request.method == 'DELETE':
        instance.delete()

        return JSONResponse(data=instance, status   s=200)
    