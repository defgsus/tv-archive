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

**198** channels, **4,335,202*** programs, **2,965,108.0** hours playtime between **2023-01-17** and **2026-03-19**


### playtime per genre (top 30)

    798,317.1h 26.92% Serie
    428,756.5h 14.46% Magazin
    376,944.6h 12.71% Dokumentation
    264,785.2h 8.93%  Spielfilm
    249,100.3h 8.40%  Show
    229,468.9h 7.74%  Werbung
    215,048.3h 7.25%  Sport
    164,997.2h 5.56%  Nachrichten
    66,297.2h  2.24%  Musik
    57,494.3h  1.94%  Reportage
    34,601.9h  1.17%  Verschiedenes
    19,064.7h  0.64%  Wetter
    11,167.4h  0.38%  Programmende
    9,515.0h   0.32%  E-Sport
    8,572.8h   0.29%  Bericht
    7,709.8h   0.26%  Event
    6,982.2h   0.24%  Kurzfilm
    6,216.3h   0.21%  Videoclip
    3,541.9h   0.12%  *unknown*
    2,045.6h   0.07%  Verkaufsshow
    353.9h     0.01%  Eishockey
    299.8h     0.01%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.00%  Wirtschaftsmagazin
