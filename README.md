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

**197** channels, **3,292,696*** programs, **2,211,719.9** hours playtime between **2023-01-17** and **2025-09-23**


### playtime per genre (top 30)

    586,407.8h 26.51% Serie
    339,639.9h 15.36% Magazin
    274,068.1h 12.39% Dokumentation
    192,752.2h 8.72%  Show
    185,448.4h 8.38%  Werbung
    176,890.8h 8.00%  Spielfilm
    139,554.3h 6.31%  Sport
    135,569.9h 6.13%  Nachrichten
    45,844.0h  2.07%  Musik
    44,205.5h  2.00%  Reportage
    23,144.9h  1.05%  Verschiedenes
    15,616.2h  0.71%  Wetter
    11,167.4h  0.50%  Programmende
    9,515.0h   0.43%  E-Sport
    6,982.1h   0.32%  Bericht
    6,316.3h   0.29%  Event
    4,336.6h   0.20%  Kurzfilm
    4,212.0h   0.19%  Videoclip
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
