import sqlite3

from base_model import AbstractBaseModel

class Candidate(AbstractBaseModel):
    TABLE_NAME = "Candidates"


    def __init __(self, candidate_id = None, candidate_name = None, andidate_post = None, id_session = None ):
        self.candidate_id = candidate_id
        self.candidate_name = candidate_name
        self.candidate_post = candidate_post 
        self.id_session = id_session

    def save(self): 
         if self.candidate_id: 
            query = f"UPDATE {self.__class__.TABLE_NAME} SET  candidate_name=?,candidate_post=?,id_session=? WHERE candidate_id=?"
            
            with sqlite3.connect("db.sqlite") as connection:
                cursor = connection.cursor()   
                cursor.execute(query, ( self.candidate_name, self.candidate_post, self.id_session, self.candidate_id))
         else:
            # save into the database
            query = f"INSERT INTO {self.__class__.TABLE_NAME} (candidate_name,candidate_post, id_session) VALUES(?,?,?,?)"
            with sqlite3.connect("db.sqlite") as connection:
                cursor = connection.cursor()
                cursor.execute(query, ( self.candidate_name, self.candidate_post, self.id_session))

                new_instance_candidate_id = cursor.execute(f"SELECT MAX(candidate_id) FROM {self.__class__.TABLE_NAME}").fetchone()[0]

                self.candidate_id= new_instance_candidate_id
    def read(candidate_id=None):
        with sqlite3.connect("db.sqlite") as connection:
            cursor = connection.cursor()++++++++++++++++++++++++++++++++++++++++
            if candidate_id:
                query = f"SELECT (candidate_id, candidate_name, candidate_post, id_session) FROM {self.__class__.TABLE_NAME} WHERE candidate_id=?"

                result = cursor.execute(query, (candidate_id, )).fetchone()

               candidate = Candidate(candidate=result[1], candidate_name=result[2], candidate_post=result[3], id_session=result[4])
                exam.candidate_id = result[0]  

                return candidate
            else:
                query = f"SELECT (candidate_id, candidate_name,candidate_post,  id_session) FROM {self.__class__.TABLE_NAME}"
                results = cursor.execute(query).fetchall()
                candidate = []

                for result in results:
                  candidate = Candidate(candidate_name=result[1], candidate_post=result[2], id_session=result[3], 
                    candidate.candidate_id = result[0]

                    candidates.append(candidate)
                
                return candidates           

    def delete(self):
        if self.candidate_id :
            with sqlite3.connect("db.sqlite") as connection:
                cursor = connection.cursor()

                cursor.execute(f"DELETE FROM {self.__class__.TABLE_NAME} WHERE candidate_id =?", (self.candidate_id , ))            