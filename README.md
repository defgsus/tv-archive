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

**197** channels, **2,861,007*** programs, **1,901,660.3** hours playtime between **2023-01-17** and **2025-07-13**


### playtime per genre (top 30)

    498,418.2h 26.21% Serie
    303,632.7h 15.97% Magazin
    231,953.6h 12.20% Dokumentation
    169,947.0h 8.94%  Show
    167,120.3h 8.79%  Werbung
    142,656.0h 7.50%  Spielfilm
    123,720.8h 6.51%  Nachrichten
    108,932.1h 5.73%  Sport
    38,628.5h  2.03%  Reportage
    36,133.2h  1.90%  Musik
    16,907.2h  0.89%  Verschiedenes
    14,167.4h  0.75%  Wetter
    11,167.4h  0.59%  Programmende
    9,515.0h   0.50%  E-Sport
    6,638.5h   0.35%  Bericht
    5,765.7h   0.30%  Event
    3,541.9h   0.19%  *unknown*
    3,291.9h   0.17%  Videoclip
    3,016.5h   0.16%  Kurzfilm
    2,045.6h   0.11%  Verkaufsshow
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
