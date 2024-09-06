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

**109** channels, **1,032,507.4** hours playtime between **2023-01-17** and **2024-09-07**


### playtime per genre (top 30)

    67193.8h 6.51% Nachrichten
    48023.2h 4.65% Verkaufsshow
    42548.1h 4.12% Krimiserie
    37355.0h 3.62% Werbesendung
    32432.6h 3.14% Dokureihe
    31140.1h 3.02% Dokusoap
    30142.3h 2.92% Regionalmagazin
    26990.1h 2.61% Dokumentation
    24996.0h 2.42% *unknown*
    19152.3h 1.85% Zeichentrickserie
    18925.4h 1.83% Infomercial
    18501.0h 1.79% Animationsserie
    15125.3h 1.46% Comedyserie
    14482.2h 1.40% Morgenmagazin
    14032.9h 1.36% Religionsmagazin
    13595.9h 1.32% Magazin
    13562.9h 1.31% Talkshow
    10197.0h 0.99% E-Sport
    9877.4h  0.96% Sitcom
    9341.2h  0.90% Wetterbericht
    9263.7h  0.90% Programmende
    9070.0h  0.88% Komödie
    8922.5h  0.86% Quiz
    8213.5h  0.80% Börsenmagazin
    7728.0h  0.75% Politikmagazin
    7705.9h  0.75% Wissensmagazin
    7691.6h  0.74% Realityshow
    7033.7h  0.68% Wirtschaftsmagazin
    6804.4h  0.66% Telenovela
    6737.3h  0.65% Dramaserie
