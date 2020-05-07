from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://az@localhost:5432/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database
db = SQLAlchemy(app)

# Table
class Person(db.Model):
  __tablename__ = 'persons'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)
  def __repr__(self):
    return f'<Person ID: {self.id}, Name: {self.name}'


db.create_all()

'''
from app import db, Person
person = Person(name='Amy')
db.session.add(person)
db.session.commit()
'''
@app.route('/')
def index():
  person = Person.query.all()[-1]
  return f'Hello {person.name}'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)