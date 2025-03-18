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

**195** channels, **2,160,147*** programs, **1,396,828.6** hours playtime between **2023-01-17** and **2025-03-18**


### playtime per genre (top 30)

    356,538.7h 25.52% Serie
    244,947.0h 17.54% Magazin
    165,637.8h 11.86% Dokumentation
    136,001.7h 9.74%  Werbung
    131,266.6h 9.40%  Show
    104,913.4h 7.51%  Nachrichten
    86,423.8h  6.19%  Spielfilm
    58,166.9h  4.16%  Sport
    29,682.6h  2.13%  Reportage
    18,786.8h  1.34%  Musik
    11,992.6h  0.86%  Wetter
    11,167.4h  0.80%  Programmende
    9,515.0h   0.68%  E-Sport
    8,228.4h   0.59%  Verschiedenes
    5,698.1h   0.41%  Bericht
    4,893.9h   0.35%  Event
    3,541.9h   0.25%  *unknown*
    2,143.5h   0.15%  Videoclip
    2,045.6h   0.15%  Verkaufsshow
    779.5h     0.06%  Kurzfilm
    353.9h     0.03%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.02%  Darts
    232.8h     0.02%  Handball
    219.5h     0.02%  Dokureihe
    212.4h     0.02%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
