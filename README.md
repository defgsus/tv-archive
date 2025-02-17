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

**110** channels, **1,279,334.2** hours playtime between **2023-01-17** and **2025-02-18**


### playtime per genre (top 30)

    83969.2h 6.56% Nachrichten
    57302.3h 4.48% Verkaufsshow
    53162.8h 4.16% Krimiserie
    47817.2h 3.74% Werbesendung
    39709.8h 3.10% Dokureihe
    37526.4h 2.93% Dokusoap
    37204.0h 2.91% Regionalmagazin
    34337.5h 2.68% Dokumentation
    30394.9h 2.38% *unknown*
    24160.2h 1.89% Zeichentrickserie
    23907.3h 1.87% Infomercial
    22913.2h 1.79% Animationsserie
    17881.3h 1.40% Morgenmagazin
    17793.7h 1.39% Comedyserie
    16908.5h 1.32% Talkshow
    16523.3h 1.29% Religionsmagazin
    15189.0h 1.19% Magazin
    12684.6h 0.99% E-Sport
    12246.0h 0.96% Sitcom
    11665.3h 0.91% Komödie
    11616.7h 0.91% Wetterbericht
    11424.0h 0.89% Quiz
    11191.2h 0.87% Programmende
    9970.6h  0.78% Realityshow
    9802.9h  0.77% Politikmagazin
    9364.6h  0.73% Wissensmagazin
    8951.5h  0.70% Börsenmagazin
    8524.9h  0.67% Arztserie
    8511.6h  0.67% Dramaserie
    8447.8h  0.66% Wirtschaftsmagazin
