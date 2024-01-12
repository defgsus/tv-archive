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

**98** channels, **647,077.4** hours playtime between **2023-01-17** and **2024-01-13**


### playtime per genre (top 30)

    42249.0h 6.53% Nachrichten
    30912.2h 4.78% Verkaufsshow
    25966.4h 4.01% Krimiserie
    22034.7h 3.41% Werbesendung
    21021.5h 3.25% Dokureihe
    19340.0h 2.99% Dokusoap
    18627.2h 2.88% Regionalmagazin
    16800.0h 2.60% Dokumentation
    16105.6h 2.49% *unknown*
    11950.9h 1.85% Zeichentrickserie
    11737.2h 1.81% Infomercial
    11371.7h 1.76% Animationsserie
    9813.6h  1.52% Comedyserie
    9170.5h  1.42% Morgenmagazin
    8744.4h  1.35% Religionsmagazin
    8536.0h  1.32% Talkshow
    8535.1h  1.32% Magazin
    6359.1h  0.98% E-Sport
    6295.0h  0.97% Programmende
    6258.1h  0.97% Sitcom
    5868.1h  0.91% Wetterbericht
    5766.9h  0.89% Börsenmagazin
    5489.3h  0.85% Komödie
    5345.6h  0.83% Quiz
    4873.2h  0.75% Wissensmagazin
    4754.3h  0.73% Wirtschaftsmagazin
    4709.9h  0.73% Realityshow
    4618.1h  0.71% Telenovela
    4607.6h  0.71% Musikmagazin
    4559.4h  0.70% Politikmagazin
