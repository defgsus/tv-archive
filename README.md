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

**197** channels, **2,992,787*** programs, **1,996,640.7** hours playtime between **2023-01-17** and **2025-08-04**


### playtime per genre (top 30)

    525,242.9h 26.31% Serie
    314,638.8h 15.76% Magazin
    244,857.5h 12.26% Dokumentation
    176,775.2h 8.85%  Show
    172,573.2h 8.64%  Werbung
    153,289.1h 7.68%  Spielfilm
    127,345.2h 6.38%  Nachrichten
    118,569.6h 5.94%  Sport
    40,312.1h  2.02%  Reportage
    39,322.4h  1.97%  Musik
    18,709.0h  0.94%  Verschiedenes
    14,593.3h  0.73%  Wetter
    11,167.4h  0.56%  Programmende
    9,515.0h   0.48%  E-Sport
    6,724.8h   0.34%  Bericht
    5,934.7h   0.30%  Event
    3,584.8h   0.18%  Videoclip
    3,541.9h   0.18%  *unknown*
    3,437.2h   0.17%  Kurzfilm
    2,045.6h   0.10%  Verkaufsshow
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
