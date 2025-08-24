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

**197** channels, **3,113,105*** programs, **2,082,390.1** hours playtime between **2023-01-17** and **2025-08-24**


### playtime per genre (top 30)

    550,134.1h 26.42% Serie
    324,336.2h 15.58% Magazin
    256,475.6h 12.32% Dokumentation
    182,867.2h 8.78%  Show
    177,766.9h 8.54%  Werbung
    162,740.6h 7.82%  Spielfilm
    130,599.1h 6.27%  Nachrichten
    126,907.1h 6.09%  Sport
    41,953.2h  2.01%  Reportage
    41,944.1h  2.01%  Musik
    20,429.7h  0.98%  Verschiedenes
    15,014.6h  0.72%  Wetter
    11,167.4h  0.54%  Programmende
    9,515.0h   0.46%  E-Sport
    6,774.0h   0.33%  Bericht
    6,068.6h   0.29%  Event
    3,847.9h   0.18%  Videoclip
    3,800.5h   0.18%  Kurzfilm
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
