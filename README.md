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

**197** channels, **2,529,693*** programs, **1,663,595.6** hours playtime between **2023-01-17** and **2025-05-19**


### playtime per genre (top 30)

    431,134.4h 25.92% Serie
    275,973.6h 16.59% Magazin
    200,726.1h 12.07% Dokumentation
    152,618.2h 9.17%  Werbung
    151,814.6h 9.13%  Show
    116,164.1h 6.98%  Spielfilm
    115,081.4h 6.92%  Nachrichten
    84,815.7h  5.10%  Sport
    34,415.5h  2.07%  Reportage
    27,887.3h  1.68%  Musik
    13,103.1h  0.79%  Wetter
    12,866.1h  0.77%  Verschiedenes
    11,167.4h  0.67%  Programmende
    9,515.0h   0.57%  E-Sport
    6,155.6h   0.37%  Bericht
    5,390.4h   0.32%  Event
    3,541.9h   0.21%  *unknown*
    2,746.8h   0.17%  Videoclip
    2,045.6h   0.12%  Verkaufsshow
    1,972.0h   0.12%  Kurzfilm
    353.9h     0.02%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.02%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
