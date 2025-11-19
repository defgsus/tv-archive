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

**197** channels, **3,632,134*** programs, **2,458,381.6** hours playtime between **2023-01-17** and **2025-11-19**


### playtime per genre (top 30)

    655,296.8h 26.66% Serie
    369,209.3h 15.02% Magazin
    307,236.0h 12.50% Dokumentation
    211,328.9h 8.60%  Show
    204,534.6h 8.32%  Spielfilm
    200,061.2h 8.14%  Werbung
    163,561.2h 6.65%  Sport
    145,216.2h 5.91%  Nachrichten
    54,111.4h  2.20%  Musik
    48,393.5h  1.97%  Reportage
    27,300.3h  1.11%  Verschiedenes
    16,721.3h  0.68%  Wetter
    11,167.4h  0.45%  Programmende
    9,515.0h   0.39%  E-Sport
    7,693.6h   0.31%  Bericht
    6,716.1h   0.27%  Event
    5,376.7h   0.22%  Kurzfilm
    4,880.8h   0.20%  Videoclip
    3,541.9h   0.14%  *unknown*
    2,045.6h   0.08%  Verkaufsshow
    353.9h     0.01%  Eishockey
    299.8h     0.01%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
