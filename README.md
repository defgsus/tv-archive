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

**198** channels, **4,260,943*** programs, **2,911,992.8** hours playtime between **2023-01-17** and **2026-03-06**


### playtime per genre (top 30)

    782,586.0h 26.87% Serie
    422,220.9h 14.50% Magazin
    369,572.4h 12.69% Dokumentation
    259,282.5h 8.90%  Spielfilm
    245,048.1h 8.42%  Show
    226,309.5h 7.77%  Werbung
    209,598.2h 7.20%  Sport
    162,809.8h 5.59%  Nachrichten
    65,299.3h  2.24%  Musik
    56,482.9h  1.94%  Reportage
    34,092.4h  1.17%  Verschiedenes
    18,829.7h  0.65%  Wetter
    11,167.4h  0.38%  Programmende
    9,515.0h   0.33%  E-Sport
    8,449.1h   0.29%  Bericht
    7,605.0h   0.26%  Event
    6,970.9h   0.24%  Kurzfilm
    6,085.1h   0.21%  Videoclip
    3,541.9h   0.12%  *unknown*
    2,045.6h   0.07%  Verkaufsshow
    353.9h     0.01%  Eishockey
    299.8h     0.01%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
