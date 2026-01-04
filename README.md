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

**197** channels, **3,902,564*** programs, **2,656,723.2** hours playtime between **2023-01-17** and **2026-01-04**


### playtime per genre (top 30)

    708,551.7h 26.67% Serie
    392,024.8h 14.76% Magazin
    333,917.8h 12.57% Dokumentation
    230,969.1h 8.69%  Spielfilm
    225,891.5h 8.50%  Show
    211,318.0h 7.95%  Werbung
    183,012.4h 6.89%  Sport
    152,638.4h 5.75%  Nachrichten
    60,652.3h  2.28%  Musik
    51,830.7h  1.95%  Reportage
    30,606.0h  1.15%  Verschiedenes
    17,660.3h  0.66%  Wetter
    11,167.4h  0.42%  Programmende
    9,515.0h   0.36%  E-Sport
    8,045.5h   0.30%  Bericht
    7,138.4h   0.27%  Event
    6,282.9h   0.24%  Kurzfilm
    5,432.4h   0.20%  Videoclip
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
