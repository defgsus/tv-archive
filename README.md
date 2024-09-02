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

**109** channels, **1,026,987.0** hours playtime between **2023-01-17** and **2024-09-03**


### playtime per genre (top 30)

    66793.6h 6.50% Nachrichten
    47771.2h 4.65% Verkaufsshow
    42260.7h 4.12% Krimiserie
    37127.0h 3.62% Werbesendung
    32278.1h 3.14% Dokureihe
    30972.4h 3.02% Dokusoap
    29928.7h 2.91% Regionalmagazin
    26843.9h 2.61% Dokumentation
    24934.3h 2.43% *unknown*
    19050.4h 1.85% Zeichentrickserie
    18823.0h 1.83% Infomercial
    18404.3h 1.79% Animationsserie
    15039.5h 1.46% Comedyserie
    14376.9h 1.40% Morgenmagazin
    13964.7h 1.36% Religionsmagazin
    13577.8h 1.32% Magazin
    13490.5h 1.31% Talkshow
    10144.2h 0.99% E-Sport
    9812.2h  0.96% Sitcom
    9287.0h  0.90% Wetterbericht
    9221.6h  0.90% Programmende
    9044.1h  0.88% Komödie
    8862.0h  0.86% Quiz
    8186.4h  0.80% Börsenmagazin
    7673.2h  0.75% Politikmagazin
    7663.9h  0.75% Wissensmagazin
    7635.7h  0.74% Realityshow
    6992.2h  0.68% Wirtschaftsmagazin
    6749.8h  0.66% Telenovela
    6689.1h  0.65% Dramaserie
