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

**198** channels, **4,570,130*** programs, **3,132,698.6** hours playtime between **2023-01-17** and **2026-04-29**


### playtime per genre (top 30)

    847,390.4h 27.05% Serie
    448,262.5h 14.31% Magazin
    400,867.4h 12.80% Dokumentation
    283,182.0h 9.04%  Spielfilm
    261,567.6h 8.35%  Show
    239,209.0h 7.64%  Werbung
    232,436.3h 7.42%  Sport
    172,213.3h 5.50%  Nachrichten
    69,483.5h  2.22%  Musik
    60,658.8h  1.94%  Reportage
    36,262.1h  1.16%  Verschiedenes
    19,847.5h  0.63%  Wetter
    11,167.4h  0.36%  Programmende
    9,515.0h   0.30%  E-Sport
    8,865.0h   0.28%  Bericht
    8,037.3h   0.26%  Event
    7,032.1h   0.22%  Kurzfilm
    6,633.2h   0.21%  Videoclip
    3,541.9h   0.11%  *unknown*
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
