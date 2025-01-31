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

**110** channels, **1,253,351.8** hours playtime between **2023-01-17** and **2025-02-01**


### playtime per genre (top 30)

    82153.4h 6.55% Nachrichten
    56431.8h 4.50% Verkaufsshow
    52011.1h 4.15% Krimiserie
    46698.3h 3.73% Werbesendung
    38915.3h 3.10% Dokureihe
    36771.7h 2.93% Dokusoap
    36483.0h 2.91% Regionalmagazin
    33493.9h 2.67% Dokumentation
    29880.6h 2.38% *unknown*
    23627.1h 1.89% Zeichentrickserie
    23254.3h 1.86% Infomercial
    22417.8h 1.79% Animationsserie
    17527.8h 1.40% Comedyserie
    17519.7h 1.40% Morgenmagazin
    16520.2h 1.32% Talkshow
    16269.5h 1.30% Religionsmagazin
    15088.3h 1.20% Magazin
    12425.6h 0.99% E-Sport
    12008.9h 0.96% Sitcom
    11467.7h 0.91% Komödie
    11362.0h 0.91% Wetterbericht
    11167.8h 0.89% Quiz
    10983.9h 0.88% Programmende
    9749.8h  0.78% Realityshow
    9585.2h  0.76% Politikmagazin
    9229.7h  0.74% Wissensmagazin
    8879.0h  0.71% Börsenmagazin
    8331.2h  0.66% Dramaserie
    8317.5h  0.66% Arztserie
    8285.2h  0.66% Wirtschaftsmagazin
