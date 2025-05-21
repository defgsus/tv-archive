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

**197** channels, **2,541,893*** programs, **1,672,239.7** hours playtime between **2023-01-17** and **2025-05-21**


### playtime per genre (top 30)

    433,745.1h 25.94% Serie
    276,985.6h 16.56% Magazin
    201,791.1h 12.07% Dokumentation
    153,161.0h 9.16%  Werbung
    152,428.1h 9.12%  Show
    116,966.9h 6.99%  Spielfilm
    115,439.5h 6.90%  Nachrichten
    85,717.5h  5.13%  Sport
    34,587.0h  2.07%  Reportage
    28,190.9h  1.69%  Musik
    13,137.6h  0.79%  Wetter
    13,012.7h  0.78%  Verschiedenes
    11,167.4h  0.67%  Programmende
    9,515.0h   0.57%  E-Sport
    6,164.2h   0.37%  Bericht
    5,400.6h   0.32%  Event
    3,541.9h   0.21%  *unknown*
    2,766.8h   0.17%  Videoclip
    2,045.6h   0.12%  Verkaufsshow
    2,014.2h   0.12%  Kurzfilm
    353.9h     0.02%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.02%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
