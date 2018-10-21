from flask import Flask, request
from caesar import rotate_string

app = Flask (__name__)

app.config['DEBUG'] = True

form = """


<html>
    <head>
        <style>
        <form method ='POST'> {{

            background-color: #eee;
            padding:20px; 
            margin: 0 auto;
            width: 540px;
            font: 16px sans-serif;
            border-radius: 10px;

        }}
        textarea {{
            margin: 10px 0;
            width: 540px
            height: 120px;
        }}


        </style>


    </head>
    <body>
        
        <form method = "POST" action ="/">
        <label>
            Rotate by:
         <input type ="text" name = "rot" value ="0">
        </label>

        <br>
        <br>
        <label>
            <textarea name = "text">{0}</textarea>

        </label>
        <br>
        <input type="submit" value ="Submit Query">
    </body>







"""
@app.route("/")
def index():
    return form.format('')

@app.route("/", methods=['POST'])
def encrypt(): 
    rot = request.form["rot"]
    text = request.form["text"]
    rot = int(rot)
    rot = rotate_string(text, rot)
    return form.format(rot)
 


if __name__ == "__main__":
    app.run(host= '0.0.0.0')