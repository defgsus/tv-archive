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

**197** channels, **2,753,009*** programs, **1,824,114.6** hours playtime between **2023-01-17** and **2025-06-25**


### playtime per genre (top 30)

    476,339.1h 26.11% Serie
    294,410.2h 16.14% Magazin
    221,800.6h 12.16% Dokumentation
    164,084.6h 9.00%  Show
    162,443.7h 8.91%  Werbung
    134,250.6h 7.36%  Spielfilm
    120,875.8h 6.63%  Nachrichten
    101,159.5h 5.55%  Sport
    37,304.8h  2.05%  Reportage
    33,437.8h  1.83%  Musik
    15,595.8h  0.85%  Verschiedenes
    13,811.1h  0.76%  Wetter
    11,167.4h  0.61%  Programmende
    9,515.0h   0.52%  E-Sport
    6,426.9h   0.35%  Bericht
    5,652.4h   0.31%  Event
    3,541.9h   0.19%  *unknown*
    3,115.9h   0.17%  Videoclip
    2,675.1h   0.15%  Kurzfilm
    2,045.6h   0.11%  Verkaufsshow
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
