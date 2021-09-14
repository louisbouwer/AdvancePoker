from flask import Flask
from flask import request, escape # jsonify

from game2 import Game2

# Instantiate an object game of class Game2
game = Game2()

# Setup Flask Web Application Framework
app = Flask(__name__)

# Setup Global Variables
# web_hand_html = " "

# Web Application Call
# game.index()
# Local Console Call
# game.web_play_game()

@app.route("/")
# WTF: Python debugger complain about capturing the class instance within the method
def index():
    
    print("This is inside the index method")

    # This is a Flask work around to be able to call the play_game methods
    cont_play = str(escape(request.args.get("Player", "")))
    print(f"cont_play : {cont_play}")
  
    if cont_play != "":
        web_hand_html = str(game.play_game())
    else:
        web_hand_html = "&emsp;Waiting for HTML response"
   
    print(f"web_hand_html : {web_hand_html}")
    return (""" <h1>Advance Poker</h1>
            &emsp;This is a 5 card draw Poker Bot. <br>
            &emsp;First you need to type your name: <br>
            <form action="" method="get">
            <label for="Player">&emsp;First Name:</label>
            <input type="text" name="Player" value="Player"><br><br>
            """ + web_hand_html + """ <br>
            &emsp;Click on the Continue button for the bot to draw 5 cars. <br><br>
            &emsp;<input type="submit" value="Continue">
            </form> 
            """
        )

# def new_func():
#    web_hand_hmtl = ""


# Startup the Flask Web Server
app.run(host='127.0.0.1', port=5000, debug=True)


