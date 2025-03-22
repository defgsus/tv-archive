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

**195** channels, **2,184,499*** programs, **1,413,918.2** hours playtime between **2023-01-17** and **2025-03-22**


### playtime per genre (top 30)

    361,518.3h 25.57% Serie
    247,082.4h 17.48% Magazin
    167,740.3h 11.86% Dokumentation
    137,099.3h 9.70%  Werbung
    132,604.9h 9.38%  Show
    105,654.4h 7.47%  Nachrichten
    88,018.6h  6.23%  Spielfilm
    59,810.8h  4.23%  Sport
    29,995.5h  2.12%  Reportage
    19,376.2h  1.37%  Musik
    12,069.2h  0.85%  Wetter
    11,167.4h  0.79%  Programmende
    9,515.0h   0.67%  E-Sport
    8,540.0h   0.60%  Verschiedenes
    5,720.0h   0.40%  Bericht
    4,912.1h   0.35%  Event
    3,541.9h   0.25%  *unknown*
    2,183.1h   0.15%  Videoclip
    2,045.6h   0.14%  Verkaufsshow
    865.6h     0.06%  Kurzfilm
    353.9h     0.03%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.02%  Darts
    232.8h     0.02%  Handball
    219.5h     0.02%  Dokureihe
    212.4h     0.02%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
