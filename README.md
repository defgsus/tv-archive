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

**195** channels, **2,039,784*** programs, **1,310,869.6** hours playtime between **2023-01-17** and **2025-02-26**


### playtime per genre (top 30)

    332,596.9h 25.37% Serie
    234,674.6h 17.90% Magazin
    154,553.7h 11.79% Dokumentation
    130,558.9h 9.96%  Werbung
    124,325.6h 9.48%  Show
    101,530.6h 7.75%  Nachrichten
    77,257.2h  5.89%  Spielfilm
    49,605.0h  3.78%  Sport
    28,303.7h  2.16%  Reportage
    15,770.8h  1.20%  Musik
    11,635.5h  0.89%  Wetter
    11,167.4h  0.85%  Programmende
    9,515.0h   0.73%  E-Sport
    6,722.6h   0.51%  Verschiedenes
    5,531.4h   0.42%  Bericht
    4,693.1h   0.36%  Event
    3,541.9h   0.27%  *unknown*
    2,045.6h   0.16%  Verkaufsshow
    1,960.4h   0.15%  Videoclip
    421.9h     0.03%  Kurzfilm
    353.9h     0.03%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.02%  Darts
    232.8h     0.02%  Handball
    219.5h     0.02%  Dokureihe
    212.4h     0.02%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
