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

**197** channels, **2,422,192*** programs, **1,585,749.6** hours playtime between **2023-01-17** and **2025-05-01**


### playtime per genre (top 30)

    409,216.5h 25.81% Serie
    267,083.4h 16.84% Magazin
    190,661.7h 12.02% Dokumentation
    147,848.3h 9.32%  Werbung
    145,782.4h 9.19%  Show
    112,202.5h 7.08%  Nachrichten
    107,450.3h 6.78%  Spielfilm
    76,862.2h  4.85%  Sport
    32,984.0h  2.08%  Reportage
    25,186.8h  1.59%  Musik
    12,792.4h  0.81%  Wetter
    11,518.6h  0.73%  Verschiedenes
    11,167.4h  0.70%  Programmende
    9,515.0h   0.60%  E-Sport
    5,977.1h   0.38%  Bericht
    5,247.1h   0.33%  Event
    3,541.9h   0.22%  *unknown*
    2,570.9h   0.16%  Videoclip
    2,045.6h   0.13%  Verkaufsshow
    1,634.7h   0.10%  Kurzfilm
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
