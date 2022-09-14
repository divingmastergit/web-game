from src.ims import InMemoryStorage

def test_is_empty():
    storage = InMemoryStorage()  # create empty storage
    assert storage.get_all_words_database != None