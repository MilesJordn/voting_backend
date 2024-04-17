import os
    
from models.sessions import Session
#from .files import save_file

#from werkzeug.utils import secure_filename

from constants import UPLOAD_FOLDER

def get_all_sessions(return_objects=False):
    """
    Set return_objects to True if you want to return a 
    model instance instead of JSON
    """
    objects = Session.read()

    if not return_objects:
        list_of_objects = [
            obj.toJSON() for obj in objects
        ]
        return list_of_objects
    
    return objects

def get_session_with_id_session(id_session, return_object=False):
    """
    Set return_object to True if you want to return a 
    model instance instead of JSON
    """
    obj = Session.read(id_session)

    return obj if return_object else obj.toJSON()

def save_session(session_name, session_date, winner,  id_session=None, uploaded_files=None, return_object=False):
    if id_session != None:
        session = get_session_with_id_session(id_session, return_object=True)
        session.session_name, session.session_date, session.winner = (
            session_name, session_date, winner
        )
    else:
        session = Session(
            session_name=session_name,session_date=session_date, 
            winner=winner
        )

      session.save()

   # for file in uploaded_files:
    #    file_name = secure_filename(file.filename)

     #   save_file(exam=exam.id, path=file_name)

      #  file.save(
       #     os.path.join(UPLOAD_FOLDER, file_name)
        #)

    return session if return_object else session.toJSON()
    
def delete_session(id_session):
    session = get_session_with_id_session(id_sessions)
    session.dselete()

    return session.toJSON()