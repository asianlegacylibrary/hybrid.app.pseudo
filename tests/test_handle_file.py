# test_handle_file.py
from process.handle_file import  handle_file_empty, handle_file_extension

def test_handle_file_empty():
    
    files = {
        "tests/texts/text.txt": True, 
        "tests/texts/empty_text.txt": False
        }

    for k, v in files.items():
        print(k, v)
        assert handle_file_empty(k) == v
    


def test_handle_file_extension():
        
    files = {
        '/var/www/bar.txt': True,
        '/var/www/foo.bar': False,
        '/var/www/TXT.RTF': False,
        '/var/www': False
    }

    for k, v in files.items():
        assert handle_file_extension(k) == v
