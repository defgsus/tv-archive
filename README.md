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

**110** channels, **1,267,196.2** hours playtime between **2023-01-17** and **2025-02-10**


### playtime per genre (top 30)

    83085.6h 6.56% Nachrichten
    56875.4h 4.49% Verkaufsshow
    52601.1h 4.15% Krimiserie
    47312.3h 3.73% Werbesendung
    39330.8h 3.10% Dokureihe
    37173.2h 2.93% Dokusoap
    36837.3h 2.91% Regionalmagazin
    33952.2h 2.68% Dokumentation
    30165.0h 2.38% *unknown*
    23910.5h 1.89% Zeichentrickserie
    23605.0h 1.86% Infomercial
    22674.4h 1.79% Animationsserie
    17691.9h 1.40% Morgenmagazin
    17662.2h 1.39% Comedyserie
    16725.3h 1.32% Talkshow
    16416.1h 1.30% Religionsmagazin
    15135.0h 1.19% Magazin
    12558.0h 0.99% E-Sport
    12128.4h 0.96% Sitcom
    11589.2h 0.91% Komödie
    11492.4h 0.91% Wetterbericht
    11287.2h 0.89% Quiz
    11094.2h 0.88% Programmende
    9870.6h  0.78% Realityshow
    9679.9h  0.76% Politikmagazin
    9310.1h  0.73% Wissensmagazin
    8913.4h  0.70% Börsenmagazin
    8429.7h  0.67% Dramaserie
    8415.2h  0.66% Arztserie
    8369.0h  0.66% Wirtschaftsmagazin
