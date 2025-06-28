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

**197** channels, **2,771,359*** programs, **1,837,140.4** hours playtime between **2023-01-17** and **2025-06-28**


### playtime per genre (top 30)

    480,145.8h 26.14% Serie
    296,032.0h 16.11% Magazin
    223,468.0h 12.16% Dokumentation
    165,124.1h 8.99%  Show
    163,250.5h 8.89%  Werbung
    135,496.2h 7.38%  Spielfilm
    121,420.8h 6.61%  Nachrichten
    102,357.5h 5.57%  Sport
    37,517.9h  2.04%  Reportage
    33,886.9h  1.84%  Musik
    15,811.0h  0.86%  Verschiedenes
    13,875.2h  0.76%  Wetter
    11,167.4h  0.61%  Programmende
    9,515.0h   0.52%  E-Sport
    6,480.3h   0.35%  Bericht
    5,665.4h   0.31%  Event
    3,541.9h   0.19%  *unknown*
    3,145.1h   0.17%  Videoclip
    2,733.0h   0.15%  Kurzfilm
    2,045.6h   0.11%  Verkaufsshow
    353.9h     0.02%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
