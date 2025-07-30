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

**197** channels, **2,962,948*** programs, **1,975,085.3** hours playtime between **2023-01-17** and **2025-07-30**


### playtime per genre (top 30)

    519,200.6h 26.29% Serie
    312,202.3h 15.81% Magazin
    241,863.6h 12.25% Dokumentation
    175,232.0h 8.87%  Show
    171,303.1h 8.67%  Werbung
    150,798.4h 7.64%  Spielfilm
    126,538.9h 6.41%  Nachrichten
    116,360.5h 5.89%  Sport
    39,936.2h  2.02%  Reportage
    38,647.9h  1.96%  Musik
    18,312.3h  0.93%  Verschiedenes
    14,493.3h  0.73%  Wetter
    11,167.4h  0.57%  Programmende
    9,515.0h   0.48%  E-Sport
    6,713.6h   0.34%  Bericht
    5,888.8h   0.30%  Event
    3,541.9h   0.18%  *unknown*
    3,517.0h   0.18%  Videoclip
    3,346.1h   0.17%  Kurzfilm
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
