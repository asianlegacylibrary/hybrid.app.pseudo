'''
Process file parameters

INPUTS: 
- input text file
- if coming from dropbox, also check matching META file

Check file:
- is it empty or doesn't exist
- is it RTF, convert to TXT
- extension is missing

'''
import os


def handle_file_extension(f):
    return os.path.splitext(f)[-1] == '.txt'

def handle_file_empty(f):
    e = False
    if os.path.isfile(f):
        if not os.stat(f).st_size == 0:
            e = True
    return e 

def check_file():

    # assert that file exists and is not empty
    

    # assert that file type is text, if RTF just rename suffix

    # if dropbox:
        # if META
        # send META through test

    print('checking file')


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 0:
        print('Please supply file or list of files to test module...')
        