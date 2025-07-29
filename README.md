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

**197** channels, **2,956,838*** programs, **1,970,804.0** hours playtime between **2023-01-17** and **2025-07-29**


### playtime per genre (top 30)

    517,943.5h 26.28% Serie
    311,670.9h 15.81% Magazin
    241,285.2h 12.24% Dokumentation
    174,940.8h 8.88%  Show
    171,073.1h 8.68%  Werbung
    150,328.1h 7.63%  Spielfilm
    126,352.2h 6.41%  Nachrichten
    115,982.2h 5.89%  Sport
    39,854.6h  2.02%  Reportage
    38,499.3h  1.95%  Musik
    18,244.2h  0.93%  Verschiedenes
    14,472.5h  0.73%  Wetter
    11,167.4h  0.57%  Programmende
    9,515.0h   0.48%  E-Sport
    6,710.8h   0.34%  Bericht
    5,884.3h   0.30%  Event
    3,541.9h   0.18%  *unknown*
    3,503.7h   0.18%  Videoclip
    3,327.8h   0.17%  Kurzfilm
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
