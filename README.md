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

**197** channels, **3,817,318*** programs, **2,591,955.4** hours playtime between **2023-01-17** and **2025-12-20**


### playtime per genre (top 30)

    692,736.2h 26.73% Serie
    385,610.5h 14.88% Magazin
    324,779.2h 12.53% Dokumentation
    221,038.2h 8.53%  Show
    219,639.0h 8.47%  Spielfilm
    207,813.8h 8.02%  Werbung
    176,613.1h 6.81%  Sport
    150,509.3h 5.81%  Nachrichten
    58,739.9h  2.27%  Musik
    50,730.9h  1.96%  Reportage
    29,469.3h  1.14%  Verschiedenes
    17,354.9h  0.67%  Wetter
    11,167.4h  0.43%  Programmende
    9,515.0h   0.37%  E-Sport
    8,019.4h   0.31%  Bericht
    6,944.6h   0.27%  Event
    5,968.3h   0.23%  Kurzfilm
    5,240.0h   0.20%  Videoclip
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
