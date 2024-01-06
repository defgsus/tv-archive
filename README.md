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

**97** channels, **636,515.5** hours playtime between **2023-01-17** and **2024-01-07**


### playtime per genre (top 30)

    41525.9h 6.52% Nachrichten
    30433.4h 4.78% Verkaufsshow
    25484.3h 4.00% Krimiserie
    21630.7h 3.40% Werbesendung
    20678.7h 3.25% Dokureihe
    19016.6h 2.99% Dokusoap
    18264.4h 2.87% Regionalmagazin
    16555.2h 2.60% Dokumentation
    15807.4h 2.48% *unknown*
    11740.4h 1.84% Zeichentrickserie
    11539.4h 1.81% Infomercial
    11195.0h 1.76% Animationsserie
    9660.6h  1.52% Comedyserie
    8996.5h  1.41% Morgenmagazin
    8610.2h  1.35% Religionsmagazin
    8394.8h  1.32% Talkshow
    8341.0h  1.31% Magazin
    6267.9h  0.98% E-Sport
    6211.5h  0.98% Programmende
    6168.0h  0.97% Sitcom
    5790.3h  0.91% Wetterbericht
    5685.8h  0.89% Börsenmagazin
    5418.5h  0.85% Komödie
    5232.5h  0.82% Quiz
    4786.9h  0.75% Wissensmagazin
    4673.8h  0.73% Wirtschaftsmagazin
    4613.5h  0.72% Realityshow
    4556.8h  0.72% Musikmagazin
    4529.8h  0.71% Telenovela
    4469.8h  0.70% Politikmagazin
