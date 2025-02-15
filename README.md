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

**110** channels, **1,275,887.1** hours playtime between **2023-01-17** and **2025-02-16**


### playtime per genre (top 30)

    83734.8h 6.56% Nachrichten
    57198.1h 4.48% Verkaufsshow
    53017.8h 4.16% Krimiserie
    47671.1h 3.74% Werbesendung
    39572.5h 3.10% Dokureihe
    37422.9h 2.93% Dokusoap
    37108.6h 2.91% Regionalmagazin
    34218.6h 2.68% Dokumentation
    30328.0h 2.38% *unknown*
    24091.6h 1.89% Zeichentrickserie
    23820.9h 1.87% Infomercial
    22843.6h 1.79% Animationsserie
    17836.5h 1.40% Morgenmagazin
    17762.4h 1.39% Comedyserie
    16852.8h 1.32% Talkshow
    16482.6h 1.29% Religionsmagazin
    15172.0h 1.19% Magazin
    12648.2h 0.99% E-Sport
    12214.6h 0.96% Sitcom
    11648.5h 0.91% Komödie
    11582.7h 0.91% Wetterbericht
    11376.4h 0.89% Quiz
    11163.5h 0.87% Programmende
    9937.7h  0.78% Realityshow
    9773.2h  0.77% Politikmagazin
    9345.9h  0.73% Wissensmagazin
    8946.0h  0.70% Börsenmagazin
    8497.4h  0.67% Arztserie
    8494.6h  0.67% Dramaserie
    8430.0h  0.66% Wirtschaftsmagazin
