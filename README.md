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

**109** channels, **1,090,714.3** hours playtime between **2023-01-17** and **2024-10-15**


### playtime per genre (top 30)

    70986.2h 6.51% Nachrichten
    50341.5h 4.62% Verkaufsshow
    45190.8h 4.14% Krimiserie
    39833.1h 3.65% Werbesendung
    34164.5h 3.13% Dokureihe
    32680.2h 3.00% Dokusoap
    31858.8h 2.92% Regionalmagazin
    28572.2h 2.62% Dokumentation
    26011.3h 2.38% *unknown*
    20321.5h 1.86% Zeichentrickserie
    20054.8h 1.84% Infomercial
    19519.2h 1.79% Animationsserie
    15814.5h 1.45% Comedyserie
    15251.6h 1.40% Morgenmagazin
    14760.1h 1.35% Religionsmagazin
    14396.8h 1.32% Talkshow
    13949.7h 1.28% Magazin
    10790.9h 0.99% E-Sport
    10487.4h 0.96% Sitcom
    9876.1h  0.91% Wetterbericht
    9706.4h  0.89% Programmende
    9568.4h  0.88% Komödie
    9554.6h  0.88% Quiz
    8386.2h  0.77% Börsenmagazin
    8246.6h  0.76% Realityshow
    8209.4h  0.75% Politikmagazin
    8196.5h  0.75% Wissensmagazin
    7351.1h  0.67% Wirtschaftsmagazin
    7178.3h  0.66% Telenovela
    7122.4h  0.65% Dramaserie
