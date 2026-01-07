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

**197** channels, **3,920,025*** programs, **2,669,410.3** hours playtime between **2023-01-17** and **2026-01-07**


### playtime per genre (top 30)

    712,123.6h 26.68% Serie
    393,452.7h 14.74% Magazin
    335,815.3h 12.58% Dokumentation
    232,630.1h 8.71%  Spielfilm
    226,737.9h 8.49%  Show
    212,048.6h 7.94%  Werbung
    184,284.8h 6.90%  Sport
    153,086.5h 5.73%  Nachrichten
    60,879.1h  2.28%  Musik
    52,040.4h  1.95%  Reportage
    30,805.5h  1.15%  Verschiedenes
    17,722.6h  0.66%  Wetter
    11,167.4h  0.42%  Programmende
    9,515.0h   0.36%  E-Sport
    8,060.1h   0.30%  Bericht
    7,169.2h   0.27%  Event
    6,335.6h   0.24%  Kurzfilm
    5,467.6h   0.20%  Videoclip
    3,541.9h   0.13%  *unknown*
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
