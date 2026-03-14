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

**198** channels, **4,306,666*** programs, **2,944,652.5** hours playtime between **2023-01-17** and **2026-03-14**


### playtime per genre (top 30)

    792,306.1h 26.91% Serie
    426,247.2h 14.48% Magazin
    374,085.3h 12.70% Dokumentation
    262,640.2h 8.92%  Spielfilm
    247,535.9h 8.41%  Show
    228,237.0h 7.75%  Werbung
    212,950.3h 7.23%  Sport
    164,167.5h 5.58%  Nachrichten
    65,910.1h  2.24%  Musik
    57,110.1h  1.94%  Reportage
    34,402.7h  1.17%  Verschiedenes
    18,969.5h  0.64%  Wetter
    11,167.4h  0.38%  Programmende
    9,515.0h   0.32%  E-Sport
    8,535.4h   0.29%  Bericht
    7,661.0h   0.26%  Event
    6,978.4h   0.24%  Kurzfilm
    6,164.9h   0.21%  Videoclip
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
