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

**198** channels, **4,068,960*** programs, **2,775,126.5** hours playtime between **2023-01-17** and **2026-02-01**


### playtime per genre (top 30)

    742,890.8h 26.77% Serie
    405,689.6h 14.62% Magazin
    350,365.5h 12.63% Dokumentation
    244,773.5h 8.82%  Spielfilm
    234,429.7h 8.45%  Show
    218,249.9h 7.86%  Werbung
    195,180.0h 7.03%  Sport
    157,321.0h 5.67%  Nachrichten
    62,786.2h  2.26%  Musik
    53,902.4h  1.94%  Reportage
    32,542.6h  1.17%  Verschiedenes
    18,225.5h  0.66%  Wetter
    11,167.4h  0.40%  Programmende
    9,515.0h   0.34%  E-Sport
    8,202.4h   0.30%  Bericht
    7,327.4h   0.26%  Event
    6,750.0h   0.24%  Kurzfilm
    5,739.3h   0.21%  Videoclip
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
