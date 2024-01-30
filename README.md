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

**99** channels, **679,017.4** hours playtime between **2023-01-17** and **2024-01-31**


### playtime per genre (top 30)

    44265.3h 6.52% Nachrichten
    32528.2h 4.79% Verkaufsshow
    27348.0h 4.03% Krimiserie
    23238.7h 3.42% Werbesendung
    21986.0h 3.24% Dokureihe
    20356.5h 3.00% Dokusoap
    19613.2h 2.89% Regionalmagazin
    17551.4h 2.58% Dokumentation
    17056.2h 2.51% *unknown*
    12585.0h 1.85% Zeichentrickserie
    12337.1h 1.82% Infomercial
    11932.6h 1.76% Animationsserie
    10276.9h 1.51% Comedyserie
    9603.1h  1.41% Morgenmagazin
    9176.0h  1.35% Religionsmagazin
    9008.6h  1.33% Magazin
    8978.2h  1.32% Talkshow
    6680.2h  0.98% E-Sport
    6543.2h  0.96% Programmende
    6503.9h  0.96% Sitcom
    6089.2h  0.90% Wetterbericht
    6051.0h  0.89% Börsenmagazin
    5765.9h  0.85% Komödie
    5642.0h  0.83% Quiz
    5106.1h  0.75% Wissensmagazin
    4978.7h  0.73% Realityshow
    4952.5h  0.73% Wirtschaftsmagazin
    4831.7h  0.71% Telenovela
    4831.1h  0.71% Politikmagazin
    4767.0h  0.70% Musikmagazin
