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

**197** channels, **2,602,408*** programs, **1,715,711.8** hours playtime between **2023-01-17** and **2025-05-31**


### playtime per genre (top 30)

    446,030.4h 26.00% Serie
    281,986.1h 16.44% Magazin
    207,637.5h 12.10% Dokumentation
    155,778.1h 9.08%  Werbung
    155,701.0h 9.08%  Show
    121,690.7h 7.09%  Spielfilm
    117,088.4h 6.82%  Nachrichten
    90,228.2h  5.26%  Sport
    35,301.6h  2.06%  Reportage
    29,673.7h  1.73%  Musik
    13,751.1h  0.80%  Verschiedenes
    13,328.1h  0.78%  Wetter
    11,167.4h  0.65%  Programmende
    9,515.0h   0.55%  E-Sport
    6,251.0h   0.36%  Bericht
    5,469.9h   0.32%  Event
    3,541.9h   0.21%  *unknown*
    2,866.0h   0.17%  Videoclip
    2,199.0h   0.13%  Kurzfilm
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
