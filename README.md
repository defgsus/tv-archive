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

**197** channels, **3,137,336*** programs, **2,099,614.8** hours playtime between **2023-01-17** and **2025-08-28**


### playtime per genre (top 30)

    554,999.1h 26.43% Serie
    326,389.6h 15.55% Magazin
    258,815.4h 12.33% Dokumentation
    184,141.1h 8.77%  Show
    178,816.3h 8.52%  Werbung
    164,670.1h 7.84%  Spielfilm
    131,261.7h 6.25%  Nachrichten
    128,495.6h 6.12%  Sport
    42,460.4h  2.02%  Musik
    42,268.8h  2.01%  Reportage
    20,790.3h  0.99%  Verschiedenes
    15,101.4h  0.72%  Wetter
    11,167.4h  0.53%  Programmende
    9,515.0h   0.45%  E-Sport
    6,791.4h   0.32%  Bericht
    6,102.1h   0.29%  Event
    3,900.6h   0.19%  Videoclip
    3,880.5h   0.18%  Kurzfilm
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
