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

**197** channels, **2,392,406*** programs, **1,564,141.1** hours playtime between **2023-01-17** and **2025-04-26**


### playtime per genre (top 30)

    403,164.4h 25.78% Serie
    264,547.1h 16.91% Magazin
    187,840.1h 12.01% Dokumentation
    146,495.4h 9.37%  Werbung
    144,143.3h 9.22%  Show
    111,394.9h 7.12%  Nachrichten
    105,036.6h 6.72%  Spielfilm
    74,669.4h  4.77%  Sport
    32,601.4h  2.08%  Reportage
    24,469.1h  1.56%  Musik
    12,700.6h  0.81%  Wetter
    11,167.4h  0.71%  Programmende
    11,149.8h  0.71%  Verschiedenes
    9,515.0h   0.61%  E-Sport
    5,952.1h   0.38%  Bericht
    5,172.6h   0.33%  Event
    3,541.9h   0.23%  *unknown*
    2,520.6h   0.16%  Videoclip
    2,045.6h   0.13%  Verkaufsshow
    1,554.0h   0.10%  Kurzfilm
    353.9h     0.02%  Eishockey
    299.8h     0.02%  Judo
    257.0h     0.02%  Darts
    232.8h     0.01%  Handball
    219.5h     0.01%  Dokureihe
    212.4h     0.01%  Leichtathletik
    190.7h     0.01%  Gespräch
    169.7h     0.01%  Erotikfilm
    157.3h     0.01%  Fußball
    147.0h     0.01%  Wirtschaftsmagazin
