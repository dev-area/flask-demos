from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/enternew')
def new_student():
   return render_template('salary.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         id = request.form['id']
         name = request.form['name']
         city = request.form['city']
         salary = request.form['salary']
         if id == '':
             err = True
             return render_template("result.html", msg = "ID is empty")
         if name == '':
             err = True
             return render_template("result.html", msg = "Name is empty")
         if city == '':
             err = True
             return render_template("result.html", msg = "City is empty")
         if salary == '':
             err = True
             return render_template("result.html", msg = "Salary is empty")
         err = False
         with sql.connect("database.db") as con:
            cur = con.cursor()
            
            cur.execute('''INSERT INTO salarydata (id,name,city,salary) 
               VALUES (?,?,?,?)''',(id,name,city,salary) )
            
            con.commit()
            msg = "Record with ID : {} Created".format(id)
      except:
         con.rollback()
         msg = "Create Database First"
      
      finally:
          if not err:
             return render_template("result.html",msg = msg)
             con.close()

@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   try:
       cur.execute("select * from salarydata")
       
       rows = cur.fetchall();
       return render_template("list.html",rows = rows)
   except:
       return render_template("result.html",msg = "Database Not Found")

@app.route('/delete')
def delete_database():
    import os
    os.remove('./database.db')
    return render_template("result.html",msg = "Deletion Success")
    
@app.route('/create_db')
def create_db():
    conn = sql.connect('database.db')
    print ("Opened database successfully")
    
    try:
        conn.execute('CREATE TABLE salarydata (id TEXT NOT NULL, name TEXT NOT NULL, city TEXT NOT NULL, salary TEXT NOT NULL)')
        msg = "Table created successfully"
        conn.close()
    except:
        msg = "Delete Database First"
        conn.close()
    return render_template("result.html",msg = msg)

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug = True, port=5804)
