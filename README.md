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

**198** channels, **4,116,352*** programs, **2,808,964.3** hours playtime between **2023-01-17** and **2026-02-09**


### playtime per genre (top 30)

    752,337.4h 26.78% Serie
    409,669.0h 14.58% Magazin
    355,163.1h 12.64% Dokumentation
    248,748.1h 8.86%  Spielfilm
    237,047.6h 8.44%  Show
    220,195.2h 7.84%  Werbung
    198,661.7h 7.07%  Sport
    158,639.8h 5.65%  Nachrichten
    63,398.8h  2.26%  Musik
    54,519.1h  1.94%  Reportage
    33,091.0h  1.18%  Verschiedenes
    18,382.8h  0.65%  Wetter
    11,167.4h  0.40%  Programmende
    9,515.0h   0.34%  E-Sport
    8,236.4h   0.29%  Bericht
    7,396.1h   0.26%  Event
    6,901.8h   0.25%  Kurzfilm
    5,825.6h   0.21%  Videoclip
    3,541.9h   0.13%  *unknown*
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
