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

**197** channels, **2,566,158*** programs, **1,689,661.3** hours playtime between **2023-01-17** and **2025-05-25**


### playtime per genre (top 30)

    438,733.5h 25.97% Serie
    279,001.0h 16.51% Magazin
    204,071.9h 12.08% Dokumentation
    154,220.2h 9.13%  Werbung
    153,766.7h 9.10%  Show
    118,776.9h 7.03%  Spielfilm
    116,109.2h 6.87%  Nachrichten
    87,533.1h  5.18%  Sport
    34,869.7h  2.06%  Reportage
    28,803.6h  1.70%  Musik
    13,311.4h  0.79%  Verschiedenes
    13,209.4h  0.78%  Wetter
    11,167.4h  0.66%  Programmende
    9,515.0h   0.56%  E-Sport
    6,222.8h   0.37%  Bericht
    5,417.2h   0.32%  Event
    3,541.9h   0.21%  *unknown*
    2,804.2h   0.17%  Videoclip
    2,079.7h   0.12%  Kurzfilm
    2,045.6h   0.12%  Verkaufsshow
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
