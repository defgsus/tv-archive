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

**97** channels, **455,571.3** hours playtime between **2023-01-17** and **2023-09-27**


### playtime per genre (top 30)

    30059.2h 6.60% Nachrichten
    21660.6h 4.75% Verkaufsshow
    18421.8h 4.04% Krimiserie
    15376.0h 3.38% Werbesendung
    15027.0h 3.30% Dokureihe
    13889.4h 3.05% Dokusoap
    13122.2h 2.88% Regionalmagazin
    11448.9h 2.51% Dokumentation
    10844.3h 2.38% *unknown*
    8579.6h  1.88% Zeichentrickserie
    8308.9h  1.82% Infomercial
    8088.1h  1.78% Animationsserie
    7354.0h  1.61% Comedyserie
    6443.1h  1.41% Morgenmagazin
    6109.0h  1.34% Religionsmagazin
    6032.5h  1.32% Talkshow
    5678.0h  1.25% Magazin
    4825.4h  1.06% Programmende
    4493.7h  0.99% E-Sport
    4295.3h  0.94% Sitcom
    4277.6h  0.94% Wetterbericht
    4113.2h  0.90% Börsenmagazin
    3808.3h  0.84% Quiz
    3525.4h  0.77% Musikmagazin
    3503.1h  0.77% Komödie
    3443.8h  0.76% Wirtschaftsmagazin
    3416.3h  0.75% Wissensmagazin
    3230.4h  0.71% Telenovela
    3026.8h  0.66% Politikmagazin
    2978.5h  0.65% Reportagereihe
