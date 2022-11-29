'''
Process file parameters

INPUTS: 
- input text file
- if coming from dropbox, also check matching META file


- Empty or doesn't exist
- is RTF, convert to TXT
- extension is missing

'''
import os

def handle_file(f):
    '''Check incoming file
    
    >>> handle_file()
    '''
    if os.path.isfile(f):
        if not os.stat(f).st_size == 0:
            file_extension = os.path.splitext(f)[-1]
    else:
        return False

    # convert RTF or if unknown return None
    # Now we can simply use == to check for equality, no need for wildcards.
    if file_extension.lower() == ".txt":
        return True
    elif file_extension.lower() == ".rtf":
        # convert to text file, I think we can just rename
        print('RTF!')
        return False
    else:
        print(f, "is an unknown file format.")
        return False



def empty_file(f):
    '''
    Returns True if empty
    '''
    return os.stat(f).st_size == 0

def correct_extension(f):
    ''' Check file extension, convert to proper file format if necessary
    >>> correct_extension('/var/www/readme.txt')
    True
    >>> correct_extension('/var/www/readme.rtf')
    False
    '''
    if os.path.isfile(f):
        file_extension = os.path.splitext(f)[-1]
    else:
        return None
    
    




    


def test_file():
    # assert that file exists
    # assert that file isn't empty
    # assert that file extension exists
    # assert that file type is txt
    
    print('Testing file')