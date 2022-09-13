from queue import Empty
import random
import os
from tkinter import image_names
from src.ims import InMemoryStorage
from flask import *
from datetime import timedelta
import sqlite3
import hashlib
from werkzeug.utils import secure_filename
import magic



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
    session.clear()
    return render_template('home.html', title='Home', app_version=version)


@app.route('/upload_image')
def upload_images():
    return render_template('upload_images.html', title='Upload', app_version=version)

@app.route('/guess', methods=['GET', 'POST'])
def guess():
    list = data.get_all_words_database()
    length = len(list)
    if(length == 0):
        flash("No Images are stored")
        return redirect("/word")
    if "word" not in session  and "number" not in session:
        print("Test")
        return render_template('guess.html', title='Guess', app_version=version)
    
    else:
        print("Nothing in session")

    #for i in range(length):
        #list[i] = list[i].replace("\n", "")

    if request.method == "POST":
        guesss_word = request.form['secretWord']
        right_word = session['word']
        guesss_word =  "('" + guesss_word + "',)"
        print(guesss_word + "Test")
        if guesss_word == right_word:
            flash("You guessed right.")
            return redirect('/')
        else:
            flash("You guessed wrong")
    return render_template('guess.html', title='Guess', app_version=version)

@app.route('/word', methods=['GET', 'POST'])
def word():
    
    if request.method == "POST":
        secret_word = request.form['secretWord']  # note the "name" attribute of the <input> we have in HTML
        secret_word = request.form['secretWord']
        image_file = request.files["image"]  # 'image' is the name of the input in HTML
        image_bytes = image_file.stream.read()  # actual image content
        image_content_type = image_file.content_type

        data.add_image(image_bytes, image_content_type)
        print("Imagae added added")
        data.add_word_database(secret_word)
        print("Word added")

        flash("Uploaded word " + repr(secret_word))

        list = data.get_all_words_database()

        return render_template('word.html', title='Guess', app_version=version, uploaded_image = image_file.filename)
        return redirect('/')  # redirect back to the main page
        
    return render_template('word.html', title='Guess', app_version=version)
    
@app.route('/image', methods=['GET'])
def get_image():
    list = data.get_all_words_database()
    lenght = len(list)
    lenght = str(lenght)
    f = open("images/" + lenght + ".png", "rb")
    file_bytes = f.read()
    mime = magic.Magic(mime=True)
    return Response(file_bytes, mimetype=mime.from_file("images/" + lenght + ".png"))

@app.route('/imageguess', methods=['GET'])
def get_image_guess():
    list = data.get_all_words_database()
    if "word" not in session  and "number" not in session:
        print("Nothing in session")
        rand = random.randint(1, len(list))
        randomword = str(list[rand-1])
        randomword = randomword.replace("\n", "")
        session['word'] = randomword
        session['number'] =  rand
        print(session['word'])

    
    else:
        lenght = session['number']
        lenght  = str(lenght)
        f = open("images/" + lenght + ".png", "rb")
        file_bytes = f.read()
        mime = magic.Magic(mime=True)
        print("Test")
        return Response(file_bytes, mimetype=mime.from_file("images/" + lenght + ".png"))
    lenght = session['number']
    lenght  = str(lenght)
    f = open("images/" + lenght + ".png", "rb")
    file_bytes = f.read()
    mime = magic.Magic(mime=True)
    return Response(file_bytes, mimetype=mime.from_file("images/" + lenght + ".png"))
