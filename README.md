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

**109** channels, **1,048,847.1** hours playtime between **2023-01-17** and **2024-09-17**


### playtime per genre (top 30)

    68214.6h 6.50% Nachrichten
    48674.9h 4.64% Verkaufsshow
    43255.6h 4.12% Krimiserie
    38029.9h 3.63% Werbesendung
    32945.4h 3.14% Dokureihe
    31589.2h 3.01% Dokusoap
    30613.7h 2.92% Regionalmagazin
    27440.5h 2.62% Dokumentation
    25249.5h 2.41% *unknown*
    19460.1h 1.86% Zeichentrickserie
    19247.6h 1.84% Infomercial
    18785.8h 1.79% Animationsserie
    15325.6h 1.46% Comedyserie
    14678.2h 1.40% Morgenmagazin
    14271.9h 1.36% Religionsmagazin
    13795.0h 1.32% Talkshow
    13678.0h 1.30% Magazin
    10368.3h 0.99% E-Sport
    10042.6h 0.96% Sitcom
    9492.6h  0.91% Wetterbericht
    9387.3h  0.90% Programmende
    9221.2h  0.88% Komödie
    9098.6h  0.87% Quiz
    8256.2h  0.79% Börsenmagazin
    7863.9h  0.75% Wissensmagazin
    7853.7h  0.75% Politikmagazin
    7814.3h  0.75% Realityshow
    7120.5h  0.68% Wirtschaftsmagazin
    6897.7h  0.66% Telenovela
    6819.9h  0.65% Dramaserie
