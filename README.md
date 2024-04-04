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

**102** channels, **792,399.5** hours playtime between **2023-01-17** and **2024-04-05**


### playtime per genre (top 30)

    51564.5h 6.51% Nachrichten
    38023.9h 4.80% Verkaufsshow
    32267.1h 4.07% Krimiserie
    27608.5h 3.48% Werbesendung
    25176.6h 3.18% Dokureihe
    23866.1h 3.01% Dokusoap
    23015.3h 2.90% Regionalmagazin
    20533.3h 2.59% Dokumentation
    20349.5h 2.57% *unknown*
    14561.2h 1.84% Zeichentrickserie
    14373.9h 1.81% Infomercial
    14061.6h 1.77% Animationsserie
    12002.4h 1.51% Comedyserie
    11204.3h 1.41% Morgenmagazin
    10942.1h 1.38% Magazin
    10701.6h 1.35% Religionsmagazin
    10538.4h 1.33% Talkshow
    7804.4h  0.98% E-Sport
    7427.8h  0.94% Programmende
    7360.4h  0.93% Sitcom
    7032.4h  0.89% Wetterbericht
    7012.8h  0.89% Börsenmagazin
    6784.8h  0.86% Quiz
    6773.6h  0.85% Komödie
    5895.0h  0.74% Wissensmagazin
    5757.7h  0.73% Politikmagazin
    5700.1h  0.72% Realityshow
    5688.2h  0.72% Wirtschaftsmagazin
    5653.1h  0.71% Telenovela
    5342.4h  0.67% Musikmagazin
