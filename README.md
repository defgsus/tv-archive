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

**109** channels, **1,028,824.4** hours playtime between **2023-01-17** and **2024-09-04**


### playtime per genre (top 30)

    66928.3h 6.51% Nachrichten
    47844.1h 4.65% Verkaufsshow
    42375.8h 4.12% Krimiserie
    37200.7h 3.62% Werbesendung
    32325.7h 3.14% Dokureihe
    31032.7h 3.02% Dokusoap
    30007.0h 2.92% Regionalmagazin
    26887.0h 2.61% Dokumentation
    24957.0h 2.43% *unknown*
    19085.7h 1.86% Zeichentrickserie
    18855.8h 1.83% Infomercial
    18436.8h 1.79% Animationsserie
    15068.8h 1.46% Comedyserie
    14411.8h 1.40% Morgenmagazin
    13990.8h 1.36% Religionsmagazin
    13585.1h 1.32% Magazin
    13506.0h 1.31% Talkshow
    10167.9h 0.99% E-Sport
    9831.0h  0.96% Sitcom
    9305.5h  0.90% Wetterbericht
    9235.4h  0.90% Programmende
    9050.7h  0.88% Komödie
    8878.5h  0.86% Quiz
    8195.5h  0.80% Börsenmagazin
    7694.5h  0.75% Politikmagazin
    7680.1h  0.75% Wissensmagazin
    7650.9h  0.74% Realityshow
    7003.2h  0.68% Wirtschaftsmagazin
    6766.6h  0.66% Telenovela
    6697.6h  0.65% Dramaserie
