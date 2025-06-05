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

**197** channels, **2,632,700*** programs, **1,737,365.7** hours playtime between **2023-01-17** and **2025-06-05**


### playtime per genre (top 30)

    452,206.2h 26.03% Serie
    284,457.2h 16.37% Magazin
    210,431.1h 12.11% Dokumentation
    157,323.1h 9.06%  Show
    157,118.0h 9.04%  Werbung
    124,119.6h 7.14%  Spielfilm
    117,841.2h 6.78%  Nachrichten
    92,451.6h  5.32%  Sport
    35,713.2h  2.06%  Reportage
    30,408.5h  1.75%  Musik
    14,139.0h  0.81%  Verschiedenes
    13,426.6h  0.77%  Wetter
    11,167.4h  0.64%  Programmende
    9,515.0h   0.55%  E-Sport
    6,275.2h   0.36%  Bericht
    5,511.4h   0.32%  Event
    3,541.9h   0.20%  *unknown*
    2,916.6h   0.17%  Videoclip
    2,296.3h   0.13%  Kurzfilm
    2,045.6h   0.12%  Verkaufsshow
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
