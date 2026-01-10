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

**197** channels, **3,938,093*** programs, **2,682,147.0** hours playtime between **2023-01-17** and **2026-01-10**


### playtime per genre (top 30)

    715,956.1h 26.69% Serie
    395,017.8h 14.73% Magazin
    337,542.1h 12.58% Dokumentation
    234,039.8h 8.73%  Spielfilm
    227,621.8h 8.49%  Show
    212,779.5h 7.93%  Werbung
    185,459.4h 6.91%  Sport
    153,639.5h 5.73%  Nachrichten
    61,110.0h  2.28%  Musik
    52,229.2h  1.95%  Reportage
    31,060.2h  1.16%  Verschiedenes
    17,787.2h  0.66%  Wetter
    11,167.4h  0.42%  Programmende
    9,515.0h   0.35%  E-Sport
    8,071.9h   0.30%  Bericht
    7,194.7h   0.27%  Event
    6,386.9h   0.24%  Kurzfilm
    5,500.3h   0.21%  Videoclip
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
