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

**198** channels, **4,289,055*** programs, **2,932,255.3** hours playtime between **2023-01-17** and **2026-03-11**


### playtime per genre (top 30)

    788,576.5h 26.89% Serie
    424,622.7h 14.48% Magazin
    372,405.5h 12.70% Dokumentation
    261,473.5h 8.92%  Spielfilm
    246,577.9h 8.41%  Show
    227,471.4h 7.76%  Werbung
    211,730.7h 7.22%  Sport
    163,604.4h 5.58%  Nachrichten
    65,678.3h  2.24%  Musik
    56,898.1h  1.94%  Reportage
    34,287.9h  1.17%  Verschiedenes
    18,910.7h  0.64%  Wetter
    11,167.4h  0.38%  Programmende
    9,515.0h   0.32%  E-Sport
    8,510.8h   0.29%  Bericht
    7,642.9h   0.26%  Event
    6,974.9h   0.24%  Kurzfilm
    6,138.6h   0.21%  Videoclip
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
    147.0h     0.01%  Wirtschaftsmagazin
