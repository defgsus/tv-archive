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

**197** channels, **3,172,911*** programs, **2,125,233.1** hours playtime between **2023-01-17** and **2025-09-03**


### playtime per genre (top 30)

    562,160.8h 26.45% Serie
    329,309.0h 15.50% Magazin
    262,316.2h 12.34% Dokumentation
    186,112.7h 8.76%  Show
    180,382.5h 8.49%  Werbung
    167,514.4h 7.88%  Spielfilm
    132,227.9h 6.22%  Nachrichten
    130,969.1h 6.16%  Sport
    43,201.4h  2.03%  Musik
    42,712.4h  2.01%  Reportage
    21,445.0h  1.01%  Verschiedenes
    15,220.0h  0.72%  Wetter
    11,167.4h  0.53%  Programmende
    9,515.0h   0.45%  E-Sport
    6,810.9h   0.32%  Bericht
    6,154.1h   0.29%  Event
    3,986.7h   0.19%  Kurzfilm
    3,979.2h   0.19%  Videoclip
    3,541.9h   0.17%  *unknown*
    2,045.6h   0.10%  Verkaufsshow
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
