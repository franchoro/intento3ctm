from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
db = SQLAlchemy(app)


class Reglamento(db.Model):
  __tablename__ = 'reglamento'

  id_reg = db.Column(db.Integer, primary_key=True)
  contenido_reg = db.Column(db.String(2000), unique=True, nullable=False)
  nom_reg = db.Column(db.String(80), unique=True, nullable=False)
  fecha_reg = db.Column(db.Date, unique=True, nullable=False)

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

# obtener todos los reglamentos
#@app.route('/reglamento', methods=['GET'])
#def get_all_reglamentos():
#  try:
#    reglamentos = Reglamento.query.all()
#    return make_response(jsonify([reglamento.json() for reglamento in reglamentos]), 200)
#
#  except Exception as e:
#    return make_response(jsonify({'message': 'error getting reglamentos'}), 500)
  

@app.route('/reglamento', methods=['GET'])
def get_all_reglamentos():
    try:
        reglamentos = Reglamento.query.all()
        reglamento_data = [reglamento.json() for reglamento in reglamentos]
        
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
      return make_response(jsonify({'reglamento': reglamento.json()}), 200)
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
