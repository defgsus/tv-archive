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

**203** channels, **4,877,369** programs, **3,353,155** hours playtime between **2023-01-17** and **2026-06-22**


### playtime per genre (top 30)

    911,627.7h 27.19% Serie
    473,386.2h 14.12% Magazin
    432,607.3h 12.90% Dokumentation
    307,142.9h 9.16%  Spielfilm
    277,904.8h 8.29%  Show
    255,901.4h 7.63%  Sport
    251,612.6h 7.50%  Werbung
    182,442.0h 5.44%  Nachrichten
    73,645.1h  2.20%  Musik
    64,499.6h  1.92%  Reportage
    38,720.9h  1.15%  Verschiedenes
    20,862.5h  0.62%  Wetter
    11,167.4h  0.33%  Programmende
    9,515.0h   0.28%  E-Sport
    9,265.7h   0.28%  Bericht
    8,464.8h   0.25%  Event
    7,176.9h   0.21%  Videoclip
    7,144.3h   0.21%  Kurzfilm
    3,541.9h   0.11%  *unknown*
    2,045.6h   0.06%  Verkaufsshow
    353.9h     0.01%  Eishockey
    299.8h     0.01%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.00%  Fußball
    147.0h     0.00%  Wirtschaftsmagazin
