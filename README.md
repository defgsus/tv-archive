# Archive of TV-shows

Scraped directly from a german webpage, started at about mid-January 2023.

TV is not as important anymore but still, archiving the decisions of which programs to run at what time
becomes another puzzle piece in the revelation of mind-control.. 

Data is stored in [docs/data/YEAR/MONTH/YEAR-MONTH-DAY.ndjson](docs/data/) files. 
Each entry looks like this:

```python
{
  "id": "181043890", 
  "url": "https://www.hoerzu.de/tv-programm/south-park-kohle-an-den-chefkoch/bid_181043890/", 
  "channel": "Comedy Central", 
  "title": "South Park", 
  "date": "2023-01-17T05:15:00",    # probably Europe/Berlin timezone 
  "length": 25,                     # minutes 
  "sub_title": "Serie", 
  "genre": "Erwachsenen-Animationsserie", 
  "season": 2, 
  "episode": 14, 
  "year": 1998, 
  "countries": ["USA"],
}
```

## Statistics

**97** channels, **391,327.8** hours playtime between **2023-01-17** and **2023-08-22**


### playtime per genre (top 30)

    25858.4h 6.61% Nachrichten
    18440.2h 4.71% Verkaufsshow
    15848.4h 4.05% Krimiserie
    13189.1h 3.37% Werbesendung
    12964.9h 3.31% Dokureihe
    11828.6h 3.02% Dokusoap
    11212.5h 2.87% Regionalmagazin
    9895.6h  2.53% Dokumentation
    9507.9h  2.43% *unknown*
    7394.2h  1.89% Zeichentrickserie
    7146.0h  1.83% Infomercial
    6909.7h  1.77% Animationsserie
    6382.8h  1.63% Comedyserie
    5499.9h  1.41% Morgenmagazin
    5216.6h  1.33% Religionsmagazin
    5141.3h  1.31% Talkshow
    4871.8h  1.24% Magazin
    4329.8h  1.11% Programmende
    3875.3h  0.99% E-Sport
    3695.7h  0.94% Wetterbericht
    3663.5h  0.94% Sitcom
    3525.1h  0.90% Börsenmagazin
    3164.2h  0.81% Quiz
    3086.2h  0.79% Musikmagazin
    3035.8h  0.78% Komödie
    2982.0h  0.76% Wirtschaftsmagazin
    2929.8h  0.75% Wissensmagazin
    2723.8h  0.70% Telenovela
    2588.2h  0.66% Reportagereihe
    2521.5h  0.64% Sportmagazin
