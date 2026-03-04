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

**198** channels, **4,249,245*** programs, **2,903,883.7** hours playtime between **2023-01-17** and **2026-03-04**


### playtime per genre (top 30)

    780,066.5h 26.86% Serie
    421,171.0h 14.50% Magazin
    368,453.3h 12.69% Dokumentation
    258,556.0h 8.90%  Spielfilm
    244,413.4h 8.42%  Show
    225,852.4h 7.78%  Werbung
    208,825.3h 7.19%  Sport
    162,452.3h 5.59%  Nachrichten
    65,150.1h  2.24%  Musik
    56,329.7h  1.94%  Reportage
    34,015.2h  1.17%  Verschiedenes
    18,788.9h  0.65%  Wetter
    11,167.4h  0.38%  Programmende
    9,515.0h   0.33%  E-Sport
    8,432.5h   0.29%  Bericht
    7,592.7h   0.26%  Event
    6,969.3h   0.24%  Kurzfilm
    6,064.4h   0.21%  Videoclip
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
    147.0h     0.01%  Wirtschaftsmagazin
