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

**197** channels, **2,897,185*** programs, **1,927,619.9** hours playtime between **2023-01-17** and **2025-07-19**


### playtime per genre (top 30)

    505,834.6h 26.24% Serie
    306,724.5h 15.91% Magazin
    235,438.7h 12.21% Dokumentation
    171,818.0h 8.91%  Show
    168,655.1h 8.75%  Werbung
    145,408.3h 7.54%  Spielfilm
    124,756.9h 6.47%  Nachrichten
    111,570.8h 5.79%  Sport
    39,089.4h  2.03%  Reportage
    37,020.2h  1.92%  Musik
    17,316.7h  0.90%  Verschiedenes
    14,286.2h  0.74%  Wetter
    11,167.4h  0.58%  Programmende
    9,515.0h   0.49%  E-Sport
    6,670.6h   0.35%  Bericht
    5,807.0h   0.30%  Event
    3,541.9h   0.18%  *unknown*
    3,370.6h   0.17%  Videoclip
    3,121.7h   0.16%  Kurzfilm
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
