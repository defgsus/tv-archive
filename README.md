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

**197** channels, **3,179,041*** programs, **2,129,564.6** hours playtime between **2023-01-17** and **2025-09-04**


### playtime per genre (top 30)

    563,397.4h 26.46% Serie
    329,845.0h 15.49% Magazin
    262,904.0h 12.35% Dokumentation
    186,432.6h 8.75%  Show
    180,647.4h 8.48%  Werbung
    167,945.6h 7.89%  Spielfilm
    132,417.4h 6.22%  Nachrichten
    131,358.7h 6.17%  Sport
    43,319.7h  2.03%  Musik
    42,777.9h  2.01%  Reportage
    21,575.2h  1.01%  Verschiedenes
    15,241.8h  0.72%  Wetter
    11,167.4h  0.52%  Programmende
    9,515.0h   0.45%  E-Sport
    6,814.9h   0.32%  Bericht
    6,159.5h   0.29%  Event
    4,004.6h   0.19%  Kurzfilm
    3,992.4h   0.19%  Videoclip
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
