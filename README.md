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

**203** channels, **5,285,442** programs, **3,644,079** hours playtime between **2023-01-17** and **2026-09-02**


### playtime per genre (top 30)

    997,861.5h 27.38% Serie
    506,762.7h 13.91% Magazin
    475,210.0h 13.04% Dokumentation
    336,735.5h 9.24%  Spielfilm
    299,600.7h 8.22%  Show
    286,636.8h 7.87%  Sport
    267,451.9h 7.34%  Werbung
    195,989.8h 5.38%  Nachrichten
    79,207.4h  2.17%  Musik
    69,958.6h  1.92%  Reportage
    41,621.1h  1.14%  Verschiedenes
    22,207.4h  0.61%  Wetter
    11,167.4h  0.31%  Programmende
    9,861.5h   0.27%  Bericht
    9,515.0h   0.26%  E-Sport
    9,051.3h   0.25%  Event
    7,929.4h   0.22%  Videoclip
    7,242.9h   0.20%  Kurzfilm
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
