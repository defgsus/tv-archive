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

**197** channels, **3,053,183*** programs, **2,039,616.2** hours playtime between **2023-01-17** and **2025-08-14**


### playtime per genre (top 30)

    537,822.8h 26.37% Serie
    319,494.0h 15.66% Magazin
    250,630.8h 12.29% Dokumentation
    179,782.0h 8.81%  Show
    175,166.4h 8.59%  Werbung
    157,902.9h 7.74%  Spielfilm
    129,078.2h 6.33%  Nachrichten
    122,736.9h 6.02%  Sport
    41,148.4h  2.02%  Reportage
    40,599.0h  1.99%  Musik
    19,635.2h  0.96%  Verschiedenes
    14,808.5h  0.73%  Wetter
    11,167.4h  0.55%  Programmende
    9,515.0h   0.47%  E-Sport
    6,746.0h   0.33%  Bericht
    5,998.2h   0.29%  Event
    3,717.7h   0.18%  Videoclip
    3,618.5h   0.18%  Kurzfilm
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
