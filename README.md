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

**197** channels, **3,118,875*** programs, **2,086,715.9** hours playtime between **2023-01-17** and **2025-08-25**


### playtime per genre (top 30)

    551,215.5h 26.42% Serie
    324,799.1h 15.57% Magazin
    257,087.0h 12.32% Dokumentation
    183,193.0h 8.78%  Show
    178,034.4h 8.53%  Werbung
    163,369.8h 7.83%  Spielfilm
    130,723.0h 6.26%  Nachrichten
    127,346.7h 6.10%  Sport
    42,084.8h  2.02%  Musik
    42,043.1h  2.01%  Reportage
    20,510.0h  0.98%  Verschiedenes
    15,033.1h  0.72%  Wetter
    11,167.4h  0.54%  Programmende
    9,515.0h   0.46%  E-Sport
    6,777.4h   0.32%  Bericht
    6,088.7h   0.29%  Event
    3,860.9h   0.19%  Videoclip
    3,818.9h   0.18%  Kurzfilm
    3,541.9h   0.17%  *unknown*
    2,045.6h   0.10%  Verkaufsshow
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
