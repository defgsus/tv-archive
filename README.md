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

**198** channels, **4,220,527*** programs, **2,883,413.3** hours playtime between **2023-01-17** and **2026-02-27**


### playtime per genre (top 30)

    774,083.9h 26.85% Serie
    418,757.6h 14.52% Magazin
    365,546.2h 12.68% Dokumentation
    256,297.0h 8.89%  Spielfilm
    242,835.4h 8.42%  Show
    224,661.1h 7.79%  Werbung
    206,713.5h 7.17%  Sport
    161,661.6h 5.61%  Nachrichten
    64,767.1h  2.25%  Musik
    55,899.2h  1.94%  Reportage
    33,794.2h  1.17%  Verschiedenes
    18,705.7h  0.65%  Wetter
    11,167.4h  0.39%  Programmende
    9,515.0h   0.33%  E-Sport
    8,409.6h   0.29%  Bericht
    7,550.2h   0.26%  Event
    6,962.9h   0.24%  Kurzfilm
    6,017.3h   0.21%  Videoclip
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
