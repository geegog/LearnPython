import urllib


def read_file():
    f = open("profanity", "r")
    content = f.read()
    f.close()
    return check(content)


def check(text):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text)
    output = connection.read()
    connection.close()
    return output


def run():
    if read_file() == 'true':
        print 'There is a profanity word in the text provided'
    else:
        print 'Text is clean'


run()
