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

**197** channels, **2,493,870*** programs, **1,637,650.2** hours playtime between **2023-01-17** and **2025-05-13**


### playtime per genre (top 30)

    423,879.2h 25.88% Serie
    272,987.0h 16.67% Magazin
    197,410.8h 12.05% Dokumentation
    151,006.5h 9.22%  Werbung
    149,734.9h 9.14%  Show
    114,126.4h 6.97%  Nachrichten
    113,354.6h 6.92%  Spielfilm
    82,141.1h  5.02%  Sport
    33,921.5h  2.07%  Reportage
    26,985.5h  1.65%  Musik
    13,006.5h  0.79%  Wetter
    12,409.3h  0.76%  Verschiedenes
    11,167.4h  0.68%  Programmende
    9,515.0h   0.58%  E-Sport
    6,066.4h   0.37%  Bericht
    5,343.2h   0.33%  Event
    3,541.9h   0.22%  *unknown*
    2,686.9h   0.16%  Videoclip
    2,045.6h   0.12%  Verkaufsshow
    1,859.6h   0.11%  Kurzfilm
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
