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

**197** channels, **3,197,108*** programs, **2,142,592.6** hours playtime between **2023-01-17** and **2025-09-07**


### playtime per genre (top 30)

    567,040.9h 26.47% Serie
    331,390.8h 15.47% Magazin
    264,657.5h 12.35% Dokumentation
    187,428.8h 8.75%  Show
    181,442.4h 8.47%  Werbung
    169,376.5h 7.91%  Spielfilm
    132,918.9h 6.20%  Nachrichten
    132,609.6h 6.19%  Sport
    43,749.8h  2.04%  Musik
    43,007.8h  2.01%  Reportage
    21,854.0h  1.02%  Verschiedenes
    15,301.8h  0.71%  Wetter
    11,167.4h  0.52%  Programmende
    9,515.0h   0.44%  E-Sport
    6,824.8h   0.32%  Bericht
    6,176.8h   0.29%  Event
    4,054.8h   0.19%  Kurzfilm
    4,026.9h   0.19%  Videoclip
    3,541.9h   0.17%  *unknown*
    2,045.6h   0.10%  Verkaufsshow
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
