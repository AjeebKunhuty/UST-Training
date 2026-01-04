from flask import *  
app = Flask(__name__)  
  
@app.route('/user/<uname>')  
def message(uname):  
      return render_template('message.html',name=uname)  

@app.route('/table/<int:num>')
def table(num):
      return render_template('tableprint.html', n=num)

if __name__ == "__main__":
      app.run(debug=True)