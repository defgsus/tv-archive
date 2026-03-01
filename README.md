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

**198** channels, **4,231,961*** programs, **2,891,610.2** hours playtime between **2023-01-17** and **2026-03-01**


### playtime per genre (top 30)

    776,417.7h 26.85% Serie
    419,681.4h 14.51% Magazin
    366,683.9h 12.68% Dokumentation
    257,274.9h 8.90%  Spielfilm
    243,494.5h 8.42%  Show
    225,160.2h 7.79%  Werbung
    207,580.8h 7.18%  Sport
    161,969.4h 5.60%  Nachrichten
    64,924.1h  2.25%  Musik
    56,054.4h  1.94%  Reportage
    33,895.8h  1.17%  Verschiedenes
    18,738.1h  0.65%  Wetter
    11,167.4h  0.39%  Programmende
    9,515.0h   0.33%  E-Sport
    8,421.3h   0.29%  Bericht
    7,564.6h   0.26%  Event
    6,964.3h   0.24%  Kurzfilm
    6,034.3h   0.21%  Videoclip
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
