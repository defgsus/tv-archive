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

**110** channels, **1,230,817.2** hours playtime between **2023-01-17** and **2025-01-16**


### playtime per genre (top 30)

    80545.0h 6.54% Nachrichten
    55606.8h 4.52% Verkaufsshow
    51031.1h 4.15% Krimiserie
    45733.2h 3.72% Werbesendung
    38289.8h 3.11% Dokureihe
    36170.2h 2.94% Dokusoap
    35831.6h 2.91% Regionalmagazin
    32813.9h 2.67% Dokumentation
    29298.5h 2.38% *unknown*
    23172.6h 1.88% Zeichentrickserie
    22791.9h 1.85% Infomercial
    21995.4h 1.79% Animationsserie
    17281.3h 1.40% Comedyserie
    17180.5h 1.40% Morgenmagazin
    16217.8h 1.32% Talkshow
    16065.1h 1.31% Religionsmagazin
    14964.0h 1.22% Magazin
    12193.8h 0.99% E-Sport
    11794.7h 0.96% Sitcom
    11271.9h 0.92% Komödie
    11148.1h 0.91% Wetterbericht
    10924.5h 0.89% Quiz
    10797.1h 0.88% Programmende
    9535.5h  0.77% Realityshow
    9387.7h  0.76% Politikmagazin
    9114.4h  0.74% Wissensmagazin
    8805.8h  0.72% Börsenmagazin
    8152.5h  0.66% Arztserie
    8151.7h  0.66% Dramaserie
    8144.4h  0.66% Wirtschaftsmagazin
