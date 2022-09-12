from pathlib import Path
class InMemoryStorage:
    
    def __init__(self):
        spot = Path("words.txt")
        if spot.is_file():
            print("File existes")
        else:
            f = open("words.txt", "a")
            f.close()

    def add_word(self, secret_word: str) -> None:
        """ Store a secret word."""
        f = open("words.txt", "a")
        f.write(secret_word + "\n")
        f.close()



    def get_all_words(self):
        f = open("words.txt", "r")
        storage = f.readlines()
        f.close()
        return storage