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

**197** channels, **3,891,048*** programs, **2,648,201.3** hours playtime between **2023-01-17** and **2026-01-02**


### playtime per genre (top 30)

    706,281.4h 26.67% Serie
    391,148.2h 14.77% Magazin
    332,703.2h 12.56% Dokumentation
    229,639.9h 8.67%  Spielfilm
    225,253.9h 8.51%  Show
    210,837.0h 7.96%  Werbung
    182,157.0h 6.88%  Sport
    152,343.6h 5.75%  Nachrichten
    60,484.0h  2.28%  Musik
    51,686.3h  1.95%  Reportage
    30,467.5h  1.15%  Verschiedenes
    17,615.2h  0.67%  Wetter
    11,167.4h  0.42%  Programmende
    9,515.0h   0.36%  E-Sport
    8,040.9h   0.30%  Bericht
    7,126.8h   0.27%  Event
    6,252.8h   0.24%  Kurzfilm
    5,413.1h   0.20%  Videoclip
    3,541.9h   0.13%  *unknown*
    2,045.6h   0.08%  Verkaufsshow
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
