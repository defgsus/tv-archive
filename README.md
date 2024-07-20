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

**109** channels, **957,831.7** hours playtime between **2023-01-17** and **2024-07-21**


### playtime per genre (top 30)

    62387.2h 6.51% Nachrichten
    44747.2h 4.67% Verkaufsshow
    39234.3h 4.10% Krimiserie
    34195.7h 3.57% Werbesendung
    30100.1h 3.14% Dokureihe
    29010.2h 3.03% Dokusoap
    27861.0h 2.91% Regionalmagazin
    24877.3h 2.60% Dokumentation
    23872.5h 2.49% *unknown*
    17713.5h 1.85% Zeichentrickserie
    17504.7h 1.83% Infomercial
    17128.9h 1.79% Animationsserie
    14241.9h 1.49% Comedyserie
    13483.8h 1.41% Morgenmagazin
    13398.2h 1.40% Magazin
    12989.8h 1.36% Religionsmagazin
    12674.0h 1.32% Talkshow
    9481.0h  0.99% E-Sport
    9039.9h  0.94% Sitcom
    8697.0h  0.91% Programmende
    8585.9h  0.90% Wetterbericht
    8348.3h  0.87% Komödie
    8263.9h  0.86% Quiz
    7966.4h  0.83% Börsenmagazin
    7213.9h  0.75% Politikmagazin
    7111.6h  0.74% Wissensmagazin
    7108.2h  0.74% Realityshow
    6636.0h  0.69% Wirtschaftsmagazin
    6430.5h  0.67% Telenovela
    6240.9h  0.65% Dramaserie
