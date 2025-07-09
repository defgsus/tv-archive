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

**197** channels, **2,836,999*** programs, **1,884,479.1** hours playtime between **2023-01-17** and **2025-07-09**


### playtime per genre (top 30)

    493,550.3h 26.19% Serie
    301,601.8h 16.00% Magazin
    229,679.8h 12.19% Dokumentation
    168,662.6h 8.95%  Show
    166,076.8h 8.81%  Werbung
    140,862.8h 7.47%  Spielfilm
    123,102.9h 6.53%  Nachrichten
    107,181.0h 5.69%  Sport
    38,331.6h  2.03%  Reportage
    35,517.4h  1.88%  Musik
    16,608.5h  0.88%  Verschiedenes
    14,090.1h  0.75%  Wetter
    11,167.4h  0.59%  Programmende
    9,515.0h   0.50%  E-Sport
    6,550.2h   0.35%  Bericht
    5,740.5h   0.30%  Event
    3,541.9h   0.19%  *unknown*
    3,252.6h   0.17%  Videoclip
    2,939.6h   0.16%  Kurzfilm
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
