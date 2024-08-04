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

**109** channels, **981,381.4** hours playtime between **2023-01-17** and **2024-08-05**


### playtime per genre (top 30)

    63824.5h 6.50% Nachrichten
    45784.8h 4.67% Verkaufsshow
    40216.0h 4.10% Krimiserie
    35207.7h 3.59% Werbesendung
    30870.1h 3.15% Dokureihe
    29689.0h 3.03% Dokusoap
    28534.5h 2.91% Regionalmagazin
    25551.0h 2.60% Dokumentation
    24209.1h 2.47% *unknown*
    18185.4h 1.85% Zeichentrickserie
    17957.7h 1.83% Infomercial
    17551.7h 1.79% Animationsserie
    14503.0h 1.48% Comedyserie
    13766.4h 1.40% Morgenmagazin
    13450.8h 1.37% Magazin
    13340.0h 1.36% Religionsmagazin
    12932.5h 1.32% Talkshow
    9715.6h  0.99% E-Sport
    9297.5h  0.95% Sitcom
    8869.5h  0.90% Programmende
    8824.0h  0.90% Wetterbericht
    8606.0h  0.88% Komödie
    8437.1h  0.86% Quiz
    8038.2h  0.82% Börsenmagazin
    7357.1h  0.75% Politikmagazin
    7306.8h  0.74% Wissensmagazin
    7264.6h  0.74% Realityshow
    6748.0h  0.69% Wirtschaftsmagazin
    6495.1h  0.66% Telenovela
    6382.3h  0.65% Dramaserie
