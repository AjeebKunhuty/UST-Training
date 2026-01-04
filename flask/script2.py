from flask import *

app = Flask(__name__)

@app.route('/admin')
def admin():
    return 'admin'

@app.route('/librarian')
def librarian():
    return 'librarian'

@app.route('/student')
def student():
    return 'student'

@app.route('/user/<name>')
def user(name):
    if name in ['librarian', 'student', 'admin']:
        return redirect(url_for(name))
    else:
        return 'Invalid userid'
    
if __name__ == "__main__":
    app.run(debug=True)