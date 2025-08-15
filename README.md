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

**197** channels, **3,059,242*** programs, **2,043,890.1** hours playtime between **2023-01-17** and **2025-08-15**


### playtime per genre (top 30)

    539,122.2h 26.38% Serie
    319,998.8h 15.66% Magazin
    251,220.4h 12.29% Dokumentation
    180,074.1h 8.81%  Show
    175,430.6h 8.58%  Werbung
    158,294.6h 7.74%  Spielfilm
    129,233.0h 6.32%  Nachrichten
    123,142.7h 6.02%  Sport
    41,234.0h  2.02%  Reportage
    40,728.2h  1.99%  Musik
    19,727.3h  0.97%  Verschiedenes
    14,831.5h  0.73%  Wetter
    11,167.4h  0.55%  Programmende
    9,515.0h   0.47%  E-Sport
    6,749.3h   0.33%  Bericht
    6,003.3h   0.29%  Event
    3,731.3h   0.18%  Videoclip
    3,637.9h   0.18%  Kurzfilm
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
