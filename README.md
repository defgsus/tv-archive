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

**197** channels, **2,613,990*** programs, **1,724,358.7** hours playtime between **2023-01-17** and **2025-06-02**


### playtime per genre (top 30)

    448,270.5h 26.00% Serie
    282,897.6h 16.41% Magazin
    208,795.1h 12.11% Dokumentation
    156,373.1h 9.07%  Show
    156,306.4h 9.06%  Werbung
    122,904.3h 7.13%  Spielfilm
    117,315.8h 6.80%  Nachrichten
    91,188.8h  5.29%  Sport
    35,453.3h  2.06%  Reportage
    29,976.3h  1.74%  Musik
    13,907.6h  0.81%  Verschiedenes
    13,363.1h  0.77%  Wetter
    11,167.4h  0.65%  Programmende
    9,515.0h   0.55%  E-Sport
    6,257.6h   0.36%  Bericht
    5,494.9h   0.32%  Event
    3,541.9h   0.21%  *unknown*
    2,885.3h   0.17%  Videoclip
    2,238.1h   0.13%  Kurzfilm
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
