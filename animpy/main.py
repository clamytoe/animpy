from sys import exit
import click
import textwrap

from animpy.animpy import clear_screen, scrape_details, search, WIDTH


@click.command()
@click.option('--show/--no-show', default=False, help='Toggles display search results on/off, defaults to off.')
@click.option('-c', '--count', default=5, help='Number of search results to display, default is 5.')
@click.option('-t', '--title', prompt='What would you like to search for?',
              help='Title of the Anime that you would like to look up, use double-quotes.')
def cli(show, count, title):
    """
    Entry point for the script, requires the title of the Anime to look up.

    If a title isn't given from the command line, one will be asked for.
    :param show: Boolean, toggles display of search results on/off
    :param count: Integer, determines how many search results to display
    :param title: String, the title of the show
    :return: None
    """
    clear_screen()
    print(f'Searching for: {title}')
    hits = search(title, count)
    if hits:
        url = display_all_hits(hits) if show else hits[0][1]
        clear_screen()
        print(f'Retrieving information from: {url}\n')
        scrape_details(url)
    else:
        print(f'Sorry I was not about to find anything called "{title}"')


def display_all_hits(results):
    """
    Displays the results from the search for the title
    :param results: List, search results
    :return: String, the url of the Anime chosen
    """
    clear_screen()
    print('SEARCH RESULTS:')
    for i, title in enumerate(results):
        wrapped = textwrap.dedent(f'[{i}] {title[0]}:\n{title[2]}')
        print(f"\n{textwrap.fill(wrapped, initial_indent='', subsequent_indent='    ', width=WIDTH)}")
    try:
        choice = int(input('\nWhich one should I look up for you? '))
        if 0 <= choice < len(results):
            return results[choice][1]
        else:
            display_error()
    except ValueError:
        display_error()


def display_error():
    print('That is not a valid choice!')
    exit(0)


if __name__ == '__main__':
    cli()
