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

**197** channels, **3,608,575*** programs, **2,441,044.2** hours playtime between **2023-01-17** and **2025-11-15**


### playtime per genre (top 30)

    650,717.8h 26.66% Serie
    367,255.3h 15.05% Magazin
    304,814.4h 12.49% Dokumentation
    210,031.7h 8.60%  Show
    202,370.6h 8.29%  Spielfilm
    199,026.8h 8.15%  Werbung
    161,749.0h 6.63%  Sport
    144,565.9h 5.92%  Nachrichten
    53,502.9h  2.19%  Musik
    48,085.1h  1.97%  Reportage
    27,037.0h  1.11%  Verschiedenes
    16,647.9h  0.68%  Wetter
    11,167.4h  0.46%  Programmende
    9,515.0h   0.39%  E-Sport
    7,677.4h   0.31%  Bericht
    6,680.9h   0.27%  Event
    5,307.6h   0.22%  Kurzfilm
    4,833.1h   0.20%  Videoclip
    3,541.9h   0.15%  *unknown*
    2,045.6h   0.08%  Verkaufsshow
    353.9h     0.01%  Eishockey
    299.8h     0.01%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
