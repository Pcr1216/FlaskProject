from flask import Flask, request, jsonify,render_template
from flask_sqlalchemy import SQLAlchemy
import mysql.connector as m

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Bbshark%401234@localhost:3306/services'
db = SQLAlchemy(app)
# mydatabase=m.connect(host="localhost",user="root",password="root",database="services")
# cursor=mydatabase.cursor()
# query="create table accommodation(id int primary key auto_increment, brokername varchar(100),contactno int);"
# cursor.execute(query)
# ------------------------------------------------------------
@app.route('/')
def gethomie():
    return render_template('homie.html')

# ----------------------------------------------------------
class Accommodation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brokername = db.Column(db.String(100))
    contactno = db.Column(db.Integer)

@app.route('/accommodation', methods=['POST'])
def add_accommodation():
    data = request.json
    new_accommodation = Accommodation(brokername=data['brokername'], contactno=data['contactno'])
    db.session.add(new_accommodation)
    db.session.commit()
    return jsonify({'message': 'Person added successfully'})

@app.route('/accommodation', methods=['GET'])
def get_accommodation():
    accommodations = Accommodation.query.all()
    result = [{'id': accommodation.id, 'brokername': accommodation.brokername, 'contactno': accommodation.contactno} for accommodation in accommodations]
    return render_template('accommodation.html',data=result)

@app.route('/accommodation/<int:id>', methods=['PUT'])
def update_accommodation(id):
    accommodation = Accommodation.query.get_or_404(id)
    data = request.json
    accommodation.brokername = data['brokername']
    accommodation.contactno = data['contactno']
    db.session.commit()
    return jsonify({'message': 'Broker updated successfully'})

@app.route('/accommodation/<int:id>', methods=['DELETE'])
def delete_accommodation(id):
    accommodation = Accommodation.query.get_or_404(id)
    db.session.delete(accommodation)
    db.session.commit()
    return jsonify({'message': 'Accommodation deleted successfully'})

# --------------------------------------------------------------------------
class Tiffin_t(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)

@app.route('/tiffin',methods={'GET'})
def get_tiffin():
    tiffin1 = Tiffin_t.query.all()
    result=[{'id': tiffin_t.id,'name': tiffin_t.name,'contact': tiffin_t.contact,'address': tiffin_t.address} for tiffin_t in tiffin1]
    return render_template('tiffin.html',data=result)


@app.route('/tiffin', methods=['POST'])
def add_tiffin():
    data = request.json
    new_tiffin = Tiffin_t(name=data['name'],contact=data['contact'],address=data['address'])
    db.session.add(new_tiffin)
    db.session.commit()
    return jsonify({'message': 'Tiffin added successfully'})


@app.route('/tiffin/<int:id>', methods=['PUT'])
def update_tiffin(id):
    tiffin1 = Tiffin_t.query.get_or_404(id)
    data = request.json
    tiffin1.name = data['name']
    tiffin1.contact = data['contact']
    tiffin1.address = data['address']
    db.session.commit()
    return jsonify({'message': 'Tiffin updated successfully'})

@app.route('/tiffin/<int:id>', methods=['DELETE'])
def delete_tiffin(id):
    tiffin1 = Tiffin_t.query.get_or_404(id)
    db.session.delete(tiffin1)
    db.session.commit()
    return jsonify({'message': 'Tiffin deleted successfully'})



# ------------------------------------------------------------------------

class Clinic(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100), nullable=False)
        address = db.Column(db.String(100), nullable=False)
        distance_in_km = db.Column(db.Float, nullable=False)


@app.route('/clinic', methods=['GET'])
def get_clinic():
    clinics = Clinic.query.all()
    result = [{'id': clinic.id, 'name': clinic.name, 'address': clinic.address, 'distance_in_km': clinic.distance_in_km} for clinic
              in clinics]
    return render_template('clinic.html',data=result)


@app.route('/clinic', methods=['POST'])
def add_clinic():
    data = request.json
    new_clinic = Clinic(name=data['name'], address=data['address'],distance_in_km=data['distance_in_km'])
    db.session.add(new_clinic)
    db.session.commit()
    return jsonify({'message': 'Clinic added successfully'})

@app.route('/clinic/<int:id>', methods=['PUT'])
def update_clinic(id):
    clinics = Clinic.query.get_or_404(id)
    data = request.json
    clinics.name = data['name']
    clinics.address = data['address']
    clinics.distance_in_km = data['distance_in_km']
    db.session.commit()
    return jsonify({'message': 'Clinic updated successfully'})

@app.route('/clinic/<int:id>', methods=['DELETE'])
def delete_clinic(id):
    clinics = Clinic.query.get_or_404(id)
    db.session.delete(clinics)
    db.session.commit()
    return jsonify({'message': 'Clinic deleted successfully'})
# ------------------------------------------------------------

class Medicals(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    MedicalName = db.Column(db.String(80), unique=True, nullable=False)
    Address = db.Column(db.String(200),nullable=False)
    Location = db.Column(db.String(200),nullable=False)


# Routes for CRUD operations
@app.route('/medicals', methods=['GET'])
def get_Medicals():
    medical = Medicals.query.all()
    result = [{'id':medicals.Id, 'name': medicals.MedicalName, 'address': medicals.Address,'location': medicals.Location} for medicals in medical]
    return render_template('medical.html',data=result)

@app.route('/medicals', methods=['POST'])
def add_medicals():
    data = request.json
    new_medical = Medicals(MedicalName=data['name'], Address=data['address'],Location=data['location'])
    db.session.add(new_medical)
    db.session.commit()
    return jsonify({'message': 'Medical added successfully'})

@app.route('/medicals/<int:id>', methods=['PUT'])
def update_medicals(id):
    meds = Medicals.query.get_or_404(id)
    data = request.json
    meds.MedicalName = data['name']
    meds.Address = data['address']
    meds.Location = data['location']
    db.session.commit()
    return jsonify({'message': 'Medical updated successfully'})

@app.route('/medicals/<int:id>', methods=['DELETE'])
def delete_medicals(id):
    meds = Medicals.query.get_or_404(id)
    db.session.delete(meds)
    db.session.commit()
    return jsonify({'message': 'Medical deleted successfully'})

# @app.route('/accommodation/<int:id>', methods=['PUT'])
# def update_accommodation(id):
#     accommodation = Accommodation.query.get_or_404(id)
#     data = request.json
#     accommodation.brokername = data['brokername']
#     accommodation.contactno = data['contactno']
#     db.session.commit()
#     return jsonify({'message': 'Broker updated successfully'})

# ----------------------------------------------------------------------------
class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rname = db.Column(db.String(100), nullable=False)
    contactno = db.Column(db.Float, nullable=False)
    address = db.Column(db.String(100), nullable=False)
    gmaps = db.Column(db.String(100))

@app.route('/restaurants', methods=['GET'])
def get_resto():
    restaurants = Restaurant.query.all()
    result = [{'id': restaurant.id, 'rname': restaurant.rname, 'contactno': restaurant.contactno, 'address': restaurant.address, 'gmaps': restaurant.gmaps} for restaurant
              in restaurants]
    return render_template('restaurant.html',data=result)

@app.route('/restaurants', methods=['POST'])
def add_resto():
    data = request.json
    new_restaurant = Restaurant(rname=data['rname'],contactno=data['contactno'], address=data['address'],gmaps=data['gmaps'])
    db.session.add(new_restaurant)
    db.session.commit()
    return jsonify({'message': 'Restaurant added successfully'})

@app.route('/restaurants/<int:id>', methods=['PUT'])
def update_resto(id):
    restos = Restaurant.query.get_or_404(id)
    data = request.json
    restos.rname = data['rname']
    restos.contactno = data['contactno']
    restos.address = data['address']
    restos.gmap=data['gmaps']
    db.session.commit()
    return jsonify({'message': 'Restaurant updated successfully'})

@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_resto(id):
    restos = Restaurant.query.get_or_404(id)
    db.session.delete(restos)
    db.session.commit()
    return jsonify({'message': 'Restaurant deleted successfully'})

# ----------------------------------------




if __name__ == '__main__':
    app.run(debug=True)

