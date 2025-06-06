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

**197** channels, **2,638,918*** programs, **1,741,710.1** hours playtime between **2023-01-17** and **2025-06-06**


### playtime per genre (top 30)

    453,485.2h 26.04% Serie
    284,995.8h 16.36% Magazin
    210,967.0h 12.11% Dokumentation
    157,688.6h 9.05%  Show
    157,387.0h 9.04%  Werbung
    124,506.4h 7.15%  Spielfilm
    118,029.1h 6.78%  Nachrichten
    92,872.3h  5.33%  Sport
    35,791.4h  2.05%  Reportage
    30,555.7h  1.75%  Musik
    14,215.1h  0.82%  Verschiedenes
    13,447.7h  0.77%  Wetter
    11,167.4h  0.64%  Programmende
    9,515.0h   0.55%  E-Sport
    6,284.2h   0.36%  Bericht
    5,516.7h   0.32%  Event
    3,541.9h   0.20%  *unknown*
    2,926.1h   0.17%  Videoclip
    2,311.1h   0.13%  Kurzfilm
    2,045.6h   0.12%  Verkaufsshow
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
