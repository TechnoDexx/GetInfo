import favicon
import mechanize
from urltitle import URLTitleReader
import requests.exceptions



def get_icon(url):
    global icons
    global geticon
    try:
        icons = favicon.get(url)
    except requests.exceptions.HTTPError as err:
        print(err.strerror)
        icons = []
    # print(len(icons))
    if len(icons) > 0:
        geticon = True
    else:
        geticon = False

    return icons, geticon


def get_title(url):
    mech = mechanize.Browser()
    mech.set_handle_robots(False)
    mech.set_header('User-Agent',
                    'APIs-Google (+https://developers.google.com/webmasters/APIs-Google.html)')
    mech.open(url)
    return mech.title()


def urltitle_get_title(url):
    reader = URLTitleReader(verify_ssl=True)
    return reader.title(url)


