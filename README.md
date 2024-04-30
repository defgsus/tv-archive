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

**102** channels, **834,712.1** hours playtime between **2023-01-17** and **2024-05-01**


### playtime per genre (top 30)

    54418.4h 6.52% Nachrichten
    39967.6h 4.79% Verkaufsshow
    34003.1h 4.07% Krimiserie
    29180.2h 3.50% Werbesendung
    26355.6h 3.16% Dokureihe
    25180.0h 3.02% Dokusoap
    24283.2h 2.91% Regionalmagazin
    21621.7h 2.59% Dokumentation
    21324.0h 2.55% *unknown*
    15334.5h 1.84% Zeichentrickserie
    15168.4h 1.82% Infomercial
    14864.1h 1.78% Animationsserie
    12623.6h 1.51% Comedyserie
    11770.9h 1.41% Morgenmagazin
    11731.7h 1.41% Magazin
    11277.0h 1.35% Religionsmagazin
    11114.9h 1.33% Talkshow
    8267.9h  0.99% E-Sport
    7757.6h  0.93% Programmende
    7674.1h  0.92% Sitcom
    7410.8h  0.89% Wetterbericht
    7347.1h  0.88% Börsenmagazin
    7217.4h  0.86% Quiz
    7109.8h  0.85% Komödie
    6174.4h  0.74% Wissensmagazin
    6119.8h  0.73% Politikmagazin
    6063.9h  0.73% Realityshow
    5964.1h  0.71% Telenovela
    5963.6h  0.71% Wirtschaftsmagazin
    5559.9h  0.67% Musikmagazin
