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

**197** channels, **2,403,829*** programs, **1,572,739.6** hours playtime between **2023-01-17** and **2025-04-28**


### playtime per genre (top 30)

    405,357.5h 25.77% Serie
    265,452.0h 16.88% Magazin
    189,025.4h 12.02% Dokumentation
    147,029.5h 9.35%  Werbung
    144,845.1h 9.21%  Show
    111,655.9h 7.10%  Nachrichten
    106,204.6h 6.75%  Spielfilm
    75,618.8h  4.81%  Sport
    32,738.8h  2.08%  Reportage
    24,751.8h  1.57%  Musik
    12,732.0h  0.81%  Wetter
    11,296.2h  0.72%  Verschiedenes
    11,167.4h  0.71%  Programmende
    9,515.0h   0.60%  E-Sport
    5,963.6h   0.38%  Bericht
    5,213.1h   0.33%  Event
    3,541.9h   0.23%  *unknown*
    2,540.4h   0.16%  Videoclip
    2,045.6h   0.13%  Verkaufsshow
    1,585.1h   0.10%  Kurzfilm
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
