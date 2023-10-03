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

**97** channels, **468,098.4** hours playtime between **2023-01-17** and **2023-10-04**


### playtime per genre (top 30)

    30844.2h 6.59% Nachrichten
    22280.6h 4.76% Verkaufsshow
    18868.9h 4.03% Krimiserie
    15806.6h 3.38% Werbesendung
    15455.2h 3.30% Dokureihe
    14284.1h 3.05% Dokusoap
    13446.9h 2.87% Regionalmagazin
    11824.0h 2.53% Dokumentation
    11153.9h 2.38% *unknown*
    8792.5h  1.88% Zeichentrickserie
    8527.1h  1.82% Infomercial
    8313.6h  1.78% Animationsserie
    7526.2h  1.61% Comedyserie
    6601.1h  1.41% Morgenmagazin
    6286.7h  1.34% Religionsmagazin
    6196.9h  1.32% Talkshow
    5812.8h  1.24% Magazin
    4923.3h  1.05% Programmende
    4621.8h  0.99% E-Sport
    4424.1h  0.95% Sitcom
    4377.5h  0.94% Wetterbericht
    4224.6h  0.90% Börsenmagazin
    3916.4h  0.84% Quiz
    3637.6h  0.78% Komödie
    3599.8h  0.77% Musikmagazin
    3528.7h  0.75% Wirtschaftsmagazin
    3515.8h  0.75% Wissensmagazin
    3318.9h  0.71% Telenovela
    3141.2h  0.67% Politikmagazin
    3046.2h  0.65% Reportagereihe
