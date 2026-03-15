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

**198** channels, **4,312,200*** programs, **2,948,741.1** hours playtime between **2023-01-17** and **2026-03-15**


### playtime per genre (top 30)

    793,449.7h 26.91% Serie
    426,693.2h 14.47% Magazin
    374,642.2h 12.71% Dokumentation
    263,150.9h 8.92%  Spielfilm
    247,880.7h 8.41%  Show
    228,495.4h 7.75%  Werbung
    213,419.2h 7.24%  Sport
    164,296.7h 5.57%  Nachrichten
    65,989.8h  2.24%  Musik
    57,177.2h  1.94%  Reportage
    34,449.1h  1.17%  Verschiedenes
    18,985.7h  0.64%  Wetter
    11,167.4h  0.38%  Programmende
    9,515.0h   0.32%  E-Sport
    8,537.5h   0.29%  Bericht
    7,668.6h   0.26%  Event
    6,979.1h   0.24%  Kurzfilm
    6,175.4h   0.21%  Videoclip
    3,541.9h   0.12%  *unknown*
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
    147.0h     0.00%  Wirtschaftsmagazin
