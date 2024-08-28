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

**109** channels, **1,019,843.9** hours playtime between **2023-01-17** and **2024-08-29**


### playtime per genre (top 30)

    66353.4h 6.51% Nachrichten
    47486.4h 4.66% Verkaufsshow
    41956.3h 4.11% Krimiserie
    36810.3h 3.61% Werbesendung
    32061.9h 3.14% Dokureihe
    30804.8h 3.02% Dokusoap
    29752.5h 2.92% Regionalmagazin
    26654.0h 2.61% Dokumentation
    24825.1h 2.43% *unknown*
    18922.0h 1.86% Zeichentrickserie
    18682.1h 1.83% Infomercial
    18281.6h 1.79% Animationsserie
    14953.1h 1.47% Comedyserie
    14306.8h 1.40% Morgenmagazin
    13864.2h 1.36% Religionsmagazin
    13559.4h 1.33% Magazin
    13388.8h 1.31% Talkshow
    10071.3h 0.99% E-Sport
    9735.2h  0.95% Sitcom
    9218.0h  0.90% Wetterbericht
    9165.6h  0.90% Programmende
    8964.1h  0.88% Komödie
    8794.2h  0.86% Quiz
    8171.1h  0.80% Börsenmagazin
    7625.4h  0.75% Politikmagazin
    7609.4h  0.75% Wissensmagazin
    7567.0h  0.74% Realityshow
    6952.6h  0.68% Wirtschaftsmagazin
    6711.2h  0.66% Telenovela
    6658.4h  0.65% Dramaserie
