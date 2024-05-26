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

**108** channels, **872,570.2** hours playtime between **2023-01-17** and **2024-05-27**


### playtime per genre (top 30)

    56963.9h 6.53% Nachrichten
    41438.8h 4.75% Verkaufsshow
    35488.6h 4.07% Krimiserie
    30602.0h 3.51% Werbesendung
    27494.6h 3.15% Dokureihe
    26378.8h 3.02% Dokusoap
    25333.7h 2.90% Regionalmagazin
    22656.3h 2.60% Dokumentation
    22138.5h 2.54% *unknown*
    16037.0h 1.84% Zeichentrickserie
    15872.3h 1.82% Infomercial
    15544.1h 1.78% Animationsserie
    13100.7h 1.50% Comedyserie
    12392.7h 1.42% Magazin
    12258.5h 1.40% Morgenmagazin
    11811.4h 1.35% Religionsmagazin
    11626.8h 1.33% Talkshow
    8643.4h  0.99% E-Sport
    8053.6h  0.92% Sitcom
    8048.1h  0.92% Programmende
    7756.5h  0.89% Wetterbericht
    7638.0h  0.88% Börsenmagazin
    7549.9h  0.87% Komödie
    7534.6h  0.86% Quiz
    6454.9h  0.74% Wissensmagazin
    6435.4h  0.74% Realityshow
    6394.4h  0.73% Politikmagazin
    6190.7h  0.71% Wirtschaftsmagazin
    6147.2h  0.70% Telenovela
    5776.9h  0.66% Musikmagazin
