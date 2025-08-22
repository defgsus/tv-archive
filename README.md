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

**197** channels, **3,101,077*** programs, **2,073,792.9** hours playtime between **2023-01-17** and **2025-08-22**


### playtime per genre (top 30)

    547,744.9h 26.41% Serie
    323,417.2h 15.60% Magazin
    255,326.7h 12.31% Dokumentation
    182,181.4h 8.78%  Show
    177,245.9h 8.55%  Werbung
    161,685.1h 7.80%  Spielfilm
    130,294.4h 6.28%  Nachrichten
    126,054.0h 6.08%  Sport
    41,801.6h  2.02%  Reportage
    41,657.2h  2.01%  Musik
    20,263.2h  0.98%  Verschiedenes
    14,973.9h  0.72%  Wetter
    11,167.4h  0.54%  Programmende
    9,515.0h   0.46%  E-Sport
    6,770.0h   0.33%  Bericht
    6,055.7h   0.29%  Event
    3,822.0h   0.18%  Videoclip
    3,768.9h   0.18%  Kurzfilm
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
