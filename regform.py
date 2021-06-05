#Using Flask
from flask import Flask,render_template,request
import mysql.connector


application = Flask(__name__)

@application.route('/')

def student():
    return render_template('reg.html')

@application.route('/result',methods=['POST','GET'])
def result():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="register"
    )

    mycursor=mydb.cursor()
    if request.method=='POST':
        signup=request.form
        Name=signup['name']
        Class=signup['class']
        Math_mark=signup['math']
        Science_mark=signup['science']
        Social_mark=signup['social']
        English_mark=signup['english']
        Tamil_mark=signup['tamil']
        
        mycursor.execute("insert into reg(name,class,math,science,social,english,tamil)values(%s,%s,%s,%s,%s,%s,%s)",(Name,Class,Math_mark,Science_mark,Social_mark,English_mark,Tamil_mark))
        mydb.commit()
        mycursor.close()
        return "Registered Successfully"
#pass this if this is the main function
if __name__ == '__main__':
  application.run(debug=True)
