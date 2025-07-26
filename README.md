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

**197** channels, **2,939,166*** programs, **1,957,858.6** hours playtime between **2023-01-17** and **2025-07-26**


### playtime per genre (top 30)

    514,396.5h 26.27% Serie
    310,208.4h 15.84% Magazin
    239,534.0h 12.23% Dokumentation
    174,018.1h 8.89%  Show
    170,375.3h 8.70%  Werbung
    148,744.8h 7.60%  Spielfilm
    125,923.2h 6.43%  Nachrichten
    114,623.4h 5.85%  Sport
    39,605.8h  2.02%  Reportage
    38,048.7h  1.94%  Musik
    17,956.5h  0.92%  Verschiedenes
    14,416.5h  0.74%  Wetter
    11,167.4h  0.57%  Programmende
    9,515.0h   0.49%  E-Sport
    6,700.0h   0.34%  Bericht
    5,849.1h   0.30%  Event
    3,541.9h   0.18%  *unknown*
    3,464.6h   0.18%  Videoclip
    3,263.0h   0.17%  Kurzfilm
    2,045.6h   0.10%  Verkaufsshow
    353.9h     0.02%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
