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

**195** channels, **2,088,065*** programs, **1,345,301.8** hours playtime between **2023-01-17** and **2025-03-06**


### playtime per genre (top 30)

    342,217.3h 25.44% Serie
    238,805.3h 17.75% Magazin
    158,961.3h 11.82% Dokumentation
    132,723.0h 9.87%  Werbung
    127,261.3h 9.46%  Show
    102,933.4h 7.65%  Nachrichten
    80,853.8h  6.01%  Spielfilm
    52,930.3h  3.93%  Sport
    28,817.1h  2.14%  Reportage
    16,957.8h  1.26%  Musik
    11,778.6h  0.88%  Wetter
    11,167.4h  0.83%  Programmende
    9,515.0h   0.71%  E-Sport
    7,319.3h   0.54%  Verschiedenes
    5,628.2h   0.42%  Bericht
    4,803.5h   0.36%  Event
    3,541.9h   0.26%  *unknown*
    2,045.6h   0.15%  Verkaufsshow
    2,027.0h   0.15%  Videoclip
    556.9h     0.04%  Kurzfilm
    353.9h     0.03%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.02%  Darts
    232.8h     0.02%  Handball
    219.5h     0.02%  Dokureihe
    212.4h     0.02%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
