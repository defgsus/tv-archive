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

**197** channels, **3,070,933*** programs, **2,052,423.4** hours playtime between **2023-01-17** and **2025-08-17**


### playtime per genre (top 30)

    541,496.4h 26.38% Serie
    320,867.9h 15.63% Magazin
    252,400.2h 12.30% Dokumentation
    180,682.9h 8.80%  Show
    175,951.0h 8.57%  Werbung
    159,413.1h 7.77%  Spielfilm
    129,475.7h 6.31%  Nachrichten
    124,019.4h 6.04%  Sport
    41,400.5h  2.02%  Reportage
    41,020.3h  2.00%  Musik
    19,889.3h  0.97%  Verschiedenes
    14,872.8h  0.72%  Wetter
    11,167.4h  0.54%  Programmende
    9,515.0h   0.46%  E-Sport
    6,754.7h   0.33%  Bericht
    6,016.2h   0.29%  Event
    3,756.2h   0.18%  Videoclip
    3,676.0h   0.18%  Kurzfilm
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
