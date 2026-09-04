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

**203** channels, **5,296,894** programs, **3,652,148** hours playtime between **2023-01-17** and **2026-09-04**


### playtime per genre (top 30)

    1,000,364.1h 27.39% Serie
    507,781.3h   13.90% Magazin
    476,317.4h   13.04% Dokumentation
    337,463.4h   9.24%  Spielfilm
    300,202.4h   8.22%  Show
    287,445.5h   7.87%  Sport
    267,870.0h   7.33%  Werbung
    196,395.6h   5.38%  Nachrichten
    79,346.3h    2.17%  Musik
    70,129.1h    1.92%  Reportage
    41,701.8h    1.14%  Verschiedenes
    22,247.5h    0.61%  Wetter
    11,167.4h    0.31%  Programmende
    9,871.1h     0.27%  Bericht
    9,515.0h     0.26%  E-Sport
    9,064.9h     0.25%  Event
    7,950.8h     0.22%  Videoclip
    7,246.4h     0.20%  Kurzfilm
    3,541.9h     0.10%  *unknown*
    2,045.6h     0.06%  Verkaufsshow
    353.9h       0.01%  Eishockey
    299.8h       0.01%  Judo
    257.0h       0.01%  Darts
    232.8h       0.01%  Handball
    219.5h       0.01%  Dokureihe
    212.4h       0.01%  Leichtathletik
    190.7h       0.01%  Gespräch
    169.7h       0.00%  Erotikfilm
    157.3h       0.00%  Fußball
    147.0h       0.00%  Wirtschaftsmagazin
