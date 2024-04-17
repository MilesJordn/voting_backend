import os
    
from models.votes import Vote
#from .files import save_file

#from werkzeug.utils import secure_filename

from constants import UPLOAD_FOLDER

def get_all_votes(return_objects=False):
    """
    Set return_objects to True if you want to return a 
    model instance instead of JSON
    """
    objects = Vote.read()

    if not return_objects:
        list_of_objects = [
            obj.toJSON() for obj in objects
        ]
        return list_of_objects
    
    return objects

def get_vote_with_id_vote(id_vote, return_object=False):
    """
    Set return_object to True if you want to return a 
    model instance instead of JSON
    """
    obj = Vote.read(id_vote)

    return obj if return_object else obj.toJSON()

def save_vote(candidate,  id_vote=None, uploaded_files=None, return_object=False):
    if id_vote != None:
        vote = get_vote_with_id_vote(id_vote, return_object=True)
        vote.candidate, = (
            candidate
        )
    else:
        vote = Vote(
            candidate_id=candidate,#academic_year=academic_year, 
            #session=session, duration=duration
        )

    vote.save()

  #  for file in uploaded_files:
   #     file_name = secure_filename(file.filename)

    #    save_file(exam=exam.id, path=file_name)

     #   file.save(
      #      os.path.join(UPLOAD_FOLDER, file_name)
       # )

    return vote if return_object else vote.toJSON()
    
def delete_vote(id_vote):
    vote = get_vote_with_id_vote(id_vote
    vote.delete()

    return vote.toJSON()