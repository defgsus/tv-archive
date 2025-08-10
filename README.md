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

**197** channels, **3,029,253*** programs, **2,022,445.3** hours playtime between **2023-01-17** and **2025-08-10**


### playtime per genre (top 30)

    532,823.1h 26.35% Serie
    317,546.0h 15.70% Magazin
    248,272.6h 12.28% Dokumentation
    178,590.6h 8.83%  Show
    174,136.1h 8.61%  Werbung
    156,011.8h 7.71%  Spielfilm
    128,435.1h 6.35%  Nachrichten
    121,058.4h 5.99%  Sport
    40,828.2h  2.02%  Reportage
    40,092.6h  1.98%  Musik
    19,279.6h  0.95%  Verschiedenes
    14,723.8h  0.73%  Wetter
    11,167.4h  0.55%  Programmende
    9,515.0h   0.47%  E-Sport
    6,736.6h   0.33%  Bericht
    5,968.1h   0.30%  Event
    3,661.3h   0.18%  Videoclip
    3,550.6h   0.18%  Kurzfilm
    3,541.9h   0.18%  *unknown*
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
