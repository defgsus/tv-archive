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

**197** channels, **3,566,934*** programs, **2,410,828.2** hours playtime between **2023-01-17** and **2025-11-08**


### playtime per genre (top 30)

    642,459.6h 26.65% Serie
    363,687.6h 15.09% Magazin
    300,722.5h 12.47% Dokumentation
    207,768.0h 8.62%  Show
    198,851.6h 8.25%  Spielfilm
    197,183.7h 8.18%  Werbung
    158,743.1h 6.58%  Sport
    143,363.3h 5.95%  Nachrichten
    52,453.8h  2.18%  Musik
    47,605.6h  1.97%  Reportage
    26,569.2h  1.10%  Verschiedenes
    16,516.8h  0.69%  Wetter
    11,167.4h  0.46%  Programmende
    9,515.0h   0.39%  E-Sport
    7,610.1h   0.32%  Bericht
    6,629.8h   0.28%  Event
    5,172.7h   0.21%  Kurzfilm
    4,750.9h   0.20%  Videoclip
    3,541.9h   0.15%  *unknown*
    2,045.6h   0.08%  Verkaufsshow
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
