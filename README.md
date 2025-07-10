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

**197** channels, **2,843,072*** programs, **1,888,770.4** hours playtime between **2023-01-17** and **2025-07-10**


### playtime per genre (top 30)

    494,828.6h 26.20% Serie
    302,138.5h 16.00% Magazin
    230,223.5h 12.19% Dokumentation
    168,953.5h 8.95%  Show
    166,341.2h 8.81%  Werbung
    141,251.6h 7.48%  Spielfilm
    123,272.3h 6.53%  Nachrichten
    107,616.6h 5.70%  Sport
    38,406.8h  2.03%  Reportage
    35,660.1h  1.89%  Musik
    16,684.2h  0.88%  Verschiedenes
    14,109.9h  0.75%  Wetter
    11,167.4h  0.59%  Programmende
    9,515.0h   0.50%  E-Sport
    6,584.8h   0.35%  Bericht
    5,747.9h   0.30%  Event
    3,541.9h   0.19%  *unknown*
    3,262.4h   0.17%  Videoclip
    2,957.9h   0.16%  Kurzfilm
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
