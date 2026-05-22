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

**200** channels, **4,702,257*** programs, **3,226,866.1** hours playtime between **2023-01-17** and **2026-05-22**


### playtime per genre (top 30)

    875,160.2h 27.12% Serie
    459,164.0h 14.23% Magazin
    414,331.7h 12.84% Dokumentation
    293,143.5h 9.08%  Spielfilm
    268,550.0h 8.32%  Show
    244,732.5h 7.58%  Werbung
    242,199.4h 7.51%  Sport
    176,589.6h 5.47%  Nachrichten
    71,243.2h  2.21%  Musik
    62,327.1h  1.93%  Reportage
    37,176.8h  1.15%  Verschiedenes
    20,288.1h  0.63%  Wetter
    11,167.4h  0.35%  Programmende
    9,515.0h   0.29%  E-Sport
    9,043.2h   0.28%  Bericht
    8,218.0h   0.25%  Event
    7,086.4h   0.22%  Kurzfilm
    6,861.5h   0.21%  Videoclip
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
