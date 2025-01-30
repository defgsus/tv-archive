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

**110** channels, **1,253,305.2** hours playtime between **2023-01-17** and **2025-01-31**


### playtime per genre (top 30)

    82156.6h 6.56% Nachrichten
    56411.8h 4.50% Verkaufsshow
    52021.2h 4.15% Krimiserie
    46688.7h 3.73% Werbesendung
    38903.2h 3.10% Dokureihe
    36778.2h 2.93% Dokusoap
    36478.3h 2.91% Regionalmagazin
    33507.5h 2.67% Dokumentation
    29877.3h 2.38% *unknown*
    23625.6h 1.89% Zeichentrickserie
    23258.7h 1.86% Infomercial
    22416.9h 1.79% Animationsserie
    17524.4h 1.40% Comedyserie
    17514.2h 1.40% Morgenmagazin
    16514.9h 1.32% Talkshow
    16268.9h 1.30% Religionsmagazin
    15090.4h 1.20% Magazin
    12426.5h 0.99% E-Sport
    12009.3h 0.96% Sitcom
    11469.2h 0.92% Komödie
    11363.1h 0.91% Wetterbericht
    11170.4h 0.89% Quiz
    10983.6h 0.88% Programmende
    9749.6h  0.78% Realityshow
    9602.5h  0.77% Politikmagazin
    9229.6h  0.74% Wissensmagazin
    8878.7h  0.71% Börsenmagazin
    8335.7h  0.67% Dramaserie
    8321.9h  0.66% Arztserie
    8286.4h  0.66% Wirtschaftsmagazin
