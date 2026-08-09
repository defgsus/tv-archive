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

**203** channels, **5,149,571** programs, **3,547,197** hours playtime between **2023-01-17** and **2026-08-09**


### playtime per genre (top 30)

    969,412.3h 27.33% Serie
    495,306.6h 13.96% Magazin
    460,812.7h 12.99% Dokumentation
    326,789.6h 9.21%  Spielfilm
    292,124.9h 8.24%  Show
    276,799.6h 7.80%  Sport
    262,191.8h 7.39%  Werbung
    191,535.8h 5.40%  Nachrichten
    77,365.6h  2.18%  Musik
    68,188.3h  1.92%  Reportage
    40,713.3h  1.15%  Verschiedenes
    21,731.3h  0.61%  Wetter
    11,167.4h  0.31%  Programmende
    9,758.3h   0.28%  Bericht
    9,515.0h   0.27%  E-Sport
    8,848.5h   0.25%  Event
    7,680.4h   0.22%  Videoclip
    7,187.7h   0.20%  Kurzfilm
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
