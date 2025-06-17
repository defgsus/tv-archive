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

**197** channels, **2,704,789*** programs, **1,789,521.9** hours playtime between **2023-01-17** and **2025-06-17**


### playtime per genre (top 30)

    466,637.7h 26.08% Serie
    290,399.3h 16.23% Magazin
    217,220.4h 12.14% Dokumentation
    161,378.4h 9.02%  Show
    160,307.5h 8.96%  Werbung
    130,404.4h 7.29%  Spielfilm
    119,637.8h 6.69%  Nachrichten
    97,713.7h  5.46%  Sport
    36,667.5h  2.05%  Reportage
    32,223.5h  1.80%  Musik
    15,028.1h  0.84%  Verschiedenes
    13,656.1h  0.76%  Wetter
    11,167.4h  0.62%  Programmende
    9,515.0h   0.53%  E-Sport
    6,359.2h   0.36%  Bericht
    5,600.1h   0.31%  Event
    3,541.9h   0.20%  *unknown*
    3,037.3h   0.17%  Videoclip
    2,520.2h   0.14%  Kurzfilm
    2,045.6h   0.11%  Verkaufsshow
    353.9h     0.02%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
