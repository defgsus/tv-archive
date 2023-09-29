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

**97** channels, **460,997.8** hours playtime between **2023-01-17** and **2023-09-30**


### playtime per genre (top 30)

    30451.5h 6.61% Nachrichten
    21941.5h 4.76% Verkaufsshow
    18623.3h 4.04% Krimiserie
    15549.8h 3.37% Werbesendung
    15197.5h 3.30% Dokureihe
    14073.7h 3.05% Dokusoap
    13310.2h 2.89% Regionalmagazin
    11573.9h 2.51% Dokumentation
    10974.1h 2.38% *unknown*
    8670.3h  1.88% Zeichentrickserie
    8408.4h  1.82% Infomercial
    8191.7h  1.78% Animationsserie
    7440.3h  1.61% Comedyserie
    6546.4h  1.42% Morgenmagazin
    6171.2h  1.34% Religionsmagazin
    6113.2h  1.33% Talkshow
    5742.6h  1.25% Magazin
    4868.7h  1.06% Programmende
    4555.9h  0.99% E-Sport
    4362.2h  0.95% Sitcom
    4327.6h  0.94% Wetterbericht
    4150.4h  0.90% Börsenmagazin
    3866.1h  0.84% Quiz
    3557.6h  0.77% Musikmagazin
    3546.3h  0.77% Komödie
    3492.1h  0.76% Wirtschaftsmagazin
    3463.6h  0.75% Wissensmagazin
    3291.2h  0.71% Telenovela
    3084.4h  0.67% Politikmagazin
    3006.3h  0.65% Reportagereihe
