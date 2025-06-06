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

**197** channels, **2,645,127*** programs, **1,746,080.0** hours playtime between **2023-01-17** and **2025-06-07**


### playtime per genre (top 30)

    454,742.1h 26.04% Serie
    285,513.6h 16.35% Magazin
    211,499.5h 12.11% Dokumentation
    158,042.2h 9.05%  Show
    157,656.4h 9.03%  Werbung
    124,973.6h 7.16%  Spielfilm
    118,200.5h 6.77%  Nachrichten
    93,301.6h  5.34%  Sport
    35,872.9h  2.05%  Reportage
    30,712.4h  1.76%  Musik
    14,290.2h  0.82%  Verschiedenes
    13,468.4h  0.77%  Wetter
    11,167.4h  0.64%  Programmende
    9,515.0h   0.54%  E-Sport
    6,290.4h   0.36%  Bericht
    5,518.7h   0.32%  Event
    3,541.9h   0.20%  *unknown*
    2,936.4h   0.17%  Videoclip
    2,330.3h   0.13%  Kurzfilm
    2,045.6h   0.12%  Verkaufsshow
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
