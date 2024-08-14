import email
from unicodedata import name
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy 


# init the Flask app
app = Flask(__name__)

app.secret_key = "Secret Key"
#SqlAlchemy Database Configuration With Mysql

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mroot@127.1/employee'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///demo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

 
#Creating ORM model table for our employee database

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    def __init__(self, name, email, phone) : 
        self.name = name 
        self.email = email
        self.phone = phone 


with app.app_context():
    db.create_all()
# Flask-server routes 

@app.route('/') # home page

def index():
    all_data = Data.query.all()
    return render_template('index.html', employees = all_data)

@app.route('/insert', methods = ['POST'])

def insert():
        name = request.form['name']
        email= request.form['email']
        phone= request.form['phone']
        
        my_data = Data(name,email,phone)
        db.session.add(my_data)
        db.session.commit()
        flash("Employee Inserted Successfully")

        return redirect(url_for('index'))
    
@app.route('/update', methods = ['POST'])
def update():
        my_data = Data.query.get(request.form.get('id'))
        my_data.name = request.form['name']
        my_data.email = request.form['email']
        my_data.phone = request.form['phone']

        db.session.commit()
        flash("Employee Updated Successfully")

        return redirect(url_for('index'))

@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Successfully")
 
    return redirect(url_for('index'))


@app.errorhandler(404)
def insufficient_permissions(e):
    """Render a 404 page."""
    return render_template("404.html"), 404

# run server
if __name__ == '__main__':
    app.run(host='127.0.0.1',debug=False)
