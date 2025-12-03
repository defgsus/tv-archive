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

**197** channels, **3,715,534*** programs, **2,518,707.3** hours playtime between **2023-01-17** and **2025-12-03**


### playtime per genre (top 30)

    671,950.7h 26.68% Serie
    376,640.2h 14.95% Magazin
    315,274.1h 12.52% Dokumentation
    215,739.7h 8.57%  Show
    211,388.7h 8.39%  Spielfilm
    203,715.7h 8.09%  Werbung
    169,404.3h 6.73%  Sport
    147,609.4h 5.86%  Nachrichten
    56,222.4h  2.23%  Musik
    49,427.9h  1.96%  Reportage
    28,248.8h  1.12%  Verschiedenes
    17,000.3h  0.67%  Wetter
    11,167.4h  0.44%  Programmende
    9,515.0h   0.38%  E-Sport
    7,821.3h   0.31%  Bericht
    6,828.0h   0.27%  Event
    5,646.8h   0.22%  Kurzfilm
    5,044.3h   0.20%  Videoclip
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
