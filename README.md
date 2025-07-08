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

**197** channels, **2,830,996*** programs, **1,880,179.7** hours playtime between **2023-01-17** and **2025-07-08**


### playtime per genre (top 30)

    492,263.2h 26.18% Serie
    301,072.9h 16.01% Magazin
    229,137.7h 12.19% Dokumentation
    168,385.3h 8.96%  Show
    165,819.4h 8.82%  Werbung
    140,411.7h 7.47%  Spielfilm
    122,934.5h 6.54%  Nachrichten
    106,749.6h 5.68%  Sport
    38,253.3h  2.03%  Reportage
    35,374.6h  1.88%  Musik
    16,538.0h  0.88%  Verschiedenes
    14,069.6h  0.75%  Wetter
    11,167.4h  0.59%  Programmende
    9,515.0h   0.51%  E-Sport
    6,537.2h   0.35%  Bericht
    5,739.2h   0.31%  Event
    3,541.9h   0.19%  *unknown*
    3,242.8h   0.17%  Videoclip
    2,920.1h   0.16%  Kurzfilm
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
