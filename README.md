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

**210** channels, **5,726,652** programs, **3,963,826** hours playtime between **2023-01-17** and **2026-11-22**


### playtime per genre (top 30)

    1,090,663.6h 27.52% Serie
    545,631.2h   13.77% Magazin
    520,813.6h   13.14% Dokumentation
    370,555.3h   9.35%  Spielfilm
    324,928.2h   8.20%  Show
    320,403.0h   8.08%  Sport
    284,559.7h   7.18%  Werbung
    210,396.2h   5.31%  Nachrichten
    84,900.2h    2.14%  Musik
    75,665.4h    1.91%  Reportage
    44,564.2h    1.12%  Verschiedenes
    23,611.5h    0.60%  Wetter
    11,167.4h    0.28%  Programmende
    10,572.5h    0.27%  Bericht
    9,654.9h     0.24%  Event
    9,515.0h     0.24%  E-Sport
    8,749.1h     0.22%  Videoclip
    7,407.2h     0.19%  Kurzfilm
    3,541.9h     0.09%  *unknown*
    2,045.6h     0.05%  Verkaufsshow
    353.9h       0.01%  Eishockey
    299.8h       0.01%  Judo
    257.0h       0.01%  Darts
    232.8h       0.01%  Handball
    219.5h       0.01%  Dokureihe
    212.4h       0.01%  Leichtathletik
    190.7h       0.00%  Gespräch
    169.7h       0.00%  Erotikfilm
    157.3h       0.00%  Fußball
    147.0h       0.00%  Wirtschaftsmagazin
