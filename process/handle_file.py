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

def handle_file(f):
    '''Check incoming file

    Return file if it passes, else return None
    
    
    '''

    # assert that file exists and is not empty
    if os.path.isfile(f):
        if not os.stat(f).st_size == 0:
            file_extension = os.path.splitext(f)[-1]
    else:
        return None

    # assert that file type is text, if RTF just rename suffix
    if file_extension.lower() == ".txt":
        return True
    elif file_extension.lower() == ".rtf":
        # convert to text file, I think we can just rename
        print('RTF!')
        return False
    # elif missing extension
    # try just adding the TXT extension
    else:
        print(f, "is an unknown file format.")
        return False


def test_file(f):
        # assert that file exists
        # assert that file isn't empty
        # assert that file extension exists
        # assert that file type is txt
        # if dropbox:
            # if META
            # send META through test
    print(type(f))
    if isinstance(f, list):
        # loop over the list
        for s in f:
            print(s)
    elif isinstance(f, str):
        # single item
        print(f)
    else:
        print('Module requires file or list of files')

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        test_file(sys.argv[1])
    else:
        print('Please supply file or list of files to test module...')
        