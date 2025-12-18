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

**197** channels, **3,805,219*** programs, **2,583,332.5** hours playtime between **2023-01-17** and **2025-12-18**


### playtime per genre (top 30)

    690,290.7h 26.72% Serie
    384,534.2h 14.89% Magazin
    323,639.7h 12.53% Dokumentation
    220,434.3h 8.53%  Show
    218,702.3h 8.47%  Spielfilm
    207,311.3h 8.02%  Werbung
    175,777.9h 6.80%  Sport
    150,141.9h 5.81%  Nachrichten
    58,438.6h  2.26%  Musik
    50,598.3h  1.96%  Reportage
    29,328.4h  1.14%  Verschiedenes
    17,310.8h  0.67%  Wetter
    11,167.4h  0.43%  Programmende
    9,515.0h   0.37%  E-Sport
    7,996.1h   0.31%  Bericht
    6,932.9h   0.27%  Event
    5,930.1h   0.23%  Kurzfilm
    5,216.1h   0.20%  Videoclip
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
