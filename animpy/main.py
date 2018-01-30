from sys import exit
import click
import textwrap

from animpy.soup_utils import clear_screen, search, scrape_details


@click.command()
@click.option('-t', '--title', prompt='What would you like to search for?',
              help='Title of the Anime show that you would like to look up.')
def cli(title):
    clear_screen()
    print(f'Searching for: {title}')
    hits = search(title)
    # choice = display_all_hits(hits) if hits else display_none(title)
    # get_details(choice)
    url = hits[0][1]
    clear_screen()
    print(f'Retrieving information from: {url}\n')
    get_details(url)


def display_all_hits(results):
    clear_screen()
    print('--')
    for i, title in enumerate(results):
        wrapped = textwrap.dedent(f'[{i}] {title[0]}:\n{title[2]}')
        print(textwrap.fill(wrapped, initial_indent='', subsequent_indent='    ', width=110))
    print('**')
    choice = int(input('Which one should I look up for you? '))
    return results[choice][1]


def display_none(term):
    print(f"Sorry, couldn't find anything about {term}")
    exit(0)


def get_details(choice):
    scrape_details(choice)

if __name__ == '__main__':
    cli()
