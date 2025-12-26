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

**197** channels, **3,851,557*** programs, **2,618,013.3** hours playtime between **2023-01-17** and **2025-12-26**


### playtime per genre (top 30)

    699,076.8h 26.70% Serie
    388,219.8h 14.83% Magazin
    328,420.5h 12.54% Dokumentation
    224,147.6h 8.56%  Spielfilm
    222,859.6h 8.51%  Show
    209,281.1h 7.99%  Werbung
    179,205.6h 6.85%  Sport
    151,363.3h 5.78%  Nachrichten
    59,609.0h  2.28%  Musik
    51,157.8h  1.95%  Reportage
    29,970.2h  1.14%  Verschiedenes
    17,471.6h  0.67%  Wetter
    11,167.4h  0.43%  Programmende
    9,515.0h   0.36%  E-Sport
    8,029.4h   0.31%  Bericht
    7,022.5h   0.27%  Event
    6,102.5h   0.23%  Kurzfilm
    5,327.2h   0.20%  Videoclip
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
