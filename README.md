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

**109** channels, **1,143,185.0** hours playtime between **2023-01-17** and **2024-11-18**


### playtime per genre (top 30)

    74489.9h 6.52% Nachrichten
    52294.0h 4.57% Verkaufsshow
    47636.4h 4.17% Krimiserie
    42054.4h 3.68% Werbesendung
    35705.0h 3.12% Dokureihe
    34086.9h 2.98% Dokusoap
    33408.6h 2.92% Regionalmagazin
    30036.8h 2.63% Dokumentation
    27038.5h 2.37% *unknown*
    21390.8h 1.87% Zeichentrickserie
    21079.1h 1.84% Infomercial
    20428.9h 1.79% Animationsserie
    16388.5h 1.43% Comedyserie
    15969.0h 1.40% Morgenmagazin
    15269.5h 1.34% Religionsmagazin
    15141.9h 1.32% Talkshow
    14315.5h 1.25% Magazin
    11289.4h 0.99% E-Sport
    11045.4h 0.97% Sitcom
    10339.0h 0.90% Wetterbericht
    10108.2h 0.88% Programmende
    10082.6h 0.88% Quiz
    10064.1h 0.88% Komödie
    8746.5h  0.77% Realityshow
    8658.2h  0.76% Politikmagazin
    8599.5h  0.75% Wissensmagazin
    8545.2h  0.75% Börsenmagazin
    7649.0h  0.67% Wirtschaftsmagazin
    7539.7h  0.66% Telenovela
    7493.0h  0.66% Dramaserie
