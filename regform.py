#Using Flask
from flask import Flask,render_template,request
import mysql.connector

application = Flask(__name__)

@application.route("/")

def student():
    return render_template('reg.html')

@application.route("/result",methods=['POST','GET'])
def result():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="register"
    )

    mycursor=mydb.cursor()
    if request.method=="POST":
        signup=request.form

#pass this if this is the main function
if __name__ == '__main__':
  application.run(debug=True)