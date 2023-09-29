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

**97** channels, **460,999.0** hours playtime between **2023-01-17** and **2023-09-30**


### playtime per genre (top 30)

    30453.3h 6.61% Nachrichten
    21938.9h 4.76% Verkaufsshow
    18623.1h 4.04% Krimiserie
    15551.8h 3.37% Werbesendung
    15195.2h 3.30% Dokureihe
    14073.3h 3.05% Dokusoap
    13310.4h 2.89% Regionalmagazin
    11571.7h 2.51% Dokumentation
    10977.4h 2.38% *unknown*
    8670.2h  1.88% Zeichentrickserie
    8408.4h  1.82% Infomercial
    8191.8h  1.78% Animationsserie
    7440.7h  1.61% Comedyserie
    6546.4h  1.42% Morgenmagazin
    6171.2h  1.34% Religionsmagazin
    6110.3h  1.33% Talkshow
    5743.3h  1.25% Magazin
    4868.8h  1.06% Programmende
    4555.7h  0.99% E-Sport
    4362.1h  0.95% Sitcom
    4326.7h  0.94% Wetterbericht
    4150.4h  0.90% Börsenmagazin
    3866.2h  0.84% Quiz
    3557.6h  0.77% Musikmagazin
    3546.3h  0.77% Komödie
    3491.9h  0.76% Wirtschaftsmagazin
    3463.7h  0.75% Wissensmagazin
    3291.2h  0.71% Telenovela
    3089.8h  0.67% Politikmagazin
    3006.0h  0.65% Reportagereihe
