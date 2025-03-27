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

**195** channels, **2,214,063*** programs, **1,435,333.6** hours playtime between **2023-01-17** and **2025-03-27**


### playtime per genre (top 30)

    367,359.8h 25.59% Serie
    249,601.8h 17.39% Magazin
    170,567.3h 11.88% Dokumentation
    138,467.4h 9.65%  Werbung
    134,283.9h 9.36%  Show
    106,465.8h 7.42%  Nachrichten
    90,381.6h  6.30%  Spielfilm
    61,991.3h  4.32%  Sport
    30,368.8h  2.12%  Reportage
    20,120.0h  1.40%  Musik
    12,155.3h  0.85%  Wetter
    11,167.4h  0.78%  Programmende
    9,515.0h   0.66%  E-Sport
    8,931.3h   0.62%  Verschiedenes
    5,760.1h   0.40%  Bericht
    4,946.7h   0.34%  Event
    3,541.9h   0.25%  *unknown*
    2,232.8h   0.16%  Videoclip
    2,045.6h   0.14%  Verkaufsshow
    972.1h     0.07%  Kurzfilm
    353.9h     0.02%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.02%  Darts
    232.8h     0.02%  Handball
    219.5h     0.02%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
