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

**197** channels, **3,011,201*** programs, **2,009,543.6** hours playtime between **2023-01-17** and **2025-08-07**


### playtime per genre (top 30)

    529,105.3h 26.33% Serie
    316,134.8h 15.73% Magazin
    246,548.7h 12.27% Dokumentation
    177,646.0h 8.84%  Show
    173,346.4h 8.63%  Werbung
    154,583.0h 7.69%  Spielfilm
    127,915.6h 6.37%  Nachrichten
    119,803.3h 5.96%  Sport
    40,572.6h  2.02%  Reportage
    39,715.9h  1.98%  Musik
    18,984.0h  0.94%  Verschiedenes
    14,658.6h  0.73%  Wetter
    11,167.4h  0.56%  Programmende
    9,515.0h   0.47%  E-Sport
    6,733.1h   0.34%  Bericht
    5,947.8h   0.30%  Event
    3,622.6h   0.18%  Videoclip
    3,541.9h   0.18%  *unknown*
    3,495.4h   0.17%  Kurzfilm
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
