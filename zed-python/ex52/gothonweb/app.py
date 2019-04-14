from flask import Flask, session, redirect, url_for, escape
from flask import render_template
from flask import request
from gothonweb import planisphere

#create app an instance of Flask
app = Flask(__name__)

#create root url which rediects to /game url
@app.route("/")
def index():
    #this is used for setting up the session with planisphere START value
    #breakpoint()
    session['room_name'] = planisphere.START
    return redirect(url_for("game"))

@app.route("/game", methods=['GET', 'POST'])
def game():
    #room name is taken from session name
    #breakpoint()
    room_name = session.get('room_name')
    if request.method == 'GET':
        if room_name:
            # if room name exist create a variable room with values from load room.
            room = planisphere.load_room(room_name)
            return render_template("show_room.html", room=room)
        else:
            return render_template("you_died.html")
    else:
        # getting the 'action' value from show room html
        action = request.form.get('action')
        if room_name and action:
            room = planisphere.load_room(room_name)
            next_room = room.go(action)
            if not next_room:
                session['room_name'] = planisphere.name_room(room)
            else:
                session['room_name'] = planisphere.name_room(next_room)
        return redirect(url_for("game"))

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'




if __name__ == "__main__":
    app.run()
