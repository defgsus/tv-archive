# Archive of TV-shows

Scraped directly from a german webpage, started at about mid-January 2023.

[webapp on github.io](https://defgsus.github.io/tv-archive/)

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
  "description": null,
  "season": 2, 
  "episode": 14, 
  "year": 1998, 
  "countries": ["USA"],
}
```

## Statistics

**203** channels, **5,098,401** programs, **3,510,810** hours playtime between **2023-01-17** and **2026-07-31**


### playtime per genre (top 30)

    958,558.5h 27.30% Serie
    491,119.0h 13.99% Magazin
    455,487.5h 12.97% Dokumentation
    322,951.1h 9.20%  Spielfilm
    289,387.4h 8.24%  Show
    273,250.1h 7.78%  Sport
    260,200.5h 7.41%  Werbung
    189,870.1h 5.41%  Nachrichten
    76,662.0h  2.18%  Musik
    67,410.8h  1.92%  Reportage
    40,389.5h  1.15%  Verschiedenes
    21,537.7h  0.61%  Wetter
    11,167.4h  0.32%  Programmende
    9,696.2h   0.28%  Bericht
    9,515.0h   0.27%  E-Sport
    8,769.5h   0.25%  Event
    7,586.7h   0.22%  Videoclip
    7,182.8h   0.20%  Kurzfilm
    3,541.9h   0.10%  *unknown*
    2,045.6h   0.06%  Verkaufsshow
    353.9h     0.01%  Eishockey
    299.8h     0.01%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.00%  Erotikfilm
    157.3h     0.00%  Fußball
    147.0h     0.00%  Wirtschaftsmagazin
