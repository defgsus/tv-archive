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

**197** channels, **2,524,058*** programs, **1,659,280.7** hours playtime between **2023-01-17** and **2025-05-18**


### playtime per genre (top 30)

    430,094.2h 25.92% Serie
    275,499.5h 16.60% Magazin
    200,156.7h 12.06% Dokumentation
    152,346.1h 9.18%  Werbung
    151,444.7h 9.13%  Show
    115,573.8h 6.97%  Spielfilm
    114,964.5h 6.93%  Nachrichten
    84,336.8h  5.08%  Sport
    34,316.1h  2.07%  Reportage
    27,738.3h  1.67%  Musik
    13,091.8h  0.79%  Wetter
    12,786.4h  0.77%  Verschiedenes
    11,167.4h  0.67%  Programmende
    9,515.0h   0.57%  E-Sport
    6,144.8h   0.37%  Bericht
    5,371.7h   0.32%  Event
    3,541.9h   0.21%  *unknown*
    2,736.4h   0.16%  Videoclip
    2,045.6h   0.12%  Verkaufsshow
    1,948.2h   0.12%  Kurzfilm
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
