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

**198** channels, **4,392,624*** programs, **3,005,995.9** hours playtime between **2023-01-17** and **2026-03-29**


### playtime per genre (top 30)

    810,272.7h 26.96% Serie
    433,635.5h 14.43% Magazin
    382,625.7h 12.73% Dokumentation
    269,071.9h 8.95%  Spielfilm
    252,264.2h 8.39%  Show
    231,917.2h 7.72%  Werbung
    219,325.7h 7.30%  Sport
    166,722.2h 5.55%  Nachrichten
    67,085.5h  2.23%  Musik
    58,287.8h  1.94%  Reportage
    35,000.4h  1.16%  Verschiedenes
    19,252.3h  0.64%  Wetter
    11,167.4h  0.37%  Programmende
    9,515.0h   0.32%  E-Sport
    8,687.5h   0.29%  Bericht
    7,782.7h   0.26%  Event
    6,994.6h   0.23%  Kurzfilm
    6,319.3h   0.21%  Videoclip
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
    147.0h     0.00%  Wirtschaftsmagazin
