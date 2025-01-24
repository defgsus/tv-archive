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

**110** channels, **1,242,971.3** hours playtime between **2023-01-17** and **2025-01-25**


### playtime per genre (top 30)

    81414.9h 6.55% Nachrichten
    56093.6h 4.51% Verkaufsshow
    51555.8h 4.15% Krimiserie
    46239.2h 3.72% Werbesendung
    38623.4h 3.11% Dokureihe
    36498.2h 2.94% Dokusoap
    36189.6h 2.91% Regionalmagazin
    33190.1h 2.67% Dokumentation
    29625.5h 2.38% *unknown*
    23416.4h 1.88% Zeichentrickserie
    23024.3h 1.85% Infomercial
    22222.8h 1.79% Animationsserie
    17420.4h 1.40% Comedyserie
    17366.0h 1.40% Morgenmagazin
    16388.6h 1.32% Talkshow
    16173.0h 1.30% Religionsmagazin
    15024.6h 1.21% Magazin
    12326.4h 0.99% E-Sport
    11909.9h 0.96% Sitcom
    11364.1h 0.91% Komödie
    11261.5h 0.91% Wetterbericht
    11060.1h 0.89% Quiz
    10894.0h 0.88% Programmende
    9650.8h  0.78% Realityshow
    9494.3h  0.76% Politikmagazin
    9173.9h  0.74% Wissensmagazin
    8844.6h  0.71% Börsenmagazin
    8258.5h  0.66% Dramaserie
    8242.0h  0.66% Arztserie
    8219.0h  0.66% Wirtschaftsmagazin
