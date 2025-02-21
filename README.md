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

**195** channels, **2,010,329*** programs, **1,289,420.3** hours playtime between **2023-01-17** and **2025-02-21**


### playtime per genre (top 30)

    326,709.4h 25.34% Serie
    232,158.9h 18.00% Magazin
    151,675.2h 11.76% Dokumentation
    129,266.4h 10.03% Werbung
    122,542.1h 9.50%  Show
    100,682.8h 7.81%  Nachrichten
    74,910.2h  5.81%  Spielfilm
    47,463.6h  3.68%  Sport
    27,970.2h  2.17%  Reportage
    15,041.9h  1.17%  Musik
    11,549.0h  0.90%  Wetter
    11,167.4h  0.87%  Programmende
    9,515.0h   0.74%  E-Sport
    6,369.2h   0.49%  Verschiedenes
    5,464.4h   0.42%  Bericht
    4,649.6h   0.36%  Event
    3,541.9h   0.27%  *unknown*
    2,045.6h   0.16%  Verkaufsshow
    1,910.1h   0.15%  Videoclip
    353.9h     0.03%  Eishockey
    329.5h     0.03%  Kurzfilm
    299.8h     0.02%  Judo
    257.0h     0.02%  Darts
    232.8h     0.02%  Handball
    219.5h     0.02%  Dokureihe
    212.4h     0.02%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
