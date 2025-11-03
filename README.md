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

**197** channels, **3,536,739*** programs, **2,389,315.1** hours playtime between **2023-01-17** and **2025-11-03**


### playtime per genre (top 30)

    636,262.9h 26.63% Serie
    360,987.0h 15.11% Magazin
    297,915.0h 12.47% Dokumentation
    206,218.6h 8.63%  Show
    196,592.3h 8.23%  Spielfilm
    195,873.1h 8.20%  Werbung
    156,708.4h 6.56%  Sport
    142,445.3h 5.96%  Nachrichten
    51,817.9h  2.17%  Musik
    47,225.0h  1.98%  Reportage
    26,184.9h  1.10%  Verschiedenes
    16,413.6h  0.69%  Wetter
    11,167.4h  0.47%  Programmende
    9,515.0h   0.40%  E-Sport
    7,559.8h   0.32%  Bericht
    6,603.8h   0.28%  Event
    5,077.4h   0.21%  Kurzfilm
    4,692.3h   0.20%  Videoclip
    3,541.9h   0.15%  *unknown*
    2,045.6h   0.09%  Verkaufsshow
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
