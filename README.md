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

**197** channels, **2,571,869*** programs, **1,694,033.8** hours playtime between **2023-01-17** and **2025-05-26**


### playtime per genre (top 30)

    439,795.5h 25.96% Serie
    279,462.1h 16.50% Magazin
    204,688.5h 12.08% Dokumentation
    154,487.6h 9.12%  Werbung
    154,107.6h 9.10%  Show
    119,391.3h 7.05%  Spielfilm
    116,228.4h 6.86%  Nachrichten
    88,069.8h  5.20%  Sport
    34,938.6h  2.06%  Reportage
    28,944.5h  1.71%  Musik
    13,381.3h  0.79%  Verschiedenes
    13,225.3h  0.78%  Wetter
    11,167.4h  0.66%  Programmende
    9,515.0h   0.56%  E-Sport
    6,228.9h   0.37%  Bericht
    5,439.3h   0.32%  Event
    3,541.9h   0.21%  *unknown*
    2,814.0h   0.17%  Videoclip
    2,100.3h   0.12%  Kurzfilm
    2,045.6h   0.12%  Verkaufsshow
    353.9h     0.02%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.02%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
