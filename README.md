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

**197** channels, **3,215,121*** programs, **2,155,583.0** hours playtime between **2023-01-17** and **2025-09-10**


### playtime per genre (top 30)

    570,604.6h 26.47% Serie
    332,946.8h 15.45% Magazin
    266,477.0h 12.36% Dokumentation
    188,437.1h 8.74%  Show
    182,230.8h 8.45%  Werbung
    170,816.4h 7.92%  Spielfilm
    133,909.4h 6.21%  Sport
    133,402.7h 6.19%  Nachrichten
    44,129.7h  2.05%  Musik
    43,231.8h  2.01%  Reportage
    22,089.8h  1.02%  Verschiedenes
    15,360.5h  0.71%  Wetter
    11,167.4h  0.52%  Programmende
    9,515.0h   0.44%  E-Sport
    6,834.4h   0.32%  Bericht
    6,209.7h   0.29%  Event
    4,108.3h   0.19%  Kurzfilm
    4,063.2h   0.19%  Videoclip
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
