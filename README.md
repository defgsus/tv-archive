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

**109** channels, **1,007,004.3** hours playtime between **2023-01-17** and **2024-08-21**


### playtime per genre (top 30)

    65501.0h 6.50% Nachrichten
    46898.4h 4.66% Verkaufsshow
    41365.2h 4.11% Krimiserie
    36247.9h 3.60% Werbesendung
    31663.9h 3.14% Dokureihe
    30454.5h 3.02% Dokusoap
    29355.2h 2.92% Regionalmagazin
    26272.3h 2.61% Dokumentation
    24593.1h 2.44% *unknown*
    18675.9h 1.85% Zeichentrickserie
    18438.7h 1.83% Infomercial
    18032.3h 1.79% Animationsserie
    14801.4h 1.47% Comedyserie
    14118.1h 1.40% Morgenmagazin
    13693.0h 1.36% Religionsmagazin
    13526.2h 1.34% Magazin
    13202.7h 1.31% Talkshow
    9959.7h  0.99% E-Sport
    9580.7h  0.95% Sitcom
    9084.0h  0.90% Wetterbericht
    9069.3h  0.90% Programmende
    8845.5h  0.88% Komödie
    8673.0h  0.86% Quiz
    8128.1h  0.81% Börsenmagazin
    7531.7h  0.75% Politikmagazin
    7497.9h  0.74% Wissensmagazin
    7455.8h  0.74% Realityshow
    6874.8h  0.68% Wirtschaftsmagazin
    6615.3h  0.66% Telenovela
    6554.4h  0.65% Dramaserie
