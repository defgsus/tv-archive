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

**197** channels, **3,458,979*** programs, **2,332,506.6** hours playtime between **2023-01-17** and **2025-10-21**


### playtime per genre (top 30)

    620,227.5h 26.59% Serie
    354,090.3h 15.18% Magazin
    290,455.7h 12.45% Dokumentation
    201,990.9h 8.66%  Show
    192,469.9h 8.25%  Werbung
    190,193.4h 8.15%  Spielfilm
    151,193.4h 6.48%  Sport
    140,245.8h 6.01%  Nachrichten
    49,891.2h  2.14%  Musik
    46,220.8h  1.98%  Reportage
    25,271.3h  1.08%  Verschiedenes
    16,169.5h  0.69%  Wetter
    11,167.4h  0.48%  Programmende
    9,515.0h   0.41%  E-Sport
    7,481.4h   0.32%  Bericht
    6,513.6h   0.28%  Event
    4,822.8h   0.21%  Kurzfilm
    4,535.2h   0.19%  Videoclip
    3,541.9h   0.15%  *unknown*
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
