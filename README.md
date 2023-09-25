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

**97** channels, **453,764.3** hours playtime between **2023-01-17** and **2023-09-26**


### playtime per genre (top 30)

    29927.7h 6.60% Nachrichten
    21572.2h 4.75% Verkaufsshow
    18332.9h 4.04% Krimiserie
    15315.4h 3.38% Werbesendung
    14950.2h 3.29% Dokureihe
    13830.1h 3.05% Dokusoap
    13057.4h 2.88% Regionalmagazin
    11405.5h 2.51% Dokumentation
    10800.5h 2.38% *unknown*
    8549.7h  1.88% Zeichentrickserie
    8276.4h  1.82% Infomercial
    8054.1h  1.77% Animationsserie
    7325.1h  1.61% Comedyserie
    6408.4h  1.41% Morgenmagazin
    6087.2h  1.34% Religionsmagazin
    6005.3h  1.32% Talkshow
    5656.6h  1.25% Magazin
    4813.2h  1.06% Programmende
    4468.6h  0.98% E-Sport
    4278.6h  0.94% Sitcom
    4261.8h  0.94% Wetterbericht
    4084.6h  0.90% Börsenmagazin
    3793.3h  0.84% Quiz
    3512.9h  0.77% Musikmagazin
    3496.8h  0.77% Komödie
    3429.7h  0.76% Wirtschaftsmagazin
    3400.6h  0.75% Wissensmagazin
    3210.6h  0.71% Telenovela
    3006.0h  0.66% Politikmagazin
    2969.9h  0.65% Reportagereihe
