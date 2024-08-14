import pyshorteners


def shortLink(link):

    short = pyshorteners.Shortener()
    x = short.tinyurl.short(link)

    return x