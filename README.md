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

**109** channels, **1,021,682.4** hours playtime between **2023-01-17** and **2024-08-31**


### playtime per genre (top 30)

    66483.4h 6.51% Nachrichten
    47559.1h 4.65% Verkaufsshow
    42053.1h 4.12% Krimiserie
    36887.2h 3.61% Werbesendung
    32104.1h 3.14% Dokureihe
    30854.2h 3.02% Dokusoap
    29817.2h 2.92% Regionalmagazin
    26682.5h 2.61% Dokumentation
    24864.0h 2.43% *unknown*
    18953.2h 1.86% Zeichentrickserie
    18717.6h 1.83% Infomercial
    18316.6h 1.79% Animationsserie
    14982.0h 1.47% Comedyserie
    14341.7h 1.40% Morgenmagazin
    13885.7h 1.36% Religionsmagazin
    13561.7h 1.33% Magazin
    13419.8h 1.31% Talkshow
    10088.8h 0.99% E-Sport
    9755.0h  0.95% Sitcom
    9235.5h  0.90% Wetterbericht
    9179.4h  0.90% Programmende
    8973.1h  0.88% Komödie
    8814.8h  0.86% Quiz
    8180.1h  0.80% Börsenmagazin
    7637.1h  0.75% Politikmagazin
    7619.7h  0.75% Wissensmagazin
    7593.2h  0.74% Realityshow
    6968.8h  0.68% Wirtschaftsmagazin
    6732.4h  0.66% Telenovela
    6670.0h  0.65% Dramaserie
