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

**210** channels, **5,663,495** programs, **3,918,149** hours playtime between **2023-01-17** and **2026-11-11**


### playtime per genre (top 30)

    1,077,663.1h 27.50% Serie
    540,103.1h   13.78% Magazin
    514,379.7h   13.13% Dokumentation
    365,556.2h   9.33%  Spielfilm
    321,216.1h   8.20%  Show
    315,700.9h   8.06%  Sport
    281,999.9h   7.20%  Werbung
    208,188.8h   5.31%  Nachrichten
    84,106.8h    2.15%  Musik
    74,855.5h    1.91%  Reportage
    44,153.3h    1.13%  Verschiedenes
    23,415.6h    0.60%  Wetter
    11,167.4h    0.29%  Programmende
    10,478.6h    0.27%  Bericht
    9,573.0h     0.24%  Event
    9,515.0h     0.24%  E-Sport
    8,632.4h     0.22%  Videoclip
    7,375.4h     0.19%  Kurzfilm
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
