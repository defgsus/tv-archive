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

**197** channels, **3,017,322*** programs, **2,013,855.0** hours playtime between **2023-01-17** and **2025-08-08**


### playtime per genre (top 30)

    530,387.9h 26.34% Serie
    316,643.8h 15.72% Magazin
    247,115.6h 12.27% Dokumentation
    177,953.4h 8.84%  Show
    173,606.1h 8.62%  Werbung
    154,979.4h 7.70%  Spielfilm
    128,109.1h 6.36%  Nachrichten
    120,207.2h 5.97%  Sport
    40,664.2h  2.02%  Reportage
    39,826.9h  1.98%  Musik
    19,113.3h  0.95%  Verschiedenes
    14,680.4h  0.73%  Wetter
    11,167.4h  0.55%  Programmende
    9,515.0h   0.47%  E-Sport
    6,734.4h   0.33%  Bericht
    5,952.9h   0.30%  Event
    3,636.4h   0.18%  Videoclip
    3,541.9h   0.18%  *unknown*
    3,513.4h   0.17%  Kurzfilm
    2,045.6h   0.10%  Verkaufsshow
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
