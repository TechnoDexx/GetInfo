import mechanize


def get(url):
    mech = mechanize.Browser()
    mech.set_handle_robots(False)
    mech.set_header('User-Agent',
                    'APIs-Google (+https://developers.google.com/webmasters/APIs-Google.html)')
    mech.open(url)
    return mech.title()
