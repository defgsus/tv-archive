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

**110** channels, **1,216,939.3** hours playtime between **2023-01-17** and **2025-01-07**


### playtime per genre (top 30)

    79520.5h 6.53% Nachrichten
    55091.4h 4.53% Verkaufsshow
    50432.2h 4.14% Krimiserie
    45120.0h 3.71% Werbesendung
    37917.7h 3.12% Dokureihe
    35779.7h 2.94% Dokusoap
    35407.2h 2.91% Regionalmagazin
    32414.1h 2.66% Dokumentation
    28953.8h 2.38% *unknown*
    22880.6h 1.88% Zeichentrickserie
    22525.5h 1.85% Infomercial
    21739.9h 1.79% Animationsserie
    17134.1h 1.41% Comedyserie
    16963.5h 1.39% Morgenmagazin
    16032.5h 1.32% Talkshow
    15940.6h 1.31% Religionsmagazin
    14869.2h 1.22% Magazin
    12032.7h 0.99% E-Sport
    11647.4h 0.96% Sitcom
    11162.5h 0.92% Komödie
    11014.4h 0.91% Wetterbericht
    10767.0h 0.88% Quiz
    10693.2h 0.88% Programmende
    9409.2h  0.77% Realityshow
    9254.5h  0.76% Politikmagazin
    9040.1h  0.74% Wissensmagazin
    8753.6h  0.72% Börsenmagazin
    8050.0h  0.66% Wirtschaftsmagazin
    8039.5h  0.66% Dramaserie
    8039.0h  0.66% Arztserie
