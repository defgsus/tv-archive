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

**200** channels, **4,724,362*** programs, **3,243,260.6** hours playtime between **2023-01-17** and **2026-05-26**


### playtime per genre (top 30)

    879,459.9h 27.12% Serie
    460,750.6h 14.21% Magazin
    416,721.2h 12.85% Dokumentation
    295,566.8h 9.11%  Spielfilm
    269,821.5h 8.32%  Show
    245,627.0h 7.57%  Werbung
    244,051.6h 7.52%  Sport
    177,272.3h 5.47%  Nachrichten
    71,572.9h  2.21%  Musik
    62,647.6h  1.93%  Reportage
    37,334.9h  1.15%  Verschiedenes
    20,358.5h  0.63%  Wetter
    11,167.4h  0.34%  Programmende
    9,515.0h   0.29%  E-Sport
    9,063.8h   0.28%  Bericht
    8,249.9h   0.25%  Event
    7,107.0h   0.22%  Kurzfilm
    6,904.2h   0.21%  Videoclip
    3,541.9h   0.11%  *unknown*
    2,045.6h   0.06%  Verkaufsshow
    353.9h     0.01%  Eishockey
    299.8h     0.01%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.00%  Fußball
    147.0h     0.00%  Wirtschaftsmagazin
