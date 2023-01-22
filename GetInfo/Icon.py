import favicon
import requests.exceptions

icons = []
geticon = False


def get(url):
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
