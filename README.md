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

**197** channels, **3,065,187*** programs, **2,048,161.9** hours playtime between **2023-01-17** and **2025-08-16**


### playtime per genre (top 30)

    540,313.1h 26.38% Serie
    320,466.6h 15.65% Magazin
    251,812.5h 12.29% Dokumentation
    180,385.7h 8.81%  Show
    175,683.9h 8.58%  Werbung
    158,825.8h 7.75%  Spielfilm
    129,371.5h 6.32%  Nachrichten
    123,557.8h 6.03%  Sport
    41,319.7h  2.02%  Reportage
    40,867.3h  2.00%  Musik
    19,807.2h  0.97%  Verschiedenes
    14,854.4h  0.73%  Wetter
    11,167.4h  0.55%  Programmende
    9,515.0h   0.46%  E-Sport
    6,751.6h   0.33%  Bericht
    6,011.9h   0.29%  Event
    3,743.9h   0.18%  Videoclip
    3,658.4h   0.18%  Kurzfilm
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
