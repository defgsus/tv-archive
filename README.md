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

**110** channels, **1,262,008.5** hours playtime between **2023-01-17** and **2025-02-06**


### playtime per genre (top 30)

    82763.4h 6.56% Nachrichten
    56712.2h 4.49% Verkaufsshow
    52388.6h 4.15% Krimiserie
    47086.8h 3.73% Werbesendung
    39170.3h 3.10% Dokureihe
    37031.3h 2.93% Dokusoap
    36723.1h 2.91% Regionalmagazin
    33782.9h 2.68% Dokumentation
    30038.0h 2.38% *unknown*
    23810.4h 1.89% Zeichentrickserie
    23469.6h 1.86% Infomercial
    22583.3h 1.79% Animationsserie
    17641.0h 1.40% Morgenmagazin
    17619.2h 1.40% Comedyserie
    16638.3h 1.32% Talkshow
    16353.9h 1.30% Religionsmagazin
    15118.0h 1.20% Magazin
    12515.6h 0.99% E-Sport
    12093.7h 0.96% Sitcom
    11526.0h 0.91% Komödie
    11444.8h 0.91% Wetterbericht
    11251.3h 0.89% Quiz
    11052.8h 0.88% Programmende
    9827.0h  0.78% Realityshow
    9657.0h  0.77% Politikmagazin
    9276.0h  0.74% Wissensmagazin
    8904.7h  0.71% Börsenmagazin
    8388.1h  0.66% Arztserie
    8387.8h  0.66% Dramaserie
    8341.9h  0.66% Wirtschaftsmagazin
