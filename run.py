import requests

from bs4 import BeautifulSoup
from settings import DATAFILE, OUTFILE


def main():
    html_doc = open(DATAFILE).read()
    soup = BeautifulSoup(html_doc, 'html.parser')

    with open(OUTFILE, 'w') as open_file:
        for _ in soup('dt'):
            if _.h3:
                print(_.h3.string)
                open_file.write('{}\n'.format(_.h3.string))

            elif _.a:
                print('|-{}'.format(_.a.string))
                try:
                    r = requests.get(_.a['href'])

                    if r.status_code == 404:
                        open_file.write('|-{}\n'.format(_.a.string))

                except requests.exceptions.ConnectionError:
                    open_file.write('|-{}\n'.format(_.a.string))


if __name__ == '__main__':
    main()
