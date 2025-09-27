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

**197** channels, **3,316,620*** programs, **2,228,898.1** hours playtime between **2023-01-17** and **2025-09-27**


### playtime per genre (top 30)

    591,353.5h 26.53% Serie
    341,783.2h 15.33% Magazin
    276,406.0h 12.40% Dokumentation
    194,058.8h 8.71%  Show
    186,386.4h 8.36%  Werbung
    178,625.2h 8.01%  Spielfilm
    141,150.0h 6.33%  Sport
    136,275.6h 6.11%  Nachrichten
    46,373.4h  2.08%  Musik
    44,476.6h  2.00%  Reportage
    23,468.3h  1.05%  Verschiedenes
    15,700.1h  0.70%  Wetter
    11,167.4h  0.50%  Programmende
    9,515.0h   0.43%  E-Sport
    7,110.1h   0.32%  Bericht
    6,337.9h   0.28%  Event
    4,403.6h   0.20%  Kurzfilm
    4,258.7h   0.19%  Videoclip
    3,541.9h   0.16%  *unknown*
    2,045.6h   0.09%  Verkaufsshow
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
