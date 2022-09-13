from importlib.resources import path
import os
import sqlite3
from turtle import st
class InMemoryStorage:
    #def __init__(self):
        #spot = Path("words.txt")
        #if spot.is_file():
          #  print("File existes")
       # else:
       #     f = open("words.txt", "a")
      #      f.close()

    #def add_word(self, secret_word: str) -> None:
    #    """ Store a secret word."""
   #     f = open("words.txt", "a")
   #     f.write(secret_word + "\n")
   #     f.close()



   # def get_all_words(self):
  #      f = open("words.txt", "r")
   #     storage = f.readlines()
   #     f.close()
   #     return storage

    def __init__(self):
        if os.path.exists("words.db"):
            print("Database already exists")
        else:
            con01 = sqlite3.connect("words.db")
            cursor = con01.cursor()
            cursor.execute("CREATE TABLE WORDS (Word text);")
            con01.close()
            print("Database has been created sucessful")
        if(os.path.isdir("images")):
            print("Directory already exists.")
        else:
            os.path.os.mkdir("images")


    def add_word_database(self, secret_word: str) -> None:
            con = sqlite3.connect("words.db")
            cur = con.cursor()
            cur.execute("INSERT INTO WORDS (Word) VALUES(?);", (secret_word,))
            con.commit()
            con.close()
            print("Word has been added")
    
    
    def get_all_words_database(self) -> list[str]:
        con = sqlite3.connect("words.db")
        cur = con.cursor()
        cur.execute("SELECT Word FROM Words")
        words = cur.fetchall()
        return words
    
    def add_image(self, file: bytes, file_type: str):
        file_type = file_type.replace("image/", "")
        file_name = len(os.listdir("images")) + 1
        file_name = str(file_name)
        f = open("images/" + file_name + ".png" , "wb")
        f.write(file)
            