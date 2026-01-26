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

**197** channels, **4,032,723*** programs, **2,749,707.2** hours playtime between **2023-01-17** and **2026-01-26**


### playtime per genre (top 30)

    735,445.9h 26.75% Serie
    402,703.0h 14.65% Magazin
    346,955.0h 12.62% Dokumentation
    241,962.5h 8.80%  Spielfilm
    232,517.8h 8.46%  Show
    216,755.1h 7.88%  Werbung
    192,560.2h 7.00%  Sport
    156,259.9h 5.68%  Nachrichten
    62,330.9h  2.27%  Musik
    53,431.7h  1.94%  Reportage
    32,162.5h  1.17%  Verschiedenes
    18,103.6h  0.66%  Wetter
    11,167.4h  0.41%  Programmende
    9,515.0h   0.35%  E-Sport
    8,153.6h   0.30%  Bericht
    7,298.1h   0.27%  Event
    6,645.1h   0.24%  Kurzfilm
    5,671.7h   0.21%  Videoclip
    3,541.9h   0.13%  *unknown*
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
