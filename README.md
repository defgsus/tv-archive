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

**197** channels, **3,745,336*** programs, **2,540,316.8** hours playtime between **2023-01-17** and **2025-12-08**


### playtime per genre (top 30)

    677,954.8h 26.69% Serie
    379,272.8h 14.93% Magazin
    318,101.9h 12.52% Dokumentation
    217,327.2h 8.56%  Show
    213,880.0h 8.42%  Spielfilm
    204,943.0h 8.07%  Werbung
    171,591.9h 6.75%  Sport
    148,433.0h 5.84%  Nachrichten
    56,977.5h  2.24%  Musik
    49,809.2h  1.96%  Reportage
    28,609.8h  1.13%  Verschiedenes
    17,094.6h  0.67%  Wetter
    11,167.4h  0.44%  Programmende
    9,515.0h   0.37%  E-Sport
    7,856.4h   0.31%  Bericht
    6,875.8h   0.27%  Event
    5,741.1h   0.23%  Kurzfilm
    5,101.1h   0.20%  Videoclip
    3,541.9h   0.14%  *unknown*
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
