import os
os.system("pip3 install flask -U")
from flask import *

app = Flask(__name__)
@app.route("/")
def home(): return "Hello World"

if __name__ == '__main__' app.run("0.0.0.0",7251)
