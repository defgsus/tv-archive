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

**197** channels, **2,554,249*** programs, **1,680,974.1** hours playtime between **2023-01-17** and **2025-05-23**


### playtime per genre (top 30)

    436,311.4h 25.96% Serie
    278,050.3h 16.54% Magazin
    202,918.0h 12.07% Dokumentation
    153,693.4h 9.14%  Werbung
    153,084.6h 9.11%  Show
    117,757.2h 7.01%  Spielfilm
    115,812.5h 6.89%  Nachrichten
    86,602.7h  5.15%  Sport
    34,735.3h  2.07%  Reportage
    28,492.2h  1.69%  Musik
    13,174.8h  0.78%  Wetter
    13,162.5h  0.78%  Verschiedenes
    11,167.4h  0.66%  Programmende
    9,515.0h   0.57%  E-Sport
    6,210.0h   0.37%  Bericht
    5,406.4h   0.32%  Event
    3,541.9h   0.21%  *unknown*
    2,786.0h   0.17%  Videoclip
    2,046.0h   0.12%  Kurzfilm
    2,045.6h   0.12%  Verkaufsshow
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
