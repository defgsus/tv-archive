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

**197** channels, **2,662,367*** programs, **1,759,116.5** hours playtime between **2023-01-17** and **2025-06-10**


### playtime per genre (top 30)

    458,062.3h 26.04% Serie
    286,759.0h 16.30% Magazin
    213,220.4h 12.12% Dokumentation
    159,055.9h 9.04%  Show
    158,405.7h 9.00%  Werbung
    127,130.4h 7.23%  Spielfilm
    118,545.9h 6.74%  Nachrichten
    94,696.9h  5.38%  Sport
    36,097.5h  2.05%  Reportage
    31,175.6h  1.77%  Musik
    14,512.9h  0.83%  Verschiedenes
    13,519.6h  0.77%  Wetter
    11,167.4h  0.63%  Programmende
    9,515.0h   0.54%  E-Sport
    6,297.0h   0.36%  Bericht
    5,549.7h   0.32%  Event
    3,541.9h   0.20%  *unknown*
    2,968.1h   0.17%  Videoclip
    2,389.1h   0.14%  Kurzfilm
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
