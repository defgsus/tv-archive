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

**197** channels, **2,518,286*** programs, **1,654,949.2** hours playtime between **2023-01-17** and **2025-05-17**


### playtime per genre (top 30)

    428,882.4h 25.92% Serie
    275,084.2h 16.62% Magazin
    199,622.7h 12.06% Dokumentation
    152,078.9h 9.19%  Werbung
    151,093.9h 9.13%  Show
    115,002.1h 6.95%  Spielfilm
    114,838.6h 6.94%  Nachrichten
    83,861.1h  5.07%  Sport
    34,234.9h  2.07%  Reportage
    27,570.2h  1.67%  Musik
    13,080.0h  0.79%  Wetter
    12,715.1h  0.77%  Verschiedenes
    11,167.4h  0.67%  Programmende
    9,515.0h   0.57%  E-Sport
    6,138.5h   0.37%  Bericht
    5,361.2h   0.32%  Event
    3,541.9h   0.21%  *unknown*
    2,726.8h   0.16%  Videoclip
    2,045.6h   0.12%  Verkaufsshow
    1,927.8h   0.12%  Kurzfilm
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
