
def txt_help(input_txt):
    """REturns expanded version of the string txt, which may contain texting
    abbreviations like 'brb' and 'lol'."""

    txt = input_txt.lower()
    if 'lol' in txt:
        txt = txt.replace('lol', 'laugh out loud')
    if 'brb' in txt:
        txt = txt.replace('brb', 'be right back')
    if 'af' in txt:
        txt = txt.replace('af ', 'as fuck ')
    if 'imo' in txt:
        txt = txt.replace('imo', 'in my opinion')
    # Mistakes when e.g. af is part of 'after' but fine for quick ex purpose.
    
    return txt

string = 'lol thats funny lol again'
string = txt_help(string)
print(string)

string = "lol i have to do something so brb but after that i'll test this" + \
        " algorithm which, iMO, looks good af. Again IMO and imo with different casing."
string = txt_help(string)
print(string)
