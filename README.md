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

**197** channels, **3,673,660*** programs, **2,488,361.4** hours playtime between **2023-01-17** and **2025-11-26**


### playtime per genre (top 30)

    663,548.5h 26.67% Serie
    372,934.6h 14.99% Magazin
    311,235.4h 12.51% Dokumentation
    213,559.6h 8.58%  Show
    207,932.6h 8.36%  Spielfilm
    201,888.0h 8.11%  Werbung
    166,420.8h 6.69%  Sport
    146,410.4h 5.88%  Nachrichten
    55,165.2h  2.22%  Musik
    48,901.1h  1.97%  Reportage
    27,763.5h  1.12%  Verschiedenes
    16,859.1h  0.68%  Wetter
    11,167.4h  0.45%  Programmende
    9,515.0h   0.38%  E-Sport
    7,755.8h   0.31%  Bericht
    6,766.1h   0.27%  Event
    5,514.6h   0.22%  Kurzfilm
    4,962.2h   0.20%  Videoclip
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
