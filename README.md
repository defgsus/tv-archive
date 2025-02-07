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

**110** channels, **1,263,718.1** hours playtime between **2023-01-17** and **2025-02-08**


### playtime per genre (top 30)

    82892.4h 6.56% Nachrichten
    56760.2h 4.49% Verkaufsshow
    52477.1h 4.15% Krimiserie
    47151.6h 3.73% Werbesendung
    39219.6h 3.10% Dokureihe
    37065.1h 2.93% Dokusoap
    36781.1h 2.91% Regionalmagazin
    33838.6h 2.68% Dokumentation
    30061.6h 2.38% *unknown*
    23850.3h 1.89% Zeichentrickserie
    23513.5h 1.86% Infomercial
    22611.9h 1.79% Animationsserie
    17675.0h 1.40% Morgenmagazin
    17636.6h 1.40% Comedyserie
    16668.2h 1.32% Talkshow
    16367.7h 1.30% Religionsmagazin
    15122.7h 1.20% Magazin
    12525.2h 0.99% E-Sport
    12111.1h 0.96% Sitcom
    11528.5h 0.91% Komödie
    11462.5h 0.91% Wetterbericht
    11267.9h 0.89% Quiz
    11066.6h 0.88% Programmende
    9844.2h  0.78% Realityshow
    9669.5h  0.77% Politikmagazin
    9285.1h  0.73% Wissensmagazin
    8913.5h  0.71% Börsenmagazin
    8401.2h  0.66% Arztserie
    8399.2h  0.66% Dramaserie
    8357.4h  0.66% Wirtschaftsmagazin
