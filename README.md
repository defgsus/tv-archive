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

**97** channels, **482,472.2** hours playtime between **2023-01-17** and **2023-10-12**


### playtime per genre (top 30)

    31797.2h 6.59% Nachrichten
    23004.2h 4.77% Verkaufsshow
    19414.0h 4.02% Krimiserie
    16300.1h 3.38% Werbesendung
    15906.0h 3.30% Dokureihe
    14752.0h 3.06% Dokusoap
    13900.5h 2.88% Regionalmagazin
    12191.0h 2.53% Dokumentation
    11540.0h 2.39% *unknown*
    9053.9h  1.88% Zeichentrickserie
    8788.0h  1.82% Infomercial
    8587.0h  1.78% Animationsserie
    7729.3h  1.60% Comedyserie
    6821.8h  1.41% Morgenmagazin
    6478.0h  1.34% Religionsmagazin
    6407.4h  1.33% Talkshow
    6009.2h  1.25% Magazin
    5029.0h  1.04% Programmende
    4754.4h  0.99% E-Sport
    4591.2h  0.95% Sitcom
    4506.3h  0.93% Wetterbericht
    4364.2h  0.90% Börsenmagazin
    4054.0h  0.84% Quiz
    3739.8h  0.78% Komödie
    3681.0h  0.76% Musikmagazin
    3639.6h  0.75% Wirtschaftsmagazin
    3635.5h  0.75% Wissensmagazin
    3438.7h  0.71% Telenovela
    3281.1h  0.68% Politikmagazin
    3135.3h  0.65% Reportagereihe
