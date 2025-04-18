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

**196** channels, **2,345,779*** programs, **1,529,677.1** hours playtime between **2023-01-17** and **2025-04-18**


### playtime per genre (top 30)

    393,961.2h 25.75% Serie
    260,747.6h 17.05% Magazin
    183,140.9h 11.97% Dokumentation
    144,445.0h 9.44%  Werbung
    141,654.3h 9.26%  Show
    110,142.1h 7.20%  Nachrichten
    100,252.2h 6.55%  Spielfilm
    71,346.2h  4.66%  Sport
    31,977.2h  2.09%  Reportage
    23,310.9h  1.52%  Musik
    12,556.9h  0.82%  Wetter
    11,167.4h  0.73%  Programmende
    10,561.8h  0.69%  Verschiedenes
    9,515.0h   0.62%  E-Sport
    5,911.1h   0.39%  Bericht
    5,100.6h   0.33%  Event
    3,541.9h   0.23%  *unknown*
    2,440.4h   0.16%  Videoclip
    2,045.6h   0.13%  Verkaufsshow
    1,399.2h   0.09%  Kurzfilm
    353.9h     0.02%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.02%  Darts
    232.8h     0.02%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
