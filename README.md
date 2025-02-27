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

**195** channels, **2,045,980*** programs, **1,315,198.8** hours playtime between **2023-01-17** and **2025-02-27**


### playtime per genre (top 30)

    333,872.7h 25.39% Serie
    235,218.9h 17.88% Magazin
    155,081.0h 11.79% Dokumentation
    130,838.1h 9.95%  Werbung
    124,683.1h 9.48%  Show
    101,723.0h 7.73%  Nachrichten
    77,664.8h  5.91%  Spielfilm
    49,998.1h  3.80%  Sport
    28,365.1h  2.16%  Reportage
    15,916.4h  1.21%  Musik
    11,656.4h  0.89%  Wetter
    11,167.4h  0.85%  Programmende
    9,515.0h   0.72%  E-Sport
    6,797.4h   0.52%  Verschiedenes
    5,550.6h   0.42%  Bericht
    4,698.1h   0.36%  Event
    3,541.9h   0.27%  *unknown*
    2,045.6h   0.16%  Verkaufsshow
    1,970.1h   0.15%  Videoclip
    437.2h     0.03%  Kurzfilm
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
