from argparse import ArgumentParser
import sys
import json
from requests import RequestException

from SAScrapper import download_page_as_soup, get_courses_tables, tables_to_courses

SUPPORTED_PAGES = {
    'sdvx4': 'http://bemaniwiki.com/index.php?SOUND%20VOLTEX%20IV%20HEAVENLY%20HAVEN/SKILL%20ANALYZER',
    'sdvx5': 'http://bemaniwiki.com/index.php?SOUND%20VOLTEX%20VIVID%20WAVE/SKILL%20ANALYZER',
}

DEFAULT_PAGE = SUPPORTED_PAGES['sdvx5']

DESCRIPTION = '''\
Scraps Skill Analyzer SDVX courses from Bemaniwiki 2nd and outputs them as JSON.
'''

def parse_args():
    parser = ArgumentParser(description=DESCRIPTION)

    parser.add_argument('url', metavar='game or URL', type=str, nargs='?',
        default=DEFAULT_PAGE,
        help='Supported games: {}'.format(list(SUPPORTED_PAGES.keys())))
    parser.add_argument('--indent', metavar='N', type=int, default=2,
        help='Indent level for JSON output')
    parser.add_argument('--unicode-escapes', action='store_true',
        help='Escapes non-ASCII strings with unicode escapes')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    if args.url in SUPPORTED_PAGES:
        args.url = SUPPORTED_PAGES[args.url]
    try:
        page = download_page_as_soup(args.url)
    except RequestException as e:
        print(e)
        sys.exit(1)
    tables = get_courses_tables(page)
    courses = tables_to_courses(tables)
    print(json.dumps(
        courses,
        ensure_ascii=args.unicode_escapes,
        indent=args.indent,
        default=lambda x: x.__dict__)
    )
