import pyperclip as p
othertext=''
while True:
    text=p.paste()
    if not text==othertext:
        othertext=text
        print(text)
    else:
        othertext=othertext
