from flask import Flask
from flask_sqlalchemy import SQLAlchemy 


app = Flask (__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resolutions.db' #database file
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

class Resolution(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each resolution
    content = db.Column(db.String(200), nullable=False)  # Resolution text
    completed = db.Column(db.Boolean, default=False)  # Track if resolution is done

def to_dict(self):
        return {
            "id": self.id,
            "content": self.content,
            "completed": self.completed
        }
with app.app_context():
    db.create_all()



@app.route("/ add-resolution", methods=)
def index():
    return "Hello World"

if __name__ in "__main__":
    app.run(debug=True)


    

