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

**200** channels, **4,774,962*** programs, **3,279,391.8** hours playtime between **2023-01-17** and **2026-06-04**


### playtime per genre (top 30)

    890,323.1h 27.15% Serie
    464,934.8h 14.18% Magazin
    422,013.2h 12.87% Dokumentation
    299,307.9h 9.13%  Spielfilm
    272,380.0h 8.31%  Show
    247,731.1h 7.55%  Sport
    247,653.7h 7.55%  Werbung
    179,068.3h 5.46%  Nachrichten
    72,224.8h  2.20%  Musik
    63,226.1h  1.93%  Reportage
    37,697.4h  1.15%  Verschiedenes
    20,535.0h  0.63%  Wetter
    11,167.4h  0.34%  Programmende
    9,515.0h   0.29%  E-Sport
    9,107.5h   0.28%  Bericht
    8,317.0h   0.25%  Event
    7,122.8h   0.22%  Kurzfilm
    6,998.4h   0.21%  Videoclip
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
