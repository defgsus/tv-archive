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

**195** channels, **2,309,883*** programs, **1,503,880.9** hours playtime between **2023-01-17** and **2025-04-12**


### playtime per genre (top 30)

    386,662.3h 25.71% Serie
    257,713.5h 17.14% Magazin
    179,648.6h 11.95% Dokumentation
    142,810.2h 9.50%  Werbung
    139,687.0h 9.29%  Show
    109,180.2h 7.26%  Nachrichten
    97,498.6h  6.48%  Spielfilm
    68,789.1h  4.57%  Sport
    31,548.8h  2.10%  Reportage
    22,435.7h  1.49%  Musik
    12,448.9h  0.83%  Wetter
    11,167.4h  0.74%  Programmende
    10,124.3h  0.67%  Verschiedenes
    9,515.0h   0.63%  E-Sport
    5,893.6h   0.39%  Bericht
    5,051.6h   0.34%  Event
    3,541.9h   0.24%  *unknown*
    2,381.7h   0.16%  Videoclip
    2,045.6h   0.14%  Verkaufsshow
    1,276.8h   0.08%  Kurzfilm
    353.9h     0.02%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.02%  Darts
    232.8h     0.02%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
