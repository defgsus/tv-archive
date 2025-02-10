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

**110** channels, **1,268,909.1** hours playtime between **2023-01-17** and **2025-02-11**


### playtime per genre (top 30)

    83224.1h 6.56% Nachrichten
    56915.9h 4.49% Verkaufsshow
    52695.8h 4.15% Krimiserie
    47383.5h 3.73% Werbesendung
    39391.0h 3.10% Dokureihe
    37221.0h 2.93% Dokusoap
    36898.9h 2.91% Regionalmagazin
    34008.2h 2.68% Dokumentation
    30193.0h 2.38% *unknown*
    23946.8h 1.89% Zeichentrickserie
    23647.0h 1.86% Infomercial
    22707.3h 1.79% Animationsserie
    17727.8h 1.40% Morgenmagazin
    17682.0h 1.39% Comedyserie
    16742.2h 1.32% Talkshow
    16425.3h 1.29% Religionsmagazin
    15141.1h 1.19% Magazin
    12578.1h 0.99% E-Sport
    12150.1h 0.96% Sitcom
    11591.0h 0.91% Komödie
    11511.0h 0.91% Wetterbericht
    11323.0h 0.89% Quiz
    11107.9h 0.88% Programmende
    9891.3h  0.78% Realityshow
    9702.4h  0.76% Politikmagazin
    9314.3h  0.73% Wissensmagazin
    8921.9h  0.70% Börsenmagazin
    8440.5h  0.67% Dramaserie
    8431.5h  0.66% Arztserie
    8383.4h  0.66% Wirtschaftsmagazin
