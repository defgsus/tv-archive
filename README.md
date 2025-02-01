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

**110** channels, **1,255,050.8** hours playtime between **2023-01-17** and **2025-02-02**


### playtime per genre (top 30)

    82250.7h 6.55% Nachrichten
    56471.8h 4.50% Verkaufsshow
    52064.6h 4.15% Krimiserie
    46773.8h 3.73% Werbesendung
    38980.8h 3.11% Dokureihe
    36830.8h 2.93% Dokusoap
    36505.0h 2.91% Regionalmagazin
    33562.0h 2.67% Dokumentation
    29918.7h 2.38% *unknown*
    23667.0h 1.89% Zeichentrickserie
    23303.1h 1.86% Infomercial
    22455.5h 1.79% Animationsserie
    17551.3h 1.40% Comedyserie
    17527.7h 1.40% Morgenmagazin
    16544.9h 1.32% Talkshow
    16286.5h 1.30% Religionsmagazin
    15092.3h 1.20% Magazin
    12437.4h 0.99% E-Sport
    12020.0h 0.96% Sitcom
    11491.1h 0.92% Komödie
    11376.7h 0.91% Wetterbericht
    11172.8h 0.89% Quiz
    10997.5h 0.88% Programmende
    9758.8h  0.78% Realityshow
    9585.9h  0.76% Politikmagazin
    9237.3h  0.74% Wissensmagazin
    8879.2h  0.71% Börsenmagazin
    8339.3h  0.66% Dramaserie
    8331.8h  0.66% Arztserie
    8286.3h  0.66% Wirtschaftsmagazin
