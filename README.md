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

**200** channels, **4,769,070*** programs, **3,275,306.5** hours playtime between **2023-01-17** and **2026-06-03**


### playtime per genre (top 30)

    889,059.7h 27.14% Serie
    464,421.2h 14.18% Magazin
    421,446.8h 12.87% Dokumentation
    298,924.7h 9.13%  Spielfilm
    272,080.5h 8.31%  Show
    247,429.4h 7.55%  Werbung
    247,346.3h 7.55%  Sport
    178,851.5h 5.46%  Nachrichten
    72,153.4h  2.20%  Musik
    63,166.4h  1.93%  Reportage
    37,642.4h  1.15%  Verschiedenes
    20,514.0h  0.63%  Wetter
    11,167.4h  0.34%  Programmende
    9,515.0h   0.29%  E-Sport
    9,099.4h   0.28%  Bericht
    8,310.9h   0.25%  Event
    7,121.5h   0.22%  Kurzfilm
    6,987.4h   0.21%  Videoclip
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
