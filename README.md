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

**110** channels, **1,225,610.8** hours playtime between **2023-01-17** and **2025-01-13**


### playtime per genre (top 30)

    80131.6h 6.54% Nachrichten
    55404.6h 4.52% Verkaufsshow
    50794.8h 4.14% Krimiserie
    45499.3h 3.71% Werbesendung
    38157.9h 3.11% Dokureihe
    36020.4h 2.94% Dokusoap
    35642.3h 2.91% Regionalmagazin
    32666.4h 2.67% Dokumentation
    29197.9h 2.38% *unknown*
    23065.2h 1.88% Zeichentrickserie
    22696.3h 1.85% Infomercial
    21901.4h 1.79% Animationsserie
    17222.4h 1.41% Comedyserie
    17082.2h 1.39% Morgenmagazin
    16164.0h 1.32% Talkshow
    16028.3h 1.31% Religionsmagazin
    14934.3h 1.22% Magazin
    12131.0h 0.99% E-Sport
    11730.1h 0.96% Sitcom
    11254.1h 0.92% Komödie
    11095.8h 0.91% Wetterbericht
    10847.9h 0.89% Quiz
    10755.9h 0.88% Programmende
    9485.3h  0.77% Realityshow
    9321.7h  0.76% Politikmagazin
    9092.5h  0.74% Wissensmagazin
    8780.3h  0.72% Börsenmagazin
    8103.7h  0.66% Dramaserie
    8102.4h  0.66% Wirtschaftsmagazin
    8100.6h  0.66% Arztserie
