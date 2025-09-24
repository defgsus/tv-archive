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

**197** channels, **3,298,698*** programs, **2,216,033.4** hours playtime between **2023-01-17** and **2025-09-24**


### playtime per genre (top 30)

    587,654.4h 26.52% Serie
    340,176.6h 15.35% Magazin
    274,659.9h 12.39% Dokumentation
    193,087.0h 8.71%  Show
    185,682.6h 8.38%  Werbung
    177,318.3h 8.00%  Spielfilm
    139,946.7h 6.32%  Sport
    135,753.2h 6.13%  Nachrichten
    45,975.4h  2.07%  Musik
    44,276.0h  2.00%  Reportage
    23,227.7h  1.05%  Verschiedenes
    15,637.1h  0.71%  Wetter
    11,167.4h  0.50%  Programmende
    9,515.0h   0.43%  E-Sport
    7,010.8h   0.32%  Bericht
    6,318.7h   0.29%  Event
    4,353.9h   0.20%  Kurzfilm
    4,224.3h   0.19%  Videoclip
    3,541.9h   0.16%  *unknown*
    2,045.6h   0.09%  Verkaufsshow
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
