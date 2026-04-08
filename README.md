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

**198** channels, **4,449,225*** programs, **3,046,916.5** hours playtime between **2023-01-17** and **2026-04-08**


### playtime per genre (top 30)

    821,830.4h 26.97% Serie
    438,212.4h 14.38% Magazin
    388,755.6h 12.76% Dokumentation
    274,367.0h 9.00%  Spielfilm
    255,205.1h 8.38%  Show
    234,183.2h 7.69%  Werbung
    223,462.6h 7.33%  Sport
    168,334.2h 5.52%  Nachrichten
    67,835.4h  2.23%  Musik
    59,133.5h  1.94%  Reportage
    35,380.5h  1.16%  Verschiedenes
    19,443.1h  0.64%  Wetter
    11,167.4h  0.37%  Programmende
    9,515.0h   0.31%  E-Sport
    8,721.7h   0.29%  Bericht
    7,873.3h   0.26%  Event
    7,007.6h   0.23%  Kurzfilm
    6,420.0h   0.21%  Videoclip
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
