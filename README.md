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

**197** channels, **3,107,250*** programs, **2,078,087.5** hours playtime between **2023-01-17** and **2025-08-23**


### playtime per genre (top 30)

    548,976.0h 26.42% Serie
    323,934.2h 15.59% Magazin
    255,901.6h 12.31% Dokumentation
    182,495.1h 8.78%  Show
    177,498.5h 8.54%  Werbung
    162,163.6h 7.80%  Spielfilm
    130,469.1h 6.28%  Nachrichten
    126,457.9h 6.09%  Sport
    41,875.6h  2.02%  Reportage
    41,798.8h  2.01%  Musik
    20,339.8h  0.98%  Verschiedenes
    14,995.8h  0.72%  Wetter
    11,167.4h  0.54%  Programmende
    9,515.0h   0.46%  E-Sport
    6,771.5h   0.33%  Bericht
    6,062.5h   0.29%  Event
    3,834.7h   0.18%  Videoclip
    3,781.9h   0.18%  Kurzfilm
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
