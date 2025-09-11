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

**197** channels, **3,221,309*** programs, **2,159,927.9** hours playtime between **2023-01-17** and **2025-09-11**


### playtime per genre (top 30)

    571,872.9h 26.48% Serie
    333,504.9h 15.44% Magazin
    267,051.0h 12.36% Dokumentation
    188,756.3h 8.74%  Show
    182,499.2h 8.45%  Werbung
    171,246.9h 7.93%  Spielfilm
    134,309.3h 6.22%  Sport
    133,591.5h 6.18%  Nachrichten
    44,252.5h  2.05%  Musik
    43,291.9h  2.00%  Reportage
    22,172.9h  1.03%  Verschiedenes
    15,383.0h  0.71%  Wetter
    11,167.4h  0.52%  Programmende
    9,515.0h   0.44%  E-Sport
    6,846.9h   0.32%  Bericht
    6,216.8h   0.29%  Event
    4,126.9h   0.19%  Kurzfilm
    4,074.2h   0.19%  Videoclip
    3,541.9h   0.16%  *unknown*
    2,045.6h   0.09%  Verkaufsshow
    353.9h     0.02%  Eishockey
    299.8h     0.01%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
