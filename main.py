'''
Input Text Processing


'''
# from process import test_file, test_filename, test_path, test_chars, \
#     test_lines, test_folios, test_markup
import process
# are we dropbox or event based processing?


# dropbox ------------------------------------------
# connect dropbox
# path
# filename
# --------------------------------------------------

# event --------------------------------------------
# monitor github
# must link to a catalog record for metadata
# --------------------------------------------------

# process ---------------------------------------------------

# file
# characters
# lines
# folios
# markup
# ----------------------------------------------------


# send to database ---------------------------------------

# control fields
# check author
# check subject

# check for match

# collation
# ---------------------------------------------------------


if __name__ == "__main__":
    import sys
    print("INPUT TEXT PROCESSING--------------------------")
    print(sys.path)
    print(process.__file__)
    process.test_file()
    process.test_filename()
    process.test_path()
    process.test_chars()
    process.test_lines()
    process.test_folios()
    process.test_markup()
    
