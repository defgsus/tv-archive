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

**110** channels, **1,222,149.9** hours playtime between **2023-01-17** and **2025-01-11**


### playtime per genre (top 30)

    79930.3h 6.54% Nachrichten
    55271.0h 4.52% Verkaufsshow
    50681.1h 4.15% Krimiserie
    45336.6h 3.71% Werbesendung
    38043.0h 3.11% Dokureihe
    35929.7h 2.94% Dokusoap
    35589.6h 2.91% Regionalmagazin
    32557.8h 2.66% Dokumentation
    29086.5h 2.38% *unknown*
    22988.5h 1.88% Zeichentrickserie
    22623.9h 1.85% Infomercial
    21837.8h 1.79% Animationsserie
    17194.6h 1.41% Comedyserie
    17065.3h 1.40% Morgenmagazin
    16102.3h 1.32% Talkshow
    15980.7h 1.31% Religionsmagazin
    14907.2h 1.22% Magazin
    12101.6h 0.99% E-Sport
    11706.5h 0.96% Sitcom
    11208.4h 0.92% Komödie
    11067.3h 0.91% Wetterbericht
    10835.8h 0.89% Quiz
    10735.5h 0.88% Programmende
    9464.3h  0.77% Realityshow
    9305.6h  0.76% Politikmagazin
    9071.0h  0.74% Wissensmagazin
    8780.4h  0.72% Börsenmagazin
    8094.2h  0.66% Wirtschaftsmagazin
    8087.7h  0.66% Dramaserie
    8085.5h  0.66% Arztserie
