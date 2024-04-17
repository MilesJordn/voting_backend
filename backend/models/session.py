import sqlites3
class Session:
    def __ init __(self, id_session = None, session_name = None,  
        session_date = None, winner = None):
          self.id_session = id_session
          self.session_name= session_name
          self.session_date = session_date
          self.winner = winner

 
    def save(self):
        if self.id_session:
            query = f"UPDATE {self.__class__.TABLE_NAME} SET session_name=?,session_date=?,winner=? WHERE id_session=?"
            
            with sqlite3.connect("db.sqlite") as connection:
                cursor = connection.cursor()
                cursor.execute(query, (self.session_name, self.session_date, self.winner,  self.id_session))
        else:
            # save into the database
            query = f"INSERT INTO {self.__class__.TABLE_NAME} (session_name, session_date, winner) VALUES(?,?,?,?)"
            with sqlite3.connect("db.sqlite") as connection:
                cursor = connection.cursor()
                cursor.execute(query, (self.session_name, self.session_date, self.winner ))

                new_instance_id_session = cursor.execute(f"SELECT MAX(id_session) FROM {self.__class__.TABLE_NAME}").fetchone()[0]

                self.id_session = new_instance_id_session

    def read(id_session=None):
        with sqlite3.connect("db.sqlite") as connection:
            cursor = connection.cursor()++++++++++++++++++++++++++++++++++++++++
            if id_session:
                query = f"SELECT (id_session, session_name, session_date, winner ) FROM {self.__class__.TABLE_NAME} WHERE id_session=?"

                result = cursor.execute(query, (id_session, )).fetchone()

                session = Session(session_name=result[1], session_date=result[2], winner=result[3], 
                session.id_session = result[0]

                return session
            else:
                query = f"SELECT (id_session, session_name, session_date, session, duration) FROM {self.__class__.TABLE_NAME}"
                results = cursor.execute(query).fetchall()
                exams = []

                for result in results:
                    exam = Exam(subject=result[1], academic_year=result[2], session=result[3], duration=result[4])
                    exam.id = result[0]

                    exams.append(exam)
                
                return exams
    
    def delete(self):
        if self.id:
            with sqlite3.connect("db.sqlite") as connection:
                cursor = connection.cursor()

                cursor.execute(f"DELETE FROM {self.__class__.TABLE_NAME} WHERE id=?", (self.id, ))