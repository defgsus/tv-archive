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

**197** channels, **3,519,222*** programs, **2,376,313.2** hours playtime between **2023-01-17** and **2025-10-31**


### playtime per genre (top 30)

    632,923.4h 26.63% Serie
    359,551.8h 15.13% Magazin
    296,152.2h 12.46% Dokumentation
    205,152.5h 8.63%  Show
    195,102.6h 8.21%  Werbung
    194,776.2h 8.20%  Spielfilm
    155,413.2h 6.54%  Sport
    142,005.4h 5.98%  Nachrichten
    51,384.6h  2.16%  Musik
    47,006.2h  1.98%  Reportage
    25,955.2h  1.09%  Verschiedenes
    16,359.0h  0.69%  Wetter
    11,167.4h  0.47%  Programmende
    9,515.0h   0.40%  E-Sport
    7,548.7h   0.32%  Bericht
    6,572.7h   0.28%  Event
    5,015.8h   0.21%  Kurzfilm
    4,657.1h   0.20%  Videoclip
    3,541.9h   0.15%  *unknown*
    2,045.6h   0.09%  Verkaufsshow
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
