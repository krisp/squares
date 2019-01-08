from flask import Flask, render_template

app = Flask(__name__)

grid = [ [ '$5/sq', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J' ], 
         [ '0', None, None, None, None, None, None, None, None, None ],
         [ '1', None, 'Dave Mc', None, None, None, None, None, None, None ],
         [ '2', None, 'Dave Mc', None, None, None, None, None, None, None ],
         [ '3', None, None, None, None, None, None, None, None, None ],
         [ '4', None, None, None, None, None, None, None, None, None ],
         [ '5', None, None, None, None, None, None, None, None, None ],
         [ '6', None, None, None, None, None, None, None, None, None ],
         [ '7', None, None, None, None, None, None, None, 'Dave Mc', None ],
         [ '8', None, None, None, None, None, None, None, 'Dave Mc', None ],
         [ '9', None, None, None, None, None, None, None, None, None ]]

@app.route("/")
def index():
    return render_template("base.html",grid=grid)
