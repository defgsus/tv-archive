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

**197** channels, **3,082,544*** programs, **2,060,937.1** hours playtime between **2023-01-17** and **2025-08-19**


### playtime per genre (top 30)

    543,894.8h 26.39% Serie
    321,797.0h 15.61% Magazin
    253,597.1h 12.30% Dokumentation
    181,280.2h 8.80%  Show
    176,473.0h 8.56%  Werbung
    160,429.9h 7.78%  Spielfilm
    129,753.6h 6.30%  Nachrichten
    124,894.1h 6.06%  Sport
    41,571.6h  2.02%  Reportage
    41,279.1h  2.00%  Musik
    20,033.8h  0.97%  Verschiedenes
    14,908.0h  0.72%  Wetter
    11,167.4h  0.54%  Programmende
    9,515.0h   0.46%  E-Sport
    6,760.1h   0.33%  Bericht
    6,039.3h   0.29%  Event
    3,782.7h   0.18%  Videoclip
    3,711.9h   0.18%  Kurzfilm
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
