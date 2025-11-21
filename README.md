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

**197** channels, **3,644,322*** programs, **2,467,022.6** hours playtime between **2023-01-17** and **2025-11-21**


### playtime per genre (top 30)

    657,795.8h 26.66% Serie
    370,335.3h 15.01% Magazin
    308,335.0h 12.50% Dokumentation
    211,961.8h 8.59%  Show
    205,407.2h 8.33%  Spielfilm
    200,592.7h 8.13%  Werbung
    164,340.6h 6.66%  Sport
    145,594.2h 5.90%  Nachrichten
    54,405.2h  2.21%  Musik
    48,533.9h  1.97%  Reportage
    27,431.9h  1.11%  Verschiedenes
    16,764.4h  0.68%  Wetter
    11,167.4h  0.45%  Programmende
    9,515.0h   0.39%  E-Sport
    7,730.4h   0.31%  Bericht
    6,732.5h   0.27%  Event
    5,413.4h   0.22%  Kurzfilm
    4,904.6h   0.20%  Videoclip
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
