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

**195** channels, **2,285,572*** programs, **1,486,786.6** hours playtime between **2023-01-17** and **2025-04-08**


### playtime per genre (top 30)

    381,656.4h 25.67% Serie
    255,617.1h 17.19% Magazin
    177,483.5h 11.94% Dokumentation
    141,723.7h 9.53%  Werbung
    138,364.8h 9.31%  Show
    108,437.5h 7.29%  Nachrichten
    95,897.5h  6.45%  Spielfilm
    67,150.4h  4.52%  Sport
    31,240.4h  2.10%  Reportage
    21,859.1h  1.47%  Musik
    12,372.9h  0.83%  Wetter
    11,167.4h  0.75%  Programmende
    9,822.2h   0.66%  Verschiedenes
    9,515.0h   0.64%  E-Sport
    5,853.1h   0.39%  Bericht
    5,035.0h   0.34%  Event
    3,541.9h   0.24%  *unknown*
    2,343.1h   0.16%  Videoclip
    2,045.6h   0.14%  Verkaufsshow
    1,200.2h   0.08%  Kurzfilm
    353.9h     0.02%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.02%  Darts
    232.8h     0.02%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
