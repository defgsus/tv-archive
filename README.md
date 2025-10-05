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

**197** channels, **3,363,319*** programs, **2,263,247.3** hours playtime between **2023-01-17** and **2025-10-05**


### playtime per genre (top 30)

    600,718.6h 26.54% Serie
    345,724.7h 15.28% Magazin
    281,261.8h 12.43% Dokumentation
    196,722.3h 8.69%  Show
    188,251.9h 8.32%  Werbung
    182,678.6h 8.07%  Spielfilm
    144,478.9h 6.38%  Sport
    137,529.5h 6.08%  Nachrichten
    47,519.1h  2.10%  Musik
    45,071.7h  1.99%  Reportage
    24,143.9h  1.07%  Verschiedenes
    15,851.8h  0.70%  Wetter
    11,167.4h  0.49%  Programmende
    9,515.0h   0.42%  E-Sport
    7,284.4h   0.32%  Bericht
    6,393.5h   0.28%  Event
    4,542.2h   0.20%  Kurzfilm
    4,343.8h   0.19%  Videoclip
    3,541.9h   0.16%  *unknown*
    2,045.6h   0.09%  Verkaufsshow
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
