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

**197** channels, **2,584,200*** programs, **1,702,698.3** hours playtime between **2023-01-17** and **2025-05-28**


### playtime per genre (top 30)

    442,409.7h 25.98% Serie
    280,503.0h 16.47% Magazin
    205,801.1h 12.09% Dokumentation
    155,008.7h 9.10%  Werbung
    154,756.0h 9.09%  Show
    120,190.4h 7.06%  Spielfilm
    116,574.7h 6.85%  Nachrichten
    88,948.1h  5.22%  Sport
    35,091.2h  2.06%  Reportage
    29,233.4h  1.72%  Musik
    13,528.0h  0.79%  Verschiedenes
    13,266.8h  0.78%  Wetter
    11,167.4h  0.66%  Programmende
    9,515.0h   0.56%  E-Sport
    6,239.8h   0.37%  Bericht
    5,445.1h   0.32%  Event
    3,541.9h   0.21%  *unknown*
    2,834.3h   0.17%  Videoclip
    2,137.4h   0.13%  Kurzfilm
    2,045.6h   0.12%  Verkaufsshow
    353.9h     0.02%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.02%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
