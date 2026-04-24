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

**198** channels, **4,541,648*** programs, **3,112,297.9** hours playtime between **2023-01-17** and **2026-04-24**


### playtime per genre (top 30)

    841,467.0h 27.04% Serie
    445,936.4h 14.33% Magazin
    397,876.3h 12.78% Dokumentation
    280,959.9h 9.03%  Spielfilm
    259,995.8h 8.35%  Show
    238,039.9h 7.65%  Werbung
    230,293.2h 7.40%  Sport
    171,294.0h 5.50%  Nachrichten
    69,090.9h  2.22%  Musik
    60,326.6h  1.94%  Reportage
    36,072.6h  1.16%  Verschiedenes
    19,754.3h  0.63%  Wetter
    11,167.4h  0.36%  Programmende
    9,515.0h   0.31%  E-Sport
    8,844.7h   0.28%  Bericht
    7,990.0h   0.26%  Event
    7,024.1h   0.23%  Kurzfilm
    6,581.3h   0.21%  Videoclip
    3,541.9h   0.11%  *unknown*
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
    147.0h     0.00%  Wirtschaftsmagazin
