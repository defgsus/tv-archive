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

**197** channels, **3,094,890*** programs, **2,069,494.5** hours playtime between **2023-01-17** and **2025-08-21**


### playtime per genre (top 30)

    546,444.9h 26.40% Serie
    322,877.2h 15.60% Magazin
    254,745.9h 12.31% Dokumentation
    181,886.4h 8.79%  Show
    176,994.2h 8.55%  Werbung
    161,288.1h 7.79%  Spielfilm
    130,109.6h 6.29%  Nachrichten
    125,654.4h 6.07%  Sport
    41,717.3h  2.02%  Reportage
    41,528.7h  2.01%  Musik
    20,192.4h  0.98%  Verschiedenes
    14,951.8h  0.72%  Wetter
    11,167.4h  0.54%  Programmende
    9,515.0h   0.46%  E-Sport
    6,767.7h   0.33%  Bericht
    6,046.1h   0.29%  Event
    3,809.0h   0.18%  Videoclip
    3,750.1h   0.18%  Kurzfilm
    3,541.9h   0.17%  *unknown*
    2,045.6h   0.10%  Verkaufsshow
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
