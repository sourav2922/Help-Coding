from flask import *
from flask_sqlalchemy import SQLAlchemy  
  
app = Flask(__name__)  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///studio.sqlite3'  
app.config['SECRET_KEY'] = "secret key"  
  
db = SQLAlchemy(app)  
  
class studio(db.Model):  
   id = db.Column('studio_id', db.Integer, primary_key = True)
   email = db.Column(db.String(100))    
   password = db.Column(db.String(200))   
   message = db.Column(db.String(10))  
  
   def __init__(self, email, password,message):  
      self.email= email 
      self.password = password  
      self.message =message  
    
   
 
@app.route('/')  
def index():  
   return render_template('index.html')  

@app.route('/detail', methods = ['GET', 'POST'])  
def detail():  
   if request.method == 'POST':  
      if not request.form['email'] or not request.form['password'] or not request.form['message']:  
         flash('Please enter all the fields', 'error')  
      else:  
         detail = studio(request.form['email'], request.form['password'],  
            request.form['message'])  
           
         db.session.add(detail)  
         db.session.commit()  
         flash('Record was successfully added')  
         return redirect(url_for('detail'))  
   return render_template('index.html')
 
@app.route('/components')  
def components():   
   return render_template('components.html')  
  
if __name__ == '__main__':  
   db.create_all()
   app.run(debug = True,port=2000)  
   
   
   
   
   
   
   