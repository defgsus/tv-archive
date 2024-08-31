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

**109** channels, **1,023,477.4** hours playtime between **2023-01-17** and **2024-09-01**


### playtime per genre (top 30)

    66569.8h 6.50% Nachrichten
    47628.9h 4.65% Verkaufsshow
    42119.8h 4.12% Krimiserie
    36966.4h 3.61% Werbesendung
    32179.0h 3.14% Dokureihe
    30894.6h 3.02% Dokusoap
    29843.6h 2.92% Regionalmagazin
    26757.7h 2.61% Dokumentation
    24887.0h 2.43% *unknown*
    18988.8h 1.86% Zeichentrickserie
    18754.9h 1.83% Infomercial
    18345.5h 1.79% Animationsserie
    14997.2h 1.47% Comedyserie
    14345.7h 1.40% Morgenmagazin
    13905.2h 1.36% Religionsmagazin
    13568.3h 1.33% Magazin
    13441.4h 1.31% Talkshow
    10115.4h 0.99% E-Sport
    9774.0h  0.95% Sitcom
    9251.6h  0.90% Wetterbericht
    9194.1h  0.90% Programmende
    9007.4h  0.88% Komödie
    8825.4h  0.86% Quiz
    8180.0h  0.80% Börsenmagazin
    7638.0h  0.75% Politikmagazin
    7632.4h  0.75% Wissensmagazin
    7607.9h  0.74% Realityshow
    6972.3h  0.68% Wirtschaftsmagazin
    6733.1h  0.66% Telenovela
    6672.9h  0.65% Dramaserie
