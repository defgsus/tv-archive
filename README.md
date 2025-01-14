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

**110** channels, **1,229,119.3** hours playtime between **2023-01-17** and **2025-01-15**


### playtime per genre (top 30)

    80408.9h 6.54% Nachrichten
    55561.1h 4.52% Verkaufsshow
    50961.0h 4.15% Krimiserie
    45655.7h 3.71% Werbesendung
    38258.8h 3.11% Dokureihe
    36111.4h 2.94% Dokusoap
    35767.6h 2.91% Regionalmagazin
    32768.1h 2.67% Dokumentation
    29265.7h 2.38% *unknown*
    23137.9h 1.88% Zeichentrickserie
    22760.9h 1.85% Infomercial
    21963.2h 1.79% Animationsserie
    17265.3h 1.40% Comedyserie
    17152.0h 1.40% Morgenmagazin
    16201.6h 1.32% Talkshow
    16053.3h 1.31% Religionsmagazin
    14950.9h 1.22% Magazin
    12175.5h 0.99% E-Sport
    11769.6h 0.96% Sitcom
    11270.3h 0.92% Komödie
    11129.2h 0.91% Wetterbericht
    10902.2h 0.89% Quiz
    10782.7h 0.88% Programmende
    9519.8h  0.77% Realityshow
    9364.9h  0.76% Politikmagazin
    9103.9h  0.74% Wissensmagazin
    8796.6h  0.72% Börsenmagazin
    8137.2h  0.66% Dramaserie
    8132.6h  0.66% Arztserie
    8130.5h  0.66% Wirtschaftsmagazin
