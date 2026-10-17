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

**210** channels, **5,538,468** programs, **3,826,336** hours playtime between **2023-01-17** and **2026-10-17**


### playtime per genre (top 30)

    1,051,432.9h 27.48% Serie
    529,120.9h   13.83% Magazin
    501,254.7h   13.10% Dokumentation
    355,358.8h   9.29%  Spielfilm
    313,958.2h   8.21%  Show
    305,678.8h   7.99%  Sport
    276,930.7h   7.24%  Werbung
    204,309.7h   5.34%  Nachrichten
    82,483.6h    2.16%  Musik
    73,227.9h    1.91%  Reportage
    43,334.5h    1.13%  Verschiedenes
    23,034.2h    0.60%  Wetter
    11,167.4h    0.29%  Programmende
    10,339.9h    0.27%  Bericht
    9,515.0h     0.25%  E-Sport
    9,401.7h     0.25%  Event
    8,396.5h     0.22%  Videoclip
    7,323.2h     0.19%  Kurzfilm
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
