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

**198** channels, **4,673,581*** programs, **3,206,354.5** hours playtime between **2023-01-17** and **2026-05-17**


### playtime per genre (top 30)

    869,082.5h 27.11% Serie
    456,712.2h 14.24% Magazin
    411,404.1h 12.83% Dokumentation
    291,156.4h 9.08%  Spielfilm
    267,067.5h 8.33%  Show
    243,514.5h 7.59%  Werbung
    239,995.5h 7.48%  Sport
    175,623.9h 5.48%  Nachrichten
    70,855.6h  2.21%  Musik
    61,970.3h  1.93%  Reportage
    36,983.5h  1.15%  Verschiedenes
    20,196.2h  0.63%  Wetter
    11,167.4h  0.35%  Programmende
    9,515.0h   0.30%  E-Sport
    8,972.9h   0.28%  Bericht
    8,183.6h   0.26%  Event
    7,074.4h   0.22%  Kurzfilm
    6,810.7h   0.21%  Videoclip
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
