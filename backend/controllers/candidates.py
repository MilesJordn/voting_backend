import os

from models.candidates import candidate 
#from .files import save_file

#from werkzeug.utils import secure_filename

from constants import UPLOAD_FOLDER

def get_all_candidates(return_objects=False):
    """
    Set return_objects to True if you want to return a 
    model instance instead of JSON
    """
    objects = candidate.read()

    if not return_objects:
        list_of_objects = [
            obj.toJSON() for obj in objects
        ]
        return list_of_objects
    
    return objects    

def get_candidate_with_candidate_id(candidate_id, return_object=False):
    """
    Set return_object to True if you want to return a 
    model instance instead of JSON
    """
    obj = candidate.read(candidate_id)

    return obj if return_object else obj.toJSON()

def save_candidate( name, id_session, candidate_class, post, candidate_id=None, uploaded_files=None, return_object=False):
    if candidate_id != None:
        candidate = get_candidate_with_candidate_id (candidate_id, return_object=True)
        candidate.name, candidate.id_session, candidate.candidate_class, candidate.post = (
            name, id_session, candidate_class, post
        )
    else:
        candidate = Candidate(
        name=name,id_session=id_session, 
            candidate_class=scandidate_class, post=post
        )

   candidate.save()

 #   for file in uploaded_files:
  #      file_name = secure_filename(file.filename)

   #     save_file(exam=exam.id, path=file_name)

    #    file.save(
     #       os.path.join(UPLOAD_FOLDER, file_name)
      #  )

    return candidate if return_object else candidate.toJSON()
    
def delete_candidate(candidate_id):
    candidate = get_candidate_with_candidate_id(candidate_id)
    candidate.delete()

    return candidate.toJSON()