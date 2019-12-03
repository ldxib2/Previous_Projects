
import urllib.request
import urllib.error
from urllib.request import urlopen
from urllib.request import urlretrieve
from urllib.parse import urlparse
import logging

# Exercise 1 - HTTP connection and retrieving first 200 characters of html code

def open_url(url):

    try:
        weburl = urlopen(url)
    except urllib.error.HTTPError as e:
        print('HTTPError: {}'.format(e.code))
    except urllib.error.URLError as e:
        print('URLError: {}'.format(e.reason))
    except urllib.error.ContentTooShortError as e:
           print('ContentTooShortError: {}'.format(e.reason))
    else:
        sourcecode = weburl.read(200)
        print(sourcecode)

# Testing
open_url("https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol")

# Made up page
open_url("https://www.randompagethathopefullydoesnotexist.com")



# Exercise 2

def init_log(file_name, file_mode = "a", level = logging.DEBUG,
             format = '%(asctime)s %(levelname)s: %(message)s.',
             date_format = "%d.%m.%Y %H:%M:%S"):

# creating and initialising a custom log file
    logging.basicConfig(filename=file_name, filemode=file_mode, level=level, format=format, datefmt=date_format)

# similar function to before except using log files
def open_urllog(url):
    try:
        weburl = urlopen(url)
    except urllib.error.HTTPError as e:
        logging.error('HTTPError: {}'.format(e.code))
    except urllib.error.URLError as e:
        logging.error('URLError: {}'.format(e.reason))
    except urllib.error.ContentTooShortError as e:
        logging.error('ContentTooShortError: {}'.format(e.reason))
    else:
        sourcecode = weburl.read(200)
        print(sourcecode)

logging.shutdown()

# Tests ran

init_log('/Users/admin/PycharmProjects/icss/Protocol.log')

open_urllog('https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol')
open_urllog('https://en.wikipedia.org/wiki/Hypertext_Transformers__is_a_terrible_franchise_Protocol')
logging.shutdown()
open_urllog('https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol')

# Exercise 3 downloading files

def download_file(url, path):
    parse = urlparse(url)
    if parse.path[-3:] == "txt":
        try:
            urlretrieve(url, path)
        except urllib.error.HTTPError as e:
            logging.error('HTTPError: {}'.format(e.code))
        except urllib.error.URLError as e:
            logging.error('URLError: {}'.format(e.reason))
        except urllib.error.ContentTooShortError as e:
            logging.error('ContentTooShortError: {}'.format(e.reason))
    else:
        logging.error("No text file found at given URL, download aborted!")

# Correct test
download_file("https://ia802707.us.archive.org/1/items/macbeth02264gut/0ws3410.txt", "/Users/admin/PycharmProjects/icss/macbeth.txt")

# Incorrect test
download_file("https://www.wikipedia.org", "/Users/admin/PycharmProjects/icss/macbeth.txt")