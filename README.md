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

**110** channels, **1,249,922.1** hours playtime between **2023-01-17** and **2025-01-29**


### playtime per genre (top 30)

    81888.2h 6.55% Nachrichten
    56344.3h 4.51% Verkaufsshow
    51851.4h 4.15% Krimiserie
    46545.4h 3.72% Werbesendung
    38830.3h 3.11% Dokureihe
    36688.0h 2.94% Dokusoap
    36364.3h 2.91% Regionalmagazin
    33418.2h 2.67% Dokumentation
    29814.1h 2.39% *unknown*
    23558.8h 1.88% Zeichentrickserie
    23159.5h 1.85% Infomercial
    22352.5h 1.79% Animationsserie
    17490.0h 1.40% Comedyserie
    17457.8h 1.40% Morgenmagazin
    16474.7h 1.32% Talkshow
    16246.8h 1.30% Religionsmagazin
    15067.0h 1.21% Magazin
    12403.5h 0.99% E-Sport
    11967.9h 0.96% Sitcom
    11447.8h 0.92% Komödie
    11326.0h 0.91% Wetterbericht
    11124.1h 0.89% Quiz
    10956.6h 0.88% Programmende
    9712.6h  0.78% Realityshow
    9550.8h  0.76% Politikmagazin
    9211.1h  0.74% Wissensmagazin
    8862.2h  0.71% Börsenmagazin
    8301.4h  0.66% Dramaserie
    8288.2h  0.66% Arztserie
    8256.1h  0.66% Wirtschaftsmagazin
