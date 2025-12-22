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

**197** channels, **3,828,640*** programs, **2,600,661.9** hours playtime between **2023-01-17** and **2025-12-22**


### playtime per genre (top 30)

    694,807.8h 26.72% Serie
    386,457.5h 14.86% Magazin
    325,929.3h 12.53% Dokumentation
    221,675.1h 8.52%  Show
    221,077.2h 8.50%  Spielfilm
    208,317.0h 8.01%  Werbung
    177,614.7h 6.83%  Sport
    150,773.3h 5.80%  Nachrichten
    59,055.9h  2.27%  Musik
    50,887.2h  1.96%  Reportage
    29,660.4h  1.14%  Verschiedenes
    17,389.8h  0.67%  Wetter
    11,167.4h  0.43%  Programmende
    9,515.0h   0.37%  E-Sport
    8,023.3h   0.31%  Bericht
    6,973.1h   0.27%  Event
    6,008.9h   0.23%  Kurzfilm
    5,262.6h   0.20%  Videoclip
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
