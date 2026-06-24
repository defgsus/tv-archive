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

**203** channels, **4,883,140** programs, **3,357,251** hours playtime between **2023-01-17** and **2026-06-24**


### playtime per genre (top 30)

    912,898.2h 27.19% Serie
    473,886.5h 14.12% Magazin
    433,139.6h 12.90% Dokumentation
    307,501.7h 9.16%  Spielfilm
    278,206.8h 8.29%  Show
    256,363.0h 7.64%  Sport
    251,815.9h 7.50%  Werbung
    182,645.5h 5.44%  Nachrichten
    73,721.3h  2.20%  Musik
    64,581.9h  1.92%  Reportage
    38,786.8h  1.16%  Verschiedenes
    20,879.9h  0.62%  Wetter
    11,167.4h  0.33%  Programmende
    9,515.0h   0.28%  E-Sport
    9,271.8h   0.28%  Bericht
    8,467.7h   0.25%  Event
    7,188.1h   0.21%  Videoclip
    7,145.7h   0.21%  Kurzfilm
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
