from flask import Flask
from flask import render_template
from flask import request
import sys
app = Flask(__name__)

"""retorna el template index"""
@app.route("/")
def index():
    return render_template('index.html')

"""recibe la expresion y la evalua"""
@app.route("/calcular",methods=['POST'])
def calcular():
    try:
        expresion = request.form['expr']
        return str(eval(expresion))
    except Exception as e:
        return "error"
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(sys.argv[1]))
