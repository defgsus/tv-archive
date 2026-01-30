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

**198** channels, **4,057,084*** programs, **2,766,636.7** hours playtime between **2023-01-17** and **2026-01-30**


### playtime per genre (top 30)

    740,502.9h 26.77% Serie
    404,766.9h 14.63% Magazin
    349,232.8h 12.62% Dokumentation
    243,673.9h 8.81%  Spielfilm
    233,749.9h 8.45%  Show
    217,749.2h 7.87%  Werbung
    194,262.8h 7.02%  Sport
    157,002.2h 5.67%  Nachrichten
    62,628.2h  2.26%  Musik
    53,775.0h  1.94%  Reportage
    32,413.0h  1.17%  Verschiedenes
    18,189.4h  0.66%  Wetter
    11,167.4h  0.40%  Programmende
    9,515.0h   0.34%  E-Sport
    8,191.5h   0.30%  Bericht
    7,313.7h   0.26%  Event
    6,717.3h   0.24%  Kurzfilm
    5,717.2h   0.21%  Videoclip
    3,541.9h   0.13%  *unknown*
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
