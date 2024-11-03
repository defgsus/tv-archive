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

**109** channels, **1,121,522.8** hours playtime between **2023-01-17** and **2024-11-04**


### playtime per genre (top 30)

    73013.9h 6.51% Nachrichten
    51548.2h 4.60% Verkaufsshow
    46602.4h 4.16% Krimiserie
    41140.9h 3.67% Werbesendung
    35077.0h 3.13% Dokureihe
    33522.4h 2.99% Dokusoap
    32752.3h 2.92% Regionalmagazin
    29463.0h 2.63% Dokumentation
    26554.5h 2.37% *unknown*
    20973.3h 1.87% Zeichentrickserie
    20651.5h 1.84% Infomercial
    20055.8h 1.79% Animationsserie
    16133.5h 1.44% Comedyserie
    15677.0h 1.40% Morgenmagazin
    15058.5h 1.34% Religionsmagazin
    14848.6h 1.32% Talkshow
    14136.4h 1.26% Magazin
    11079.8h 0.99% E-Sport
    10811.1h 0.96% Sitcom
    10140.8h 0.90% Wetterbericht
    9940.9h  0.89% Programmende
    9904.5h  0.88% Komödie
    9838.6h  0.88% Quiz
    8545.6h  0.76% Realityshow
    8480.7h  0.76% Börsenmagazin
    8465.2h  0.75% Politikmagazin
    8427.2h  0.75% Wissensmagazin
    7529.0h  0.67% Wirtschaftsmagazin
    7384.5h  0.66% Telenovela
    7329.9h  0.65% Dramaserie
