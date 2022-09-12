from src.ims import InMemoryStorage
from flask import *
from datetime import timedelta
import sqlite3
import hashlib
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.secret_key = 'c1155c6a351e49eba15c00ce577b259e'
version = 1.0
data = InMemoryStorage()



def Hash(String):
    bytes_string = bytes(String, 'utf-8')
    hashed_string = hashlib.md5(bytes_string)
    return hashed_string.hexdigest()

@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html', title='Home', app_version=version)


@app.route('/upload_image')
def upload_images():
    return render_template('upload_images.html', title='Upload', app_version=version)

@app.route('/guess', methods=['GET', 'POST'])
def guess():
    list = data.get_all_words()
    length = len(list)
    for i in range(length):
        list[i] = list[i].replace("\n", "")
    if len(list) == 0:
        flash("No Words uploaded yet.")
    session['word'] 
    if request.method == "POST":
        guesss_word = request.form['secretWord']  # note the "name" attribute of the <input> we have in HTML
        print(guesss_word)
        print(list)
        if guesss_word in list:
            flash("You guessed right.")
            print("right") 
            #return redirect('/')  # redirect back to the main page
    return render_template('guess.html', title='Guess', app_version=version)

@app.route('/word', methods=['GET', 'POST'])
def word():
    
    if request.method == "POST":
        secret_word = request.form['secretWord']  # note the "name" attribute of the <input> we have in HTML
        data.add_word(secret_word)
        flash("Uploaded word " + repr(secret_word))
        list = data.get_all_words()
        length = len(list)
        for i in range(length):
            flash(list[i])
        return redirect('/')  # redirect back to the main page
    return render_template('word.html', title='Guess', app_version=version)



