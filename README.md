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

**197** channels, **2,656,723*** programs, **1,754,784.8** hours playtime between **2023-01-17** and **2025-06-09**


### playtime per genre (top 30)

    456,953.9h 26.04% Serie
    286,380.0h 16.32% Magazin
    212,639.8h 12.12% Dokumentation
    158,752.5h 9.05%  Show
    158,170.1h 9.01%  Werbung
    126,352.2h 7.20%  Spielfilm
    118,419.3h 6.75%  Nachrichten
    94,246.7h  5.37%  Sport
    36,010.1h  2.05%  Reportage
    31,023.1h  1.77%  Musik
    14,438.5h  0.82%  Verschiedenes
    13,501.2h  0.77%  Wetter
    11,167.4h  0.64%  Programmende
    9,515.0h   0.54%  E-Sport
    6,294.2h   0.36%  Bericht
    5,546.0h   0.32%  Event
    3,541.9h   0.20%  *unknown*
    2,957.3h   0.17%  Videoclip
    2,369.2h   0.14%  Kurzfilm
    2,045.6h   0.12%  Verkaufsshow
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
