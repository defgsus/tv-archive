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

**198** channels, **4,472,391*** programs, **3,063,235.9** hours playtime between **2023-01-17** and **2026-04-12**


### playtime per genre (top 30)

    826,746.5h 26.99% Serie
    440,152.4h 14.37% Magazin
    390,955.9h 12.76% Dokumentation
    276,082.6h 9.01%  Spielfilm
    256,425.6h 8.37%  Show
    235,151.9h 7.68%  Werbung
    225,151.2h 7.35%  Sport
    169,062.7h 5.52%  Nachrichten
    68,157.6h  2.23%  Musik
    59,424.9h  1.94%  Reportage
    35,541.4h  1.16%  Verschiedenes
    19,522.2h  0.64%  Wetter
    11,167.4h  0.36%  Programmende
    9,515.0h   0.31%  E-Sport
    8,741.6h   0.29%  Bericht
    7,895.8h   0.26%  Event
    7,012.1h   0.23%  Kurzfilm
    6,460.8h   0.21%  Videoclip
    3,541.9h   0.12%  *unknown*
    2,045.6h   0.07%  Verkaufsshow
    353.9h     0.01%  Eishockey
    299.8h     0.01%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.00%  Wirtschaftsmagazin
