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

**197** channels, **3,834,653*** programs, **2,604,979.6** hours playtime between **2023-01-17** and **2025-12-23**


### playtime per genre (top 30)

    695,992.6h 26.72% Serie
    386,986.2h 14.86% Magazin
    326,490.3h 12.53% Dokumentation
    221,934.4h 8.52%  Show
    221,671.8h 8.51%  Spielfilm
    208,565.4h 8.01%  Werbung
    178,043.5h 6.83%  Sport
    150,946.6h 5.79%  Nachrichten
    59,196.5h  2.27%  Musik
    50,960.1h  1.96%  Reportage
    29,730.3h  1.14%  Verschiedenes
    17,411.4h  0.67%  Wetter
    11,167.4h  0.43%  Programmende
    9,515.0h   0.37%  E-Sport
    8,025.4h   0.31%  Bericht
    6,978.1h   0.27%  Event
    6,023.4h   0.23%  Kurzfilm
    5,275.1h   0.20%  Videoclip
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
