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

**203** channels, **4,837,773*** programs, **3,324,448.3** hours playtime between **2023-01-17** and **2026-06-15**


### playtime per genre (top 30)

    903,264.7h 27.17% Serie
    470,060.2h 14.14% Magazin
    428,570.7h 12.89% Dokumentation
    304,211.8h 9.15%  Spielfilm
    275,791.7h 8.30%  Show
    252,609.6h 7.60%  Sport
    250,060.9h 7.52%  Werbung
    181,174.1h 5.45%  Nachrichten
    73,096.9h  2.20%  Musik
    63,987.7h  1.92%  Reportage
    38,256.8h  1.15%  Verschiedenes
    20,744.5h  0.62%  Wetter
    11,167.4h  0.34%  Programmende
    9,515.0h   0.29%  E-Sport
    9,210.2h   0.28%  Bericht
    8,413.9h   0.25%  Event
    7,136.8h   0.21%  Kurzfilm
    7,106.9h   0.21%  Videoclip
    3,541.9h   0.11%  *unknown*
    2,045.6h   0.06%  Verkaufsshow
    353.9h     0.01%  Eishockey
    299.8h     0.01%  Judo
    257.0h     0.01%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.00%  Fußball
    147.0h     0.00%  Wirtschaftsmagazin
