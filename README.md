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

**203** channels, **4,899,852** programs, **3,369,166** hours playtime between **2023-01-17** and **2026-06-26**


### playtime per genre (top 30)

    916,490.4h 27.20% Serie
    475,347.0h 14.11% Magazin
    434,816.5h 12.91% Dokumentation
    308,593.2h 9.16%  Spielfilm
    279,016.0h 8.28%  Show
    257,686.1h 7.65%  Sport
    252,436.1h 7.49%  Werbung
    183,226.2h 5.44%  Nachrichten
    73,927.6h  2.19%  Musik
    64,806.1h  1.92%  Reportage
    38,977.9h  1.16%  Verschiedenes
    20,930.4h  0.62%  Wetter
    11,167.4h  0.33%  Programmende
    9,515.0h   0.28%  E-Sport
    9,308.0h   0.28%  Bericht
    8,486.1h   0.25%  Event
    7,219.9h   0.21%  Videoclip
    7,148.5h   0.21%  Kurzfilm
    3,541.9h   0.11%  *unknown*
    2,045.6h   0.06%  Verkaufsshow
    353.9h     0.01%  Eishockey
    299.8h     0.01%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.00%  Fußball
    147.0h     0.00%  Wirtschaftsmagazin
