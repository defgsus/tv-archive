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

**195** channels, **2,255,934*** programs, **1,465,449.0** hours playtime between **2023-01-17** and **2025-04-03**


### playtime per genre (top 30)

    375,745.3h 25.64% Serie
    253,091.9h 17.27% Magazin
    174,630.4h 11.92% Dokumentation
    140,364.6h 9.58%  Werbung
    136,659.6h 9.33%  Show
    107,640.1h 7.35%  Nachrichten
    93,558.6h  6.38%  Spielfilm
    65,064.9h  4.44%  Sport
    30,858.1h  2.11%  Reportage
    21,147.8h  1.44%  Musik
    12,284.2h  0.84%  Wetter
    11,167.4h  0.76%  Programmende
    9,515.0h   0.65%  E-Sport
    9,457.1h   0.65%  Verschiedenes
    5,818.3h   0.40%  Bericht
    4,992.8h   0.34%  Event
    3,541.9h   0.24%  *unknown*
    2,299.7h   0.16%  Videoclip
    2,045.6h   0.14%  Verkaufsshow
    1,105.8h   0.08%  Kurzfilm
    353.9h     0.02%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.02%  Darts
    232.8h     0.02%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
