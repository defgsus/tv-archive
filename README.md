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

**197** channels, **3,548,821*** programs, **2,397,898.0** hours playtime between **2023-01-17** and **2025-11-05**


### playtime per genre (top 30)

    638,736.5h 26.64% Serie
    362,059.4h 15.10% Magazin
    299,071.5h 12.47% Dokumentation
    206,823.6h 8.63%  Show
    197,491.5h 8.24%  Spielfilm
    196,396.7h 8.19%  Werbung
    157,508.7h 6.57%  Sport
    142,806.9h 5.96%  Nachrichten
    52,057.2h  2.17%  Musik
    47,405.1h  1.98%  Reportage
    26,329.3h  1.10%  Verschiedenes
    16,453.7h  0.69%  Wetter
    11,167.4h  0.47%  Programmende
    9,515.0h   0.40%  E-Sport
    7,573.6h   0.32%  Bericht
    6,611.6h   0.28%  Event
    5,116.7h   0.21%  Kurzfilm
    4,716.1h   0.20%  Videoclip
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
