'''
### Comments / Markup

- square brackets are comments from the input operators
    - square brackets are anything not to be transformed for instance
        - [DD] [BP] [?]
        - [?] text unreadable
        - [BP, BLANK] blank pages
        - [DD] one or more pictures on that page, if text on the page then that is there
- parentheses, switch to a smaller type font in unicode
    - means for instance something in italics which in Tibetan is smaller font
    - anything requiring recitation has this all over (Lama Chupa)
- what happens when we get a text with bullet points?
    - for instance 1) which should be something like [1)]
    - in hyper-texting we use <e this is english><t this is tibetan>

'''
def test_markup():
    print('Testing markup / input operator comments')
    