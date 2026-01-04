from flask import *

app = Flask(__name__)  

@app.route('/login',methods = ['POST'])  
def loginPost():  
      uname=request.form['uname']  
      password=request.form['pass']  
      if uname=="Ajeeb" and password=="UST":  
          return "Welcome %s" %uname  
      else:
           return render_template('loginhtml.html')    # renders from template folder
      
@app.route('/login',methods = ['GET'])  
def loginGet():  
      # arguments passed as part of url
      #   http://localhost:5000/login?uname=Ajeeb&pass=UST
      uname=request.args.get('uname')  
      passwrd=request.args.get('pass')  
      if uname=="Ajeeb" and passwrd=="UST":  
          return "Welcome %s" %uname  
      else:
           return render_template('loginhtml.html')    # renders from templates folder
      

if __name__ == '__main__':  
   app.run(debug = True)  