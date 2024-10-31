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

**109** channels, **1,117,928.2** hours playtime between **2023-01-17** and **2024-11-01**


### playtime per genre (top 30)

    72833.4h 6.52% Nachrichten
    51424.7h 4.60% Verkaufsshow
    46512.6h 4.16% Krimiserie
    40997.3h 3.67% Werbesendung
    34946.4h 3.13% Dokureihe
    33424.8h 2.99% Dokusoap
    32724.7h 2.93% Regionalmagazin
    29334.0h 2.62% Dokumentation
    26452.2h 2.37% *unknown*
    20887.8h 1.87% Zeichentrickserie
    20581.7h 1.84% Infomercial
    19979.5h 1.79% Animationsserie
    16122.3h 1.44% Comedyserie
    15661.9h 1.40% Morgenmagazin
    15009.6h 1.34% Religionsmagazin
    14792.1h 1.32% Talkshow
    14107.3h 1.26% Magazin
    11046.6h 0.99% E-Sport
    10784.8h 0.96% Sitcom
    10121.8h 0.91% Wetterbericht
    9914.2h  0.89% Programmende
    9841.3h  0.88% Quiz
    9792.8h  0.88% Komödie
    8534.5h  0.76% Realityshow
    8481.0h  0.76% Börsenmagazin
    8469.6h  0.76% Politikmagazin
    8405.7h  0.75% Wissensmagazin
    7520.3h  0.67% Wirtschaftsmagazin
    7382.6h  0.66% Telenovela
    7328.0h  0.66% Dramaserie
