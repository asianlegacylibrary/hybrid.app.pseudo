'''
Parse filename from Dropbox

INPUTS: input text file, catalogued by Mixed Nuts

- example: CAT_TIBTITLE_ENGLISHTITLE_AUTHORTIB (DATE)_AUTHORENG.TXT
- underscores separate metadata
- double underscore if any are missing
- file names have spaces
- if file name ends with + (like +.TXT) then we have a meta file which is a companion TXT file designated by catalog number, example S00216M META.TXT
- Meta file
    - within the file it just continues exactly where we left off
- Catalog Number
    - typically there's a letter at the end (check level)
    - missing check level, or isn't a letter between A-E, N, M
- TITLE
    - Tibetan transliteration and English
    - check for missing titles
- AUTHOR
    - check for match in authority file
    - ACIP transliteration Tibetan, English
    - author dates: sometimes exist
    - check for missing author

'''


def test_filename():
    print('Testing filename')