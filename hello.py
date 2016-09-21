from flask import Flask

#variable; doesn't need to be called app
app = Flask(__name__)

#helpful links to all pages
tail = """
<br><br>
Helpful links! <br>
<a href = "/"> Main page </a> <br>
<a href = "/polite"> Polite page </a> <br>
<a href = "/pic"> Cool Page </a>
"""

#main page
@app.route("/")
def mainPage():
    #basic opening line
    return "Well hello there" + tail

#page found at /polite
@app.route("/polite")
def politePage():
    #manners are important
    return "It's a pleasure to see you" + tail

#page found at /pic
@app.route("/pic")
def picPage():
    #this is an adorable dog, and therefore belongs here
    return "<img src = \"http://media-cache-ak0.pinimg.com/736x/27/2f/de/272fdefd243176d37d25220e826def4b.jpg\">" + tail
    
app.run()
