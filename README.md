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

**196** channels, **2,380,184*** programs, **1,555,454.6** hours playtime between **2023-01-17** and **2025-04-24**


### playtime per genre (top 30)

    400,670.9h 25.76% Serie
    263,454.8h 16.94% Magazin
    186,702.0h 12.00% Dokumentation
    145,949.9h 9.38%  Werbung
    143,464.3h 9.22%  Show
    111,025.7h 7.14%  Nachrichten
    104,201.5h 6.70%  Spielfilm
    73,850.6h  4.75%  Sport
    32,471.5h  2.09%  Reportage
    24,171.3h  1.55%  Musik
    12,662.1h  0.81%  Wetter
    11,167.4h  0.72%  Programmende
    10,997.1h  0.71%  Verschiedenes
    9,515.0h   0.61%  E-Sport
    5,922.5h   0.38%  Bericht
    5,159.2h   0.33%  Event
    3,541.9h   0.23%  *unknown*
    2,501.2h   0.16%  Videoclip
    2,045.6h   0.13%  Verkaufsshow
    1,520.2h   0.10%  Kurzfilm
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
