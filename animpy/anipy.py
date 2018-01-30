from animpy.soup_utils import _soup


class Anipy:

    def __init__(self, title, type, episodes, status, year, genres, rating, url):
        self.title = title
        self.type = type
        self.episodes = episodes
        self.status = status
        self.year = year
        self.genres = genres
        self.rating = rating
        self.url = url

    def reviews(self):
        reviews = self.get_reviews()

    def get_reviews(self):
        reviews_url = f'{self.url}/reviews'
        soup = _soup(reviews_url)
        soup_section = soup.find('div', {'class': 'js-scrollfix-bottom-rel'})
        soup_reviews = soup_section.findall('div', {'class': 'spaceit textReadability word-break pt8 mt8'})
        print(soup_reviews[0].string)


"""
Type: TV
Episodes: 24
Status: Finished Airing
Aired: Apr 3, 2016 to Sep 25, 2016
Premiered: Spring 2016
Broadcast: Sundays at 01:55 (JST)
Producers: VAP, Nippon Television Network, Nippon Television Music, Takara Tomy A.R.T.S, CyberAgent, Forecast Communications
Licensors: Funimation
Studios: Brain's Base
Source: Original
Genres: Adventure, Fantasy
Duration: 23 min. per ep.
Rating: PG-13 - Teens 13 or older 
"""

