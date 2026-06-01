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

**200** channels, **4,758,009*** programs, **3,267,486.6** hours playtime between **2023-01-17** and **2026-06-01**


### playtime per genre (top 30)

    886,561.1h 27.13% Serie
    463,491.1h 14.18% Magazin
    420,257.9h 12.86% Dokumentation
    298,190.4h 9.13%  Spielfilm
    271,573.8h 8.31%  Show
    247,026.4h 7.56%  Werbung
    246,606.6h 7.55%  Sport
    178,437.5h 5.46%  Nachrichten
    72,038.2h  2.20%  Musik
    63,035.7h  1.93%  Reportage
    37,566.6h  1.15%  Verschiedenes
    20,474.7h  0.63%  Wetter
    11,167.4h  0.34%  Programmende
    9,515.0h   0.29%  E-Sport
    9,090.4h   0.28%  Bericht
    8,300.4h   0.25%  Event
    7,120.4h   0.22%  Kurzfilm
    6,964.8h   0.21%  Videoclip
    3,541.9h   0.11%  *unknown*
    2,045.6h   0.06%  Verkaufsshow
    353.9h     0.01%  Eishockey
    299.8h     0.01%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.00%  Fußball
    147.0h     0.00%  Wirtschaftsmagazin
