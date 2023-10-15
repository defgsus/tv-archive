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

**97** channels, **489,659.6** hours playtime between **2023-01-17** and **2023-10-16**


### playtime per genre (top 30)

    32231.5h 6.58% Nachrichten
    23359.2h 4.77% Verkaufsshow
    19696.2h 4.02% Krimiserie
    16557.7h 3.38% Werbesendung
    16120.9h 3.29% Dokureihe
    14967.7h 3.06% Dokusoap
    14083.4h 2.88% Regionalmagazin
    12382.8h 2.53% Dokumentation
    11758.8h 2.40% *unknown*
    9174.9h  1.87% Zeichentrickserie
    8918.5h  1.82% Infomercial
    8720.5h  1.78% Animationsserie
    7807.7h  1.59% Comedyserie
    6902.5h  1.41% Morgenmagazin
    6585.9h  1.34% Religionsmagazin
    6523.5h  1.33% Talkshow
    6118.8h  1.25% Magazin
    5084.3h  1.04% Programmende
    4819.6h  0.98% E-Sport
    4649.2h  0.95% Sitcom
    4556.1h  0.93% Wetterbericht
    4407.2h  0.90% Börsenmagazin
    4101.9h  0.84% Quiz
    3812.5h  0.78% Komödie
    3722.4h  0.76% Musikmagazin
    3687.9h  0.75% Wissensmagazin
    3687.5h  0.75% Wirtschaftsmagazin
    3482.1h  0.71% Telenovela
    3321.6h  0.68% Politikmagazin
    3179.8h  0.65% Reportagereihe
