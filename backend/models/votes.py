import sqlite3
class Votes:
    def __init __(self, id_vote = None, participant_id = None, candidate_id = None ):
        self.id_vote = id_vote
        self.participant_id = participant_id
        self.candidate_id  = candidate_id 
        self.participant_name  = participant_name  
        



    def save(self):
        if self.id_vote:
            query = f"UPDATE {self.__class__.TABLE_NAME} SET participant_id=?,candidate_id =?, WHERE id_vote=?, WHERE participant_name=?",
            
            with sqlite3.connect("db.sqlite") as connection:
                cursor = connection.cursor()
                cursor.execute(query, (self.participant_id, self.candidate_id ,  self.id_vote, self.participant_name)
        else:
            # save into the database
            query = f"INSERT INTO {self.__class__.TABLE_NAME} (participant_id, candidate_id, participant_name) VALUES(?,?,?,?)"
            with sqlite3.connect("db.sqlite") as connection:
                cursor = connection.cursor()
                cursor.execute(query, (self.participant_id, self.candidate_id, participant_name))

                new_instance_id_session = cursor.execute(f"SELECT MAX(id_vote) FROM {self.__class__.TABLE_NAME}").fetchone()[0]

                self.id_vote = new_instance_id_vote

    def read(id_vote=None):
        with sqlite3.connect("db.sqlite") as connection:
            cursor = connection.cursor()++++++++++++++++++++++++++++++++++++++++
            if id_vote:
                query = f"SELECT (id_vote, participant_id,candidate_id, participant_name ) FROM {self.__class__.TABLE_NAME} WHERE id_vote=?"

                result = cursor.execute(query, (id_vote, )).fetchone()

            votes= Votes(participant_id=result[1], candidate_id =result[2], participant_name=result[3], 
                 votes.id_votes = result[0]

                return  votes
            else:
                query = f"SELECT (id_votes, participant_id, candidate_id, participant_name) FROM {self.__class__.TABLE_NAME}"
                results = cursor.execute(query).fetchall()
               votes = []

                for result in results:
                   votes = Votes (participant_id=result[1], candidate_id=result[2], participant_name=result[3], 
                    votes.id = result[0]

                   Votes.append(exam)
                
                return votes
    
    def delete(self):
        if self.votes.id:
            with sqlite3.connect("db.sqlite") as connection:
                cursor = connection.cursor()

                cursor.execute(f"DELETE FROM {self.__class__.TABLE_NAME} WHERE votes.id=?", (self.votes.id, ))
 