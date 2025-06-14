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

**197** channels, **2,687,090*** programs, **1,776,536.9** hours playtime between **2023-01-17** and **2025-06-14**


### playtime per genre (top 30)

    463,129.3h 26.07% Serie
    288,908.5h 16.26% Magazin
    215,481.3h 12.13% Dokumentation
    160,352.5h 9.03%  Show
    159,492.5h 8.98%  Werbung
    128,827.3h 7.25%  Spielfilm
    119,254.4h 6.71%  Nachrichten
    96,370.9h  5.42%  Sport
    36,433.8h  2.05%  Reportage
    31,758.9h  1.79%  Musik
    14,816.0h  0.83%  Verschiedenes
    13,600.5h  0.77%  Wetter
    11,167.4h  0.63%  Programmende
    9,515.0h   0.54%  E-Sport
    6,328.1h   0.36%  Bericht
    5,577.9h   0.31%  Event
    3,541.9h   0.20%  *unknown*
    3,009.0h   0.17%  Videoclip
    2,465.2h   0.14%  Kurzfilm
    2,045.6h   0.12%  Verkaufsshow
    353.9h     0.02%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
