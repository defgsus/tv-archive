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

**197** channels, **3,879,793*** programs, **2,639,633.7** hours playtime between **2023-01-17** and **2025-12-31**


### playtime per genre (top 30)

    704,303.1h 26.68% Serie
    390,339.4h 14.79% Magazin
    331,506.5h 12.56% Dokumentation
    228,044.5h 8.64%  Spielfilm
    224,372.5h 8.50%  Show
    210,432.2h 7.97%  Werbung
    181,339.8h 6.87%  Sport
    152,085.9h 5.76%  Nachrichten
    60,302.1h  2.28%  Musik
    51,556.9h  1.95%  Reportage
    30,320.7h  1.15%  Verschiedenes
    17,572.0h  0.67%  Wetter
    11,167.4h  0.42%  Programmende
    9,515.0h   0.36%  E-Sport
    8,037.7h   0.30%  Bericht
    7,079.4h   0.27%  Event
    6,201.1h   0.23%  Kurzfilm
    5,389.1h   0.20%  Videoclip
    3,541.9h   0.13%  *unknown*
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
