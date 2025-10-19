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

**197** channels, **3,447,079*** programs, **2,323,831.8** hours playtime between **2023-01-17** and **2025-10-19**


### playtime per genre (top 30)

    617,823.2h 26.59% Serie
    353,072.9h 15.19% Magazin
    289,294.4h 12.45% Dokumentation
    201,347.9h 8.66%  Show
    191,953.6h 8.26%  Werbung
    189,226.8h 8.14%  Spielfilm
    150,287.0h 6.47%  Sport
    139,934.3h 6.02%  Nachrichten
    49,602.3h  2.13%  Musik
    46,042.1h  1.98%  Reportage
    25,138.5h  1.08%  Verschiedenes
    16,131.9h  0.69%  Wetter
    11,167.4h  0.48%  Programmende
    9,515.0h   0.41%  E-Sport
    7,460.4h   0.32%  Bericht
    6,487.4h   0.28%  Event
    4,785.2h   0.21%  Kurzfilm
    4,511.2h   0.19%  Videoclip
    3,541.9h   0.15%  *unknown*
    2,045.6h   0.09%  Verkaufsshow
    353.9h     0.02%  Eishockey
    299.8h     0.01%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
