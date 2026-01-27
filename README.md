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

**197** channels, **4,038,829*** programs, **2,753,929.6** hours playtime between **2023-01-17** and **2026-01-27**


### playtime per genre (top 30)

    736,743.9h 26.75% Serie
    403,208.2h 14.64% Magazin
    347,541.0h 12.62% Dokumentation
    242,363.2h 8.80%  Spielfilm
    232,816.4h 8.45%  Show
    217,006.1h 7.88%  Werbung
    192,982.9h 7.01%  Sport
    156,438.1h 5.68%  Nachrichten
    62,399.5h  2.27%  Musik
    53,518.0h  1.94%  Reportage
    32,227.0h  1.17%  Verschiedenes
    18,125.6h  0.66%  Wetter
    11,167.4h  0.41%  Programmende
    9,515.0h   0.35%  E-Sport
    8,158.6h   0.30%  Bericht
    7,303.4h   0.27%  Event
    6,663.1h   0.24%  Kurzfilm
    5,683.9h   0.21%  Videoclip
    3,541.9h   0.13%  *unknown*
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
    147.0h     0.01%  Wirtschaftsmagazin
