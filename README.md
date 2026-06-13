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

**203** channels, **4,826,645*** programs, **3,316,134.8** hours playtime between **2023-01-17** and **2026-06-13**


### playtime per genre (top 30)

    901,046.6h 27.17% Serie
    469,262.4h 14.15% Magazin
    427,408.0h 12.89% Dokumentation
    303,189.5h 9.14%  Spielfilm
    275,089.8h 8.30%  Show
    251,516.5h 7.58%  Sport
    249,605.0h 7.53%  Werbung
    180,842.7h 5.45%  Nachrichten
    72,931.8h  2.20%  Musik
    63,841.2h  1.93%  Reportage
    38,128.2h  1.15%  Verschiedenes
    20,715.5h  0.62%  Wetter
    11,167.4h  0.34%  Programmende
    9,515.0h   0.29%  E-Sport
    9,196.5h   0.28%  Bericht
    8,389.6h   0.25%  Event
    7,134.5h   0.22%  Kurzfilm
    7,086.3h   0.21%  Videoclip
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
