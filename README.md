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

**109** channels, **1,096,172.6** hours playtime between **2023-01-17** and **2024-10-18**


### playtime per genre (top 30)

    71393.0h 6.51% Nachrichten
    50569.7h 4.61% Verkaufsshow
    45483.3h 4.15% Krimiserie
    40069.0h 3.66% Werbesendung
    34305.1h 3.13% Dokureihe
    32814.0h 2.99% Dokusoap
    32069.7h 2.93% Regionalmagazin
    28714.3h 2.62% Dokumentation
    26091.6h 2.38% *unknown*
    20435.0h 1.86% Zeichentrickserie
    20158.6h 1.84% Infomercial
    19607.0h 1.79% Animationsserie
    15887.4h 1.45% Comedyserie
    15352.8h 1.40% Morgenmagazin
    14800.3h 1.35% Religionsmagazin
    14480.4h 1.32% Talkshow
    13977.5h 1.28% Magazin
    10843.3h 0.99% E-Sport
    10555.2h 0.96% Sitcom
    9930.0h  0.91% Wetterbericht
    9747.3h  0.89% Programmende
    9624.9h  0.88% Quiz
    9603.1h  0.88% Komödie
    8411.3h  0.77% Börsenmagazin
    8349.5h  0.76% Realityshow
    8286.3h  0.76% Politikmagazin
    8242.1h  0.75% Wissensmagazin
    7390.7h  0.67% Wirtschaftsmagazin
    7236.1h  0.66% Telenovela
    7188.9h  0.66% Dramaserie
