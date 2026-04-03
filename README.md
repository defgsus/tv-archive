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

**198** channels, **4,421,579*** programs, **3,026,393.3** hours playtime between **2023-01-17** and **2026-04-03**


### playtime per genre (top 30)

    816,407.9h 26.98% Serie
    436,200.4h 14.41% Magazin
    385,633.4h 12.74% Dokumentation
    271,099.1h 8.96%  Spielfilm
    253,766.5h 8.39%  Show
    233,044.6h 7.70%  Werbung
    221,322.8h 7.31%  Sport
    167,574.2h 5.54%  Nachrichten
    67,452.6h  2.23%  Musik
    58,703.9h  1.94%  Reportage
    35,190.3h  1.16%  Verschiedenes
    19,350.7h  0.64%  Wetter
    11,167.4h  0.37%  Programmende
    9,515.0h   0.31%  E-Sport
    8,707.8h   0.29%  Bericht
    7,821.0h   0.26%  Event
    6,996.8h   0.23%  Kurzfilm
    6,370.3h   0.21%  Videoclip
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
