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

**197** channels, **2,866,666*** programs, **1,906,010.4** hours playtime between **2023-01-17** and **2025-07-14**


### playtime per genre (top 30)

    499,509.1h 26.21% Serie
    304,077.8h 15.95% Magazin
    232,580.4h 12.20% Dokumentation
    170,278.7h 8.93%  Show
    167,380.3h 8.78%  Werbung
    143,263.0h 7.52%  Spielfilm
    123,844.3h 6.50%  Nachrichten
    109,456.1h 5.74%  Sport
    38,693.1h  2.03%  Reportage
    36,276.5h  1.90%  Musik
    16,975.7h  0.89%  Verschiedenes
    14,179.9h  0.74%  Wetter
    11,167.4h  0.59%  Programmende
    9,515.0h   0.50%  E-Sport
    6,640.5h   0.35%  Bericht
    5,782.3h   0.30%  Event
    3,541.9h   0.19%  *unknown*
    3,303.3h   0.17%  Videoclip
    3,038.6h   0.16%  Kurzfilm
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
