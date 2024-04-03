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

**102** channels, **790,624.2** hours playtime between **2023-01-17** and **2024-04-04**


### playtime per genre (top 30)

    51427.7h 6.50% Nachrichten
    37937.2h 4.80% Verkaufsshow
    32172.7h 4.07% Krimiserie
    27546.0h 3.48% Werbesendung
    25148.1h 3.18% Dokureihe
    23813.6h 3.01% Dokusoap
    22950.9h 2.90% Regionalmagazin
    20485.9h 2.59% Dokumentation
    20304.2h 2.57% *unknown*
    14532.0h 1.84% Zeichentrickserie
    14340.4h 1.81% Infomercial
    14031.4h 1.77% Animationsserie
    11967.0h 1.51% Comedyserie
    11173.4h 1.41% Morgenmagazin
    10902.5h 1.38% Magazin
    10682.0h 1.35% Religionsmagazin
    10519.3h 1.33% Talkshow
    7797.2h  0.99% E-Sport
    7414.2h  0.94% Programmende
    7347.0h  0.93% Sitcom
    7015.9h  0.89% Wetterbericht
    7002.6h  0.89% Börsenmagazin
    6773.5h  0.86% Komödie
    6762.0h  0.86% Quiz
    5879.8h  0.74% Wissensmagazin
    5741.1h  0.73% Politikmagazin
    5682.8h  0.72% Realityshow
    5672.0h  0.72% Wirtschaftsmagazin
    5635.5h  0.71% Telenovela
    5336.8h  0.68% Musikmagazin
