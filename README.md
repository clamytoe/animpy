# Anime Python Research Tool (animpy)
> Just a little tool to make it easier for me to look up anime reviews.

![Python version][python-version]
[![Build Status][travis-image]][travis-url]
[![BCH compliance][bch-image]][bch-url]
[![GitHub issues][issues-image]][issues-url]
[![GitHub forks][fork-image]][fork-url]
[![GitHub Stars][stars-image]][stars-url]
[![License][license-image]][license-url]

My kids are big movie and anime buffs and are constantly asking me to look up shows to see if they are allowed to watch them. This of course takes time, more so when they bring you a list of them!

I initially wrote [Parental Guide (pguide)](https://github.com/clamytoe/pguide.git) but IMDb isn't really the greatest place to find reviews for anime. That lead me to start from scratch, so I created this one that scrapes [MyAnimeList](https://myanimelist.net) instead.

## How to set it all up
First of all, you should setup a virtual environment. I've included both a *requirements.txt* and an *environment.yml* file in order to make things easier. Perform the steps in the *Initial* and *Final* setups but do either the *Anaconda* or *Python* ones depending on which one you prefer to work with.

#### Initial setup
```bash
cd Projects
git clone https://github.com/clamytoe/animpy.git
cd animpy
```

#### Anaconda setup
```bash
conda env create
```

#### Regular Python setup
```bash
pip install -r requirements.txt
```

#### Final setup
```bash
activate animpy # or source activate animpy
pip install -e .
```

## How to run
Once that's all out of the way using the script is pretty straight forward. If you use the *--help* flag it will display the followign usage statement:

```bash
Usage: animpy [OPTIONS]

  Entry point for the script, requires the title of the Anime to look up.

  If a title isn't given from the command line, one will be asked for.
  :param title: String, the title of the show :return: None

Options:
  --show / --no-show   Toggles display search results on/off, defaults to off.
  -c, --count INTEGER  Number of search results to display, default is 5.
  -t, --title TEXT     Title of the Anime that you would like to look up, use
                       double-quotes.
  --help               Show this message and exit.
  ```

### Method #1
```bash
animpy
```

You will be prompted for the title.

### Method #2
```bash
animpy -t "D.Grey-man"

# or

animpy --show --count 2 --title "D.Gray-man"
```

## Sample run
> Notice that even if there is a type-o in the search term, the correct show is still found.

![sample run](img/start.png)

![search](img/review.png)

Just hitting the *ENTER* key will continue with the next screen. To exit enter an *n*.

[python-version]:https://img.shields.io/badge/python-3.6.3-brightgreen.svg
[travis-image]:https://travis-ci.org/clamytoe/animpy.svg?branch=master
[travis-url]:https://travis-ci.org/clamytoe/animpy
[bch-image]:https://bettercodehub.com/edge/badge/clamytoe/animpy?branch=master
[bch-url]:https://bettercodehub.com/
[issues-image]:https://img.shields.io/github/issues/clamytoe/animpy.svg
[issues-url]:https://github.com/clamytoe/animpy/issues
[fork-image]:https://img.shields.io/github/forks/clamytoe/animpy.svg
[fork-url]:https://github.com/clamytoe/animpy/network
[stars-image]:https://img.shields.io/github/stars/clamytoe/animpy.svg
[stars-url]:https://github.com/clamytoe/animpy/stargazers
[license-image]:https://img.shields.io/github/license/clamytoe/animpy.svg
[license-url]:https://github.com/clamytoe/animpy/blob/master/LICENSE
