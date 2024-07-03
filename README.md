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

**109** channels, **932,512.8** hours playtime between **2023-01-17** and **2024-07-04**


### playtime per genre (top 30)

    60859.8h 6.53% Nachrichten
    43690.4h 4.69% Verkaufsshow
    38112.6h 4.09% Krimiserie
    33127.2h 3.55% Werbesendung
    29328.1h 3.15% Dokureihe
    28218.9h 3.03% Dokusoap
    27129.4h 2.91% Regionalmagazin
    24186.8h 2.59% Dokumentation
    23310.8h 2.50% *unknown*
    17185.9h 1.84% Zeichentrickserie
    17013.5h 1.82% Infomercial
    16668.8h 1.79% Animationsserie
    13908.5h 1.49% Comedyserie
    13310.3h 1.43% Magazin
    13148.0h 1.41% Morgenmagazin
    12635.2h 1.35% Religionsmagazin
    12376.8h 1.33% Talkshow
    9228.2h  0.99% E-Sport
    8762.9h  0.94% Sitcom
    8503.9h  0.91% Programmende
    8338.1h  0.89% Wetterbericht
    8088.1h  0.87% Komödie
    8060.7h  0.86% Quiz
    7886.5h  0.85% Börsenmagazin
    7030.8h  0.75% Politikmagazin
    6947.4h  0.75% Realityshow
    6931.9h  0.74% Wissensmagazin
    6508.8h  0.70% Wirtschaftsmagazin
    6357.6h  0.68% Telenovela
    6088.0h  0.65% Musikmagazin
