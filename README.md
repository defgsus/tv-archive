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

**197** channels, **2,975,212*** programs, **1,983,765.2** hours playtime between **2023-01-17** and **2025-08-01**


### playtime per genre (top 30)

    521,748.6h 26.30% Serie
    313,298.2h 15.79% Magazin
    243,055.9h 12.25% Dokumentation
    175,855.0h 8.86%  Show
    171,786.9h 8.66%  Werbung
    151,595.0h 7.64%  Spielfilm
    126,910.6h 6.40%  Nachrichten
    117,171.4h 5.91%  Sport
    40,104.7h  2.02%  Reportage
    38,935.6h  1.96%  Musik
    18,495.6h  0.93%  Verschiedenes
    14,534.1h  0.73%  Wetter
    11,167.4h  0.56%  Programmende
    9,515.0h   0.48%  E-Sport
    6,719.7h   0.34%  Bericht
    5,897.2h   0.30%  Event
    3,543.7h   0.18%  Videoclip
    3,541.9h   0.18%  *unknown*
    3,382.2h   0.17%  Kurzfilm
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
