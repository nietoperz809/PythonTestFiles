from urllib.request import urlopen
from html.parser import HTMLParser
from timer import do_every
import time


class MyHTMLParser(HTMLParser):
    hit = False

    # def handle_starttag(self, tag, attrs):
    # print("Encountered a start tag:", tag, " - ", attrs)

    # def handle_endtag(self, tag):
    # print("Encountered an end tag :", tag)

    def handle_data(self, data):
        data = str(data).strip()
        if data == '':
            return
        if data == 'Robots':
            self.hit = True
            return
        if self.hit:
            if data.startswith('<!--//<![CDATA'):
                self.hit = False
                print ("------------------------------------")
                return
            print(data)
            # self.hit = False


def load_and_show():
    f = urlopen("http://www.denkforum.at/online/?type=registered")
    parser = MyHTMLParser()
    myfile = str(f.read(), 'utf-8')
    parser.feed(myfile)
    time.sleep(.3)


do_every(10, load_and_show)
