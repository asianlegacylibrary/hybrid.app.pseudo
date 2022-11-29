'''
File path

- SUBJECT
    - first we look in the authority file
        - Tibetan transliteration and English, separated by underscore
    - check for similar subject found, different Tibetan phrasing for same thing
    - check for subject missing, files without folder
'''

def test_path():
    # check for missing subject (files without folder)
    print('Testing file path')