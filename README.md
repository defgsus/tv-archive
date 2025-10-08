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

**197** channels, **3,381,252*** programs, **2,276,279.5** hours playtime between **2023-01-17** and **2025-10-08**


### playtime per genre (top 30)

    604,295.2h 26.55% Serie
    347,311.2h 15.26% Magazin
    283,116.0h 12.44% Dokumentation
    197,680.8h 8.68%  Show
    189,042.7h 8.30%  Werbung
    184,106.5h 8.09%  Spielfilm
    145,702.9h 6.40%  Sport
    138,036.6h 6.06%  Nachrichten
    47,961.8h  2.11%  Musik
    45,288.0h  1.99%  Reportage
    24,386.7h  1.07%  Verschiedenes
    15,908.7h  0.70%  Wetter
    11,167.4h  0.49%  Programmende
    9,515.0h   0.42%  E-Sport
    7,323.8h   0.32%  Bericht
    6,413.0h   0.28%  Event
    4,593.0h   0.20%  Kurzfilm
    4,381.8h   0.19%  Videoclip
    3,541.9h   0.16%  *unknown*
    2,045.6h   0.09%  Verkaufsshow
    353.9h     0.02%  Eishockey
    299.8h     0.01%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
