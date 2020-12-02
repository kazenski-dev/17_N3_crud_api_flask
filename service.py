from connection import Connection


class StudentService():

    def save(self, dict_data):

        name = dict_data.get("name") #dict
        cpf = dict_data.get("cpf")
        email = dict_data.get("email")

        self.validate_name(name)
        self.validate_cpf(cpf)
        self.validate_email(email)
        self.validate_must_have(name, cpf, email)

        conn = Connection().get_connection()

        cur = conn.cursor()
        cur.execute ("insert into student (name, cpf, email, situation)\
                    values ('{0}','{1}','{2}', '1')".format(name, cpf, email))

        conn.commit()
        conn.close()

    def list_all(self):

        conn = Connection().get_connection()

        cur = conn.cursor()
        cur.execute("select * from student where situation = '1'")

        rows = cur.fetchall()

        new_list = []

        for row in rows:
            dict_01 = {"id": row[0], "name": row[1], "cpf": row[2], "email": row[3]}
            new_list.append(dict_01)

        #conn.commit()
        conn.close()

        return new_list

    def list_by_id(self, dict_data):
   
        cpf = dict_data.get("cpf")

        self.validate_cpf(cpf)

        conn = Connection().get_connection()

        cur = conn.cursor()
        cur.execute("select * from student where situation = '1' AND cpf = '{0}'".format(cpf))

        rows = cur.fetchall()

        new_list = []
        for row in rows:
            dict_01 = {"id": row[0], "name": row[1], "cpf": row[2], "email": row[3]}
            new_list.append(dict_01)
            
        conn.commit()
        conn.close()

        return new_list

    def list_by_email(self, dict_data):

        email = dict_data.get("email")

        self.validate_email(email)

        conn = Connection().get_connection()

        cur = conn.cursor()
        cur.execute("select * from student where situation = '1' AND email = '{0}'".format(email))

        rows = cur.fetchall()

        new_list = []
        for row in rows:
            dict_01 = {"id": row[0], "name": row[1], "cpf": row[2], "email": row[3]}
            new_list.append(dict_01)

        conn.commit()
        conn.close()

        return new_list

    def update_name(self, dict_data):
        
        cpf = dict_data.get("cpf")
        self.validate_cpf(cpf)

        name = dict_data.get("name") #dict
        self.validate_name(name)

        conn = Connection().get_connection()

        cur = conn.cursor()
        cur.execute("Update student set name = '{0}' WHERE cpf = '{1}' AND situation = '1'".format(name, cpf))

        conn.commit()
        conn.close()

    def update_email(self, dict_data):

        cpf = dict_data.get("cpf")
        self.validate_cpf(cpf)

        email = dict_data.get("email")
        self.validate_email(email)

        conn = Connection().get_connection()

        cur = conn.cursor()
        cur.execute("Update student set email = '{0}' WHERE cpf = '{1}' AND situation = '1'".format(email, cpf))
        conn.commit()
        conn.close()

    def delete(self, dict_data):

        cpf = dict_data.get("cpf")
        self.validate_cpf(cpf)

        conn = Connection().get_connection()

        cur = conn.cursor()
        cur.execute("Update student set situation = '0' WHERE cpf = '{0}' AND situation = '1'".format(cpf))
        conn.commit()

        conn.close()

#------------------- VALIDATIONS
    def validate_email(self, email):
        #codigo para validar email
        if len(email) <= 400:
            return("Valid email.")   
        else:
            raise Exception("Valid email.")

    def validate_name(self, nome):
        #somente letras
        if len(nome) <= 150:
            return("Valid name.")
        else:
            raise Exception("Invalid name.")

    def validate_cpf(self, cpf):
        if cpf.isdigit() == True and len(cpf) == 11:
            return("Valid cpf.")
        else:
            raise Exception("Invalid cpf.")

    def validate_must_have(self, name, cpf, email):
        #codigo para validar campos
        if name is None:
            raise Exception("Must have the name")
        if cpf is None:
            raise Exception("Must have the cpf")
        if email is None:
            raise Exception("Must have the email")