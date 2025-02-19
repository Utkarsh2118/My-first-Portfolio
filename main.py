from flask import Flask, render_template,request
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['portfolio']
app = Flask(__name__)

@app.route('/') 
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    doc = {
        'name': name,
        'email': email,
        'message': message
    }   
    
    db.contactus.insert_one(doc)
    return "Thank You for contacting us. We will get back to you soon."

if __name__ == '__main__':
    app.run(port=5000,debug=True)