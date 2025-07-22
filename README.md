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

**197** channels, **2,914,828*** programs, **1,940,584.8** hours playtime between **2023-01-17** and **2025-07-22**


### playtime per genre (top 30)

    509,372.4h 26.25% Serie
    308,135.6h 15.88% Magazin
    237,198.0h 12.22% Dokumentation
    172,786.8h 8.90%  Show
    169,427.1h 8.73%  Werbung
    147,038.6h 7.58%  Spielfilm
    125,188.8h 6.45%  Nachrichten
    112,931.7h 5.82%  Sport
    39,312.2h  2.03%  Reportage
    37,458.7h  1.93%  Musik
    17,552.1h  0.90%  Verschiedenes
    14,339.7h  0.74%  Wetter
    11,167.4h  0.58%  Programmende
    9,515.0h   0.49%  E-Sport
    6,677.1h   0.34%  Bericht
    5,835.5h   0.30%  Event
    3,541.9h   0.18%  *unknown*
    3,411.2h   0.18%  Videoclip
    3,188.6h   0.16%  Kurzfilm
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
