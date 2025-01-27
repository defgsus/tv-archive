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

**110** channels, **1,248,156.7** hours playtime between **2023-01-17** and **2025-01-28**


### playtime per genre (top 30)

    81752.8h 6.55% Nachrichten
    56277.8h 4.51% Verkaufsshow
    51763.2h 4.15% Krimiserie
    46469.9h 3.72% Werbesendung
    38783.0h 3.11% Dokureihe
    36640.5h 2.94% Dokusoap
    36292.6h 2.91% Regionalmagazin
    33363.0h 2.67% Dokumentation
    29790.3h 2.39% *unknown*
    23520.8h 1.88% Zeichentrickserie
    23127.8h 1.85% Infomercial
    22321.7h 1.79% Animationsserie
    17469.0h 1.40% Comedyserie
    17423.9h 1.40% Morgenmagazin
    16451.4h 1.32% Talkshow
    16231.9h 1.30% Religionsmagazin
    15052.0h 1.21% Magazin
    12369.8h 0.99% E-Sport
    11951.9h 0.96% Sitcom
    11425.1h 0.92% Komödie
    11308.6h 0.91% Wetterbericht
    11107.4h 0.89% Quiz
    10942.2h 0.88% Programmende
    9693.9h  0.78% Realityshow
    9530.8h  0.76% Politikmagazin
    9206.8h  0.74% Wissensmagazin
    8853.3h  0.71% Börsenmagazin
    8283.5h  0.66% Dramaserie
    8269.8h  0.66% Arztserie
    8244.3h  0.66% Wirtschaftsmagazin
