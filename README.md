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

**197** channels, **3,709,469*** programs, **2,514,403.9** hours playtime between **2023-01-17** and **2025-12-02**


### playtime per genre (top 30)

    670,715.9h 26.67% Serie
    376,087.4h 14.96% Magazin
    314,716.6h 12.52% Dokumentation
    215,437.5h 8.57%  Show
    210,958.2h 8.39%  Spielfilm
    203,461.3h 8.09%  Werbung
    168,997.3h 6.72%  Sport
    147,427.5h 5.86%  Nachrichten
    56,074.2h  2.23%  Musik
    49,323.6h  1.96%  Reportage
    28,182.5h  1.12%  Verschiedenes
    16,979.0h  0.68%  Wetter
    11,167.4h  0.44%  Programmende
    9,515.0h   0.38%  E-Sport
    7,815.0h   0.31%  Bericht
    6,823.2h   0.27%  Event
    5,626.6h   0.22%  Kurzfilm
    5,033.3h   0.20%  Videoclip
    3,541.9h   0.14%  *unknown*
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
