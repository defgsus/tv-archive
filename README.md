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

**197** channels, **2,945,016*** programs, **1,962,160.0** hours playtime between **2023-01-17** and **2025-07-27**


### playtime per genre (top 30)

    515,543.9h 26.27% Serie
    310,682.2h 15.83% Magazin
    240,113.3h 12.24% Dokumentation
    174,331.9h 8.88%  Show
    170,617.8h 8.70%  Werbung
    149,312.8h 7.61%  Spielfilm
    126,051.4h 6.42%  Nachrichten
    115,078.8h 5.86%  Sport
    39,681.0h  2.02%  Reportage
    38,201.1h  1.95%  Musik
    18,060.9h  0.92%  Verschiedenes
    14,435.0h  0.74%  Wetter
    11,167.4h  0.57%  Programmende
    9,515.0h   0.48%  E-Sport
    6,707.6h   0.34%  Bericht
    5,852.5h   0.30%  Event
    3,541.9h   0.18%  *unknown*
    3,476.5h   0.18%  Videoclip
    3,282.8h   0.17%  Kurzfilm
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
