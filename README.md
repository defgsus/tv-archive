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

**198** channels, **4,381,428*** programs, **2,997,868.6** hours playtime between **2023-01-17** and **2026-03-27**


### playtime per genre (top 30)

    807,959.8h 26.95% Serie
    432,691.6h 14.43% Magazin
    381,505.0h 12.73% Dokumentation
    268,095.8h 8.94%  Spielfilm
    251,604.5h 8.39%  Show
    231,433.3h 7.72%  Werbung
    218,479.8h 7.29%  Sport
    166,403.8h 5.55%  Nachrichten
    66,924.0h  2.23%  Musik
    58,137.3h  1.94%  Reportage
    34,923.5h  1.16%  Verschiedenes
    19,218.8h  0.64%  Wetter
    11,167.4h  0.37%  Programmende
    9,515.0h   0.32%  E-Sport
    8,676.6h   0.29%  Bericht
    7,771.3h   0.26%  Event
    6,992.9h   0.23%  Kurzfilm
    6,299.9h   0.21%  Videoclip
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
