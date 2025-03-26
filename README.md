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

**195** channels, **2,208,067*** programs, **1,431,083.6** hours playtime between **2023-01-17** and **2025-03-26**


### playtime per genre (top 30)

    366,141.4h 25.58% Serie
    249,086.0h 17.41% Magazin
    170,052.1h 11.88% Dokumentation
    138,193.5h 9.66%  Werbung
    133,956.4h 9.36%  Show
    106,280.1h 7.43%  Nachrichten
    89,982.9h  6.29%  Spielfilm
    61,563.2h  4.30%  Sport
    30,293.8h  2.12%  Reportage
    19,968.9h  1.40%  Musik
    12,136.4h  0.85%  Wetter
    11,167.4h  0.78%  Programmende
    9,515.0h   0.66%  E-Sport
    8,849.2h   0.62%  Verschiedenes
    5,736.8h   0.40%  Bericht
    4,941.6h   0.35%  Event
    3,541.9h   0.25%  *unknown*
    2,222.3h   0.16%  Videoclip
    2,045.6h   0.14%  Verkaufsshow
    951.2h     0.07%  Kurzfilm
    353.9h     0.02%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.02%  Darts
    232.8h     0.02%  Handball
    219.5h     0.02%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
