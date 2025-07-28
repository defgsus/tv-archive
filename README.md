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

**197** channels, **2,950,700*** programs, **1,966,482.2** hours playtime between **2023-01-17** and **2025-07-28**


### playtime per genre (top 30)

    516,628.5h 26.27% Serie
    311,134.2h 15.82% Magazin
    240,734.2h 12.24% Dokumentation
    174,651.1h 8.88%  Show
    170,844.3h 8.69%  Werbung
    149,902.2h 7.62%  Spielfilm
    126,174.0h 6.42%  Nachrichten
    115,588.7h 5.88%  Sport
    39,752.4h  2.02%  Reportage
    38,353.1h  1.95%  Musik
    18,156.1h  0.92%  Verschiedenes
    14,451.2h  0.73%  Wetter
    11,167.4h  0.57%  Programmende
    9,515.0h   0.48%  E-Sport
    6,708.2h   0.34%  Bericht
    5,877.3h   0.30%  Event
    3,541.9h   0.18%  *unknown*
    3,490.0h   0.18%  Videoclip
    3,306.1h   0.17%  Kurzfilm
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
