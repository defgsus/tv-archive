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

**195** channels, **2,315,600*** programs, **1,508,143.6** hours playtime between **2023-01-17** and **2025-04-13**


### playtime per genre (top 30)

    387,848.8h 25.72% Serie
    258,141.1h 17.12% Magazin
    180,205.3h 11.95% Dokumentation
    143,081.1h 9.49%  Werbung
    140,037.5h 9.29%  Show
    109,307.2h 7.25%  Nachrichten
    98,048.6h  6.50%  Spielfilm
    69,242.7h  4.59%  Sport
    31,609.8h  2.10%  Reportage
    22,588.7h  1.50%  Musik
    12,464.9h  0.83%  Wetter
    11,167.4h  0.74%  Programmende
    10,196.0h  0.68%  Verschiedenes
    9,515.0h   0.63%  E-Sport
    5,895.1h   0.39%  Bericht
    5,057.2h   0.34%  Event
    3,541.9h   0.23%  *unknown*
    2,391.1h   0.16%  Videoclip
    2,045.6h   0.14%  Verkaufsshow
    1,298.7h   0.09%  Kurzfilm
    353.9h     0.02%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.02%  Darts
    232.8h     0.02%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
