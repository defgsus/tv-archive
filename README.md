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

**110** channels, **1,232,609.6** hours playtime between **2023-01-17** and **2025-01-18**


### playtime per genre (top 30)

    80678.5h 6.55% Nachrichten
    55715.9h 4.52% Verkaufsshow
    51114.1h 4.15% Krimiserie
    45800.4h 3.72% Werbesendung
    38326.3h 3.11% Dokureihe
    36212.8h 2.94% Dokusoap
    35892.8h 2.91% Regionalmagazin
    32873.7h 2.67% Dokumentation
    29332.8h 2.38% *unknown*
    23206.3h 1.88% Zeichentrickserie
    22825.0h 1.85% Infomercial
    22030.0h 1.79% Animationsserie
    17298.8h 1.40% Comedyserie
    17219.9h 1.40% Morgenmagazin
    16249.4h 1.32% Talkshow
    16076.5h 1.30% Religionsmagazin
    14970.2h 1.21% Magazin
    12212.8h 0.99% E-Sport
    11811.1h 0.96% Sitcom
    11288.3h 0.92% Komödie
    11164.2h 0.91% Wetterbericht
    10947.0h 0.89% Quiz
    10810.8h 0.88% Programmende
    9550.9h  0.77% Realityshow
    9399.7h  0.76% Politikmagazin
    9121.8h  0.74% Wissensmagazin
    8813.6h  0.72% Börsenmagazin
    8178.8h  0.66% Dramaserie
    8162.4h  0.66% Arztserie
    8159.5h  0.66% Wirtschaftsmagazin
