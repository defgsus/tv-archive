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

**197** channels, **3,423,027*** programs, **2,306,519.0** hours playtime between **2023-01-17** and **2025-10-15**


### playtime per genre (top 30)

    612,824.6h 26.57% Serie
    350,963.7h 15.22% Magazin
    287,113.2h 12.45% Dokumentation
    200,020.7h 8.67%  Show
    190,887.5h 8.28%  Werbung
    187,411.6h 8.13%  Spielfilm
    148,614.5h 6.44%  Sport
    139,236.5h 6.04%  Nachrichten
    48,998.8h  2.12%  Musik
    45,757.1h  1.98%  Reportage
    24,872.0h  1.08%  Verschiedenes
    16,050.9h  0.70%  Wetter
    11,167.4h  0.48%  Programmende
    9,515.0h   0.41%  E-Sport
    7,390.3h   0.32%  Bericht
    6,462.6h   0.28%  Event
    4,718.9h   0.20%  Kurzfilm
    4,464.4h   0.19%  Videoclip
    3,541.9h   0.15%  *unknown*
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
