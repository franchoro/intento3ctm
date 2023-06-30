from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
db = SQLAlchemy(app)



#Creamos las clases que vendran a ser las tablas

#Tabla reglamento
class Reglamento(db.Model):
  __tablename__ = 'reglamento'

  id_reg = db.Column(db.Integer, primary_key=True)
  contenido_reg = db.Column(db.String(2000), unique=True, nullable=False)
  nom_reg = db.Column(db.String(80), unique=True, nullable=False)
  fecha_reg = db.Column(db.Date, nullable=False)
  def jsonReg(self):
        return {'id_reg': self.id_reg,'contenido_reg': self.contenido_reg, 'nom_reg': self.nom_reg, 'fecha_reg':self.fecha_reg}


#Tabla alumno
class Alumno(db.Model):
    __tablename__ = 'alumno'

    id_al = db.Column(db.Integer, primary_key=True)
    nom_al = db.Column(db.String(50), nullable=False)
    carrera_al = db.Column(db.String(50), nullable=False)
    activa_al = db.Column(db.Boolean, nullable=False)
    mail_al=db.Column(db.String(50), unique=True, nullable=False)
    contrasena_al=db.Column(db.String(50), nullable=False)
    id_reg1 = db.Column(db.Integer, db.ForeignKey('reglamento.id_reg'))
    reglamento = db.relationship('Reglamento',backref='alumnos')
    

    def jsonAl(self):
        return {'id_al': self.id_al, 'nom_al': self.nom_al,
                'carrera_al': self.carrera_al, 'activa_al':self.activa_al, 
                'mail_al':self.mail_al, 'contrasena_al':self.contrasena_al,
                'id_reg1':self.id_reg1
}


#Tabla profesor

class Profesor(db.Model):
    __tablename__ = 'profesor'

    id_profe = db.Column(db.Integer, primary_key=True)
    nom_profe = db.Column(db.String(50), nullable=False)
    profesion_profe = db.Column(db.String(50), nullable=False)
    activa_profe = db.Column(db.Boolean, nullable=False)
    mail_profe=db.Column(db.String(50), unique=True, nullable=False)
    contrasena_profe=db.Column(db.String(50), nullable=False)

    

    def jsonProfe(self):
        return {'id_profe': self.id_profe, 'nom_profe': self.nom_profe,
                'profesion_profe': self.profesion_profe, 'activa_profe':self.activa_profe, 
                'mail_profe':self.mail_profe, 'contrasena_profe':self.contrasena_profe,

}

#Tabla admin


class Admin(db.Model):
    __tablename__ = 'admin'

    id_admin = db.Column(db.Integer, primary_key=True)
    nom_admin = db.Column(db.String(50), nullable=False)
    profesion_admin = db.Column(db.String(50), nullable=False)
    activa_admin = db.Column(db.Boolean, nullable=False)
    mail_admin=db.Column(db.String(50), unique=True, nullable=False)
    contrasena_admin=db.Column(db.String(50), nullable=False)

    

    def jsonAdmin(self):
        return {'id_admin': self.id_admin, 'nom_admin': self.nom_admin,
                'profesion_admin': self.profesion_admin, 'activa_admin':self.activa_admin, 
                'mail_admin':self.mail_admin, 'contrasena_admin':self.contrasena_admin,

}

#Tabla pasantia

class Pasantia(db.Model):
    __tablename__ = 'pasantia'

    id_pas = db.Column(db.Integer, primary_key=True)
    nom_pas = db.Column(db.String(50), nullable=False)
    nota1 = db.Column(db.Integer, nullable=False)
    nota2 = db.Column(db.Integer, nullable=False)
    nota_final = db.Column(db.Integer, nullable=False)
    id_profe1 = db.Column(db.Integer, db.ForeignKey('profesor.id_profe'))
    profesor = db.relationship('Profesor',backref='pasantias')
    id_al1 = db.Column(db.Integer, db.ForeignKey('alumno.id_al'))
    alumno = db.relationship('Alumno',backref='pasantias')
    id_admin1 = db.Column(db.Integer, db.ForeignKey('admin.id_admin'))
    admin = db.relationship('Admin',backref='pasantias')
    

    def jsonPas(self):
        return {'id_pas': self.id_pas, 'nom_pas':self.nom_pas, 'nota1':self.nota1,
                'nota2':self.nota2, 'nota_final':self.nota_final, 'id_profe1':self.id_profe1,
          'id_al1' :self.id_al1, 'id_admin1' :self.id_admin1  
}


db.create_all()


#create a test route
@app.route('/test', methods=['GET'])
def test():
  return make_response(jsonify({'message': 'test route'}), 200)




#REGLAMENTO
# crear un reglamento
@app.route('/reglamento', methods=['POST'])
def crear_reglamento():
  try:
    data = request.get_json()

    

    new_reglamento = Reglamento(id_reg=data['id_reg'], contenido_reg=data['contenido_reg'], nom_reg=data['nom_reg'], fecha_reg=data['fecha_reg'])
    db.session.add(new_reglamento)
    db.session.commit()
    return make_response(jsonify({'message': 'reglamento created'}), 201)
  except Exception as e:
    return make_response(jsonify({'message': 'error creating reglamento'}), 500)

#Obtener reglamento
@app.route('/reglamento', methods=['GET'])
def get_all_reglamentos():
    try:
        reglamentos = Reglamento.query.all()
        reglamento_data = [reglamento.jsonReg() for reglamento in reglamentos]
        
        if len(reglamento_data) == 0:
            return make_response(jsonify({'message': 'no reglamentos found'}), 404)
        
        return make_response(jsonify(reglamento_data), 200)

    except Exception as e:
        print(e)
        return make_response(jsonify({'message': 'error getting reglamentos'}), 500)

# obtener reglamento por id_reg
@app.route('/reglamento/<int:id_reg>', methods=['GET'])
def get_reglamento(id_reg):
  try:
    reglamento = Reglamento.query.filter_by(id_reg=id_reg).first()
    if reglamento:
      return make_response(jsonify({'reglamento': reglamento.jsonReg()}), 200)
    return make_response(jsonify({'message': 'reglamento not found'}), 404)
  except Exception as e:
    return make_response(jsonify({'message': 'error getting reglamento'}), 500)

# actualiza reglamento
@app.route('/reglamento/<int:id_reg>', methods=['PUT'])
def update_reglamento(id_reg):
  try:
    reglamento = Reglamento.query.filter_by(id_reg=id_reg).first()
    if reglamento:
      data = request.get_json()
      reglamento.contenido_reg = data['contenido_reg']
      reglamento.nom_reg = data['nom_reg']
      reglamento.fecha_reg = data['fecha_reg']
      db.session.commit()
      return make_response(jsonify({'message': 'reglamento updated'}), 200)
    return make_response(jsonify({'message': 'reglamento not found'}), 404)
  except Exception as e:
    return make_response(jsonify({'message': 'error updating reglamento'}), 500)

# borrar reglamento
@app.route('/reglamento/<int:id_reg>', methods=['DELETE'])
def delete_user(id_reg):
  try:
    reglamento = Reglamento.query.filter_by(id_reg=id_reg).first()
    if reglamento:
      db.session.delete(reglamento)
      db.session.commit()
      return make_response(jsonify({'message': 'reglamento deleted'}), 200)
    return make_response(jsonify({'message': 'reglamento not found'}), 404)
  except Exception as e:
    return make_response(jsonify({'message': 'error deleting reglamento'}), 500)



#ALUMNOS

# crear un alumno
@app.route('/alumno', methods=['POST'])
def crear_alumno():
  try:
    data = request.get_json()

    

    new_alumno = Alumno(id_al=data['id_al'], nom_al=data['nom_al'], carrera_al=data['carrera_al'], activa_al=data['activa_al'], mail_al=data['mail_al'], contrasena_al=data['contrasena_al'], id_reg1=data['id_reg1'])
    db.session.add(new_alumno)
    db.session.commit()
    return make_response(jsonify({'message': 'alumno created'}), 201)
  except Exception as e:
    return make_response(jsonify({'message': 'error creating alumno'}), 500)

#obtener alumno

@app.route('/alumno', methods=['GET'])
def get_all_alumnos():
    try:
        alumnos = Alumno.query.all()
        alumno_data = [alumno.jsonAl() for alumno in alumnos]
        
        if len(alumno_data) == 0:
            return make_response(jsonify({'message': 'no alumnos found'}), 404)
        
        return make_response(jsonify(alumno_data), 200)

    except Exception as e:
        print(e)
        return make_response(jsonify({'message': 'error getting alumnos'}), 500)

# obtener alumno por id_al
@app.route('/alumno/<int:id_al>', methods=['GET'])
def get_alumno(id_al):
  try:
    alumno = Alumno.query.filter_by(id_al=id_al).first()
    if alumno:
      return make_response(jsonify({'alumno': alumno.jsonAl()}), 200)
    return make_response(jsonify({'message': 'alumno not found'}), 404)
  except Exception as e:
    return make_response(jsonify({'message': 'error getting alumno'}), 500)
  




# actualiza alumno
@app.route('/alumno/<int:id_al>', methods=['PUT'])
def update_alumno(id_al):
  try:
    alumno = Alumno.query.filter_by(id_reg=id_al).first()
    if alumno:
      data = request.get_json()
      alumno.nom_al=data['nom_al']
      alumno.carrera_al=data['carrera_al']
      alumno.id_reg1=data['id_reg1'] 
      alumno.activa_al=data['activa_al']
      alumno.contrasena_al=data['contrasena_al']
      db.session.commit()
      return make_response(jsonify({'message': 'alumno updated'}), 200)
    return make_response(jsonify({'message': 'alumno not found'}), 404)
  except Exception as e:
    return make_response(jsonify({'message': 'error updating alumno'}), 500)

# borrar alumno
@app.route('/reglamento/<int:id_al>', methods=['DELETE'])
def delete_alumno(id_al):
  try:
    alumno = Alumno.query.filter_by(id_al=id_al).first()
    if alumno:
      db.session.delete(alumno)
      db.session.commit()
      return make_response(jsonify({'message': 'alumno deleted'}), 200)
    return make_response(jsonify({'message': 'alumno not found'}), 404)
  except Exception as e:
    return make_response(jsonify({'message': 'error deleting alumno'}), 500)



#PROFESORES 

# crear un profesor
@app.route('/profesor', methods=['POST'])
def crear_profesor():
  try:
    data = request.get_json()

    

    new_profesor = Profesor(id_profe=data['id_profe'], nom_profe=data['nom_profe'], profesion_profe=data['profesion_profe'], activa_profe=data['activa_profe'], mail_profe=data['mail_profe'], contrasena_profe=data['contrasena_profe'])
    db.session.add(new_profesor)
    db.session.commit()
    return make_response(jsonify({'message': 'profesor created'}), 201)
  except Exception as e:
    return make_response(jsonify({'message': 'error creating profesor'}), 500)


#Obtener todos los profesores

@app.route('/profesor', methods=['GET'])
def get_all_profesores():
    try:
        profesores = Profesor.query.all()
        profesor_data = [profesor.jsonProfe() for profesor in profesores]
        
        if len(profesor_data) == 0:
            return make_response(jsonify({'message': 'no profesores found'}), 404)
        
        return make_response(jsonify(profesor_data), 200)

    except Exception as e:
        print(e)
        return make_response(jsonify({'message': 'error getting profesores'}), 500)

# obtener profesor por id_profe
@app.route('/profesor/<int:id_profe>', methods=['GET'])
def get_profesor(id_profe):
  try:
    profesor = Profesor.query.filter_by(id_profe=id_profe).first()
    if profesor:
      return make_response(jsonify({'profesor': profesor.jsonProfe()}), 200)
    return make_response(jsonify({'message': 'profesor not found'}), 404)
  except Exception as e:
    return make_response(jsonify({'message': 'error getting profesor'}), 500)
  




# actualiza profesor
@app.route('/profesor/<int:id_profe>', methods=['PUT'])
def update_profesor(id_profe):
  try:
    profesor = Profesor.query.filter_by(id_profe=id_profe).first()
    if profesor:
      data = request.get_json()
      profesor.nom_profe=data['nom_profe']
      profesor.profesion_profe=data['profesion_profe']
      profesor.activa_profe=data['activa_profe']
      profesor.contrasena_profe=data['contrasena_profe']
      db.session.commit()
      return make_response(jsonify({'message': 'profesor updated'}), 200)
    return make_response(jsonify({'message': 'profesor not found'}), 404)
  except Exception as e:
    return make_response(jsonify({'message': 'error updating profesor'}), 500)

# borrar profesor
@app.route('/profesor/<int:id_profe>', methods=['DELETE'])
def delete_profesor(id_profe):
  try:
    profesor = Profesor.query.filter_by(id_profe=id_profe).first()
    if profesor:
      db.session.delete(profesor)
      db.session.commit()
      return make_response(jsonify({'message': 'profesor deleted'}), 200)
    return make_response(jsonify({'message': 'profesor not found'}), 404)
  except Exception as e:
    return make_response(jsonify({'message': 'error deleting profesor'}), 500)




#ADMINISTRADORES 

# crear un admin
@app.route('/admin', methods=['POST'])
def crear_admin():
  try:
    data = request.get_json()

    

    new_admin = Admin(id_admin=data['id_admin'], nom_admin=data['nom_admin'], profesion_admin=data['profesion_admin'], activa_admin=data['activa_admin'], mail_admin=data['mail_admin'], contrasena_admin=data['contrasena_admin'])
    db.session.add(new_admin)
    db.session.commit()
    return make_response(jsonify({'message': 'admin created'}), 201)
  except Exception as e:
    return make_response(jsonify({'message': 'error creating admin'}), 500)


#Obtener todos los admins

@app.route('/admin', methods=['GET'])
def get_all_admins():
    try:
        admins = Admin.query.all()
        admin_data = [admin.jsonAdmin() for admin in admins]
        
        if len(admin_data) == 0:
            return make_response(jsonify({'message': 'no admins found'}), 404)
        
        return make_response(jsonify(admin_data), 200)

    except Exception as e:
        print(e)
        return make_response(jsonify({'message': 'error getting admins'}), 500)

# obtener admin por id_admin
@app.route('/admin/<int:id_admin>', methods=['GET'])
def get_admin(id_admin):
  try:
    admin = Admin.query.filter_by(id_admin=id_admin).first()
    if admin:
      return make_response(jsonify({'admin': admin.jsonAdmin()}), 200)
    return make_response(jsonify({'message': 'admin not found'}), 404)
  except Exception as e:
    return make_response(jsonify({'message': 'error getting admin'}), 500)
  




# actualiza admin
@app.route('/admin/<int:id_admin>', methods=['PUT'])
def update_admin(id_admin):
  try:
    admin = Admin.query.filter_by(id_admin=id_admin).first()
    if admin:
      data = request.get_json()
      admin.nom_admin=data['nom_admin']
      admin.profesion_admin=data['profesion_admin']
      admin.activa_admin=data['activa_admin']
      admin.contrasena_admin=data['contrasena_admin']
      db.session.commit()
      return make_response(jsonify({'message': 'admin updated'}), 200)
    return make_response(jsonify({'message': 'admin not found'}), 404)
  except Exception as e:
    return make_response(jsonify({'message': 'error updating admin'}), 500)

# borrar admin
@app.route('/admin/<int:id_admin>', methods=['DELETE'])
def delete_admin(id_admin):
  try:
    admin = Admin.query.filter_by(id_admin=id_admin).first()
    if admin:
      db.session.delete(admin)
      db.session.commit()
      return make_response(jsonify({'message': 'admin deleted'}), 200)
    return make_response(jsonify({'message': 'admin not found'}), 404)
  except Exception as e:
    return make_response(jsonify({'message': 'error deleting admin'}), 500)



#PASANTIAS

#{'id_pas', 'nom_pas', 'nota1','nota2', 'nota_final', 'id_profe1','id_al1', 'id_admin1' 


# crear una pasantia
@app.route('/pasantia', methods=['POST'])
def crear_pasantia():
  try:
    data = request.get_json()

    

    new_pasantia = Pasantia(id_pas=data['id_pas'], nom_pas=data['nom_pas'], nota1=data['nota1'], 
                            nota2=data['nota2'], nota_final=data['nota_final'], id_profe1=data['id_profe1'],
                            id_al1=data['id_al1'], id_admin1=data['id_admin1'])
    db.session.add(new_pasantia)
    db.session.commit()
    return make_response(jsonify({'message': 'pasantia created'}), 201)
  except Exception as e:
    return make_response(jsonify({'message': 'error creating pasantia'}), 500)


#Obtener todas las pasantias

@app.route('/pasantia', methods=['GET'])
def get_all_pasantias():
    try:
        pasantias = Pasantia.query.all()
        pasantia_data = [pasantia.jsonPas() for pasantia in pasantias]
        
        if len(pasantia_data) == 0:
            return make_response(jsonify({'message': 'no pasantias found'}), 404)
        
        return make_response(jsonify(pasantia_data), 200)

    except Exception as e:
        print(e)
        return make_response(jsonify({'message': 'error getting pasantias'}), 500)

# obtener pasantias por id_pas
@app.route('/pasantia/<int:id_pas>', methods=['GET'])
def get_pasantia(id_pas):
  try:
    pasantia = Pasantia.query.filter_by(id_pas=id_pas).first()
    if pasantia:
      return make_response(jsonify({'pasantia': pasantia.jsonPas()}), 200)
    return make_response(jsonify({'message': 'pasantia not found'}), 404)
  except Exception as e:
    return make_response(jsonify({'message': 'error getting pasantia'}), 500)
  


#{'id_pas', 'nom_pas', 'nota1','nota2', 'nota_final', 'id_profe1','id_al1', 'id_admin1'

# actualiza pasantia
@app.route('/pasantia/<int:id_pas>', methods=['PUT'])
def update_pasantia(id_pas):
  try:
    pasantia = Pasantia.query.filter_by(id_pas=id_pas).first()
    if pasantia:
      data = request.get_json()
      pasantia.nom_pas=data['nom_pas']
      pasantia.nota1=data['nota1']
      pasantia.nota2=data['nota2']
      pasantia.nota_final=data['nota_final']
      db.session.commit()
      return make_response(jsonify({'message': 'pasantia updated'}), 200)
    return make_response(jsonify({'message': 'pasantia not found'}), 404)
  except Exception as e:
    return make_response(jsonify({'message': 'error updating pasantia'}), 500)

# borrar pasantia
@app.route('/pasantia/<int:id_pas>', methods=['DELETE'])
def delete_pasantia(id_pas):
  try:
    pasantia = Pasantia.query.filter_by(id_pas=id_pas).first()
    if pasantia:
      db.session.delete(pasantia)
      db.session.commit()
      return make_response(jsonify({'message': 'pasantia deleted'}), 200)
    return make_response(jsonify({'message': 'pasantia not found'}), 404)
  except Exception as e:
    return make_response(jsonify({'message': 'error deleting pasantia'}), 500)

