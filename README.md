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

**195** channels, **2,052,161*** programs, **1,319,515.1** hours playtime between **2023-01-17** and **2025-02-28**


### playtime per genre (top 30)

    335,117.3h 25.40% Serie
    235,769.1h 17.87% Magazin
    155,643.1h 11.80% Dokumentation
    131,112.8h 9.94%  Werbung
    125,054.7h 9.48%  Show
    101,917.6h 7.72%  Nachrichten
    78,035.9h  5.91%  Spielfilm
    50,388.2h  3.82%  Sport
    28,438.5h  2.16%  Reportage
    16,067.7h  1.22%  Musik
    11,676.2h  0.88%  Wetter
    11,167.4h  0.85%  Programmende
    9,515.0h   0.72%  E-Sport
    6,872.1h   0.52%  Verschiedenes
    5,560.8h   0.42%  Bericht
    4,701.5h   0.36%  Event
    3,541.9h   0.27%  *unknown*
    2,045.6h   0.16%  Verkaufsshow
    1,979.9h   0.15%  Videoclip
    451.9h     0.03%  Kurzfilm
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
