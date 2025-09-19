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

**197** channels, **3,269,232*** programs, **2,194,423.6** hours playtime between **2023-01-17** and **2025-09-19**


### playtime per genre (top 30)

    581,677.5h 26.51% Serie
    337,676.1h 15.39% Magazin
    271,695.4h 12.38% Dokumentation
    191,385.9h 8.72%  Show
    184,473.2h 8.41%  Werbung
    174,886.0h 7.97%  Spielfilm
    137,793.1h 6.28%  Sport
    134,951.1h 6.15%  Nachrichten
    45,293.5h  2.06%  Musik
    43,875.6h  2.00%  Reportage
    22,821.8h  1.04%  Verschiedenes
    15,537.5h  0.71%  Wetter
    11,167.4h  0.51%  Programmende
    9,515.0h   0.43%  E-Sport
    6,922.1h   0.32%  Bericht
    6,271.9h   0.29%  Event
    4,266.0h   0.19%  Kurzfilm
    4,166.4h   0.19%  Videoclip
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
