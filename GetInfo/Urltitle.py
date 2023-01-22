from urltitle import URLTitleReader


def get(url):
    reader = URLTitleReader(verify_ssl=True)
    return reader.title(url)
