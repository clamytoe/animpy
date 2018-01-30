from sys import exit
import click
import textwrap

from animpy.soup_utils import clear_screen, search, scrape_details


@click.command()
@click.option('-t', '--title', prompt='What would you like to search for?',
              help='Title of the Anime show that you would like to look up.')
def cli(title):
    """
    Entry point for the script, requires the title of the Anime to look up.

    If a title isn't given from the command line, one will be asked for.
    :param title: String, the title of the show
    :return: None
    """
    clear_screen()
    print(f'Searching for: {title}')
    hits = search(title)
    # used to display the search results, but since the first one is the most
    # relevant, that's the one picked for retrieval.
    url = hits[0][1]
    clear_screen()
    print(f'Retrieving information from: {url}\n')
    scrape_details(url)


def display_all_hits(results):
    """
    Displays the results from the search for the title
    :param results: List, search results
    :return: String, the url of the Anime chosen
    """
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


if __name__ == '__main__':
    cli()
