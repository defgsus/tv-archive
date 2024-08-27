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

**109** channels, **1,017,893.8** hours playtime between **2023-01-17** and **2024-08-28**


### playtime per genre (top 30)

    66219.0h 6.51% Nachrichten
    47338.4h 4.65% Verkaufsshow
    41874.0h 4.11% Krimiserie
    36727.6h 3.61% Werbesendung
    32003.1h 3.14% Dokureihe
    30766.0h 3.02% Dokusoap
    29663.4h 2.91% Regionalmagazin
    26582.5h 2.61% Dokumentation
    24800.2h 2.44% *unknown*
    18889.8h 1.86% Zeichentrickserie
    18645.4h 1.83% Infomercial
    18242.8h 1.79% Animationsserie
    14934.0h 1.47% Comedyserie
    14271.9h 1.40% Morgenmagazin
    13843.6h 1.36% Religionsmagazin
    13555.3h 1.33% Magazin
    13359.7h 1.31% Talkshow
    10053.9h 0.99% E-Sport
    9705.7h  0.95% Sitcom
    9199.8h  0.90% Wetterbericht
    9151.7h  0.90% Programmende
    8947.4h  0.88% Komödie
    8778.0h  0.86% Quiz
    8163.5h  0.80% Börsenmagazin
    7604.1h  0.75% Politikmagazin
    7595.9h  0.75% Wissensmagazin
    7542.3h  0.74% Realityshow
    6937.2h  0.68% Wirtschaftsmagazin
    6691.3h  0.66% Telenovela
    6636.6h  0.65% Dramaserie
