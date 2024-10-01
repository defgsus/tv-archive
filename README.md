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

**109** channels, **1,070,783.2** hours playtime between **2023-01-17** and **2024-10-02**


### playtime per genre (top 30)

    69647.4h 6.50% Nachrichten
    49546.0h 4.63% Verkaufsshow
    44281.3h 4.14% Krimiserie
    38975.3h 3.64% Werbesendung
    33552.2h 3.13% Dokureihe
    32127.2h 3.00% Dokusoap
    31272.5h 2.92% Regionalmagazin
    28022.6h 2.62% Dokumentation
    25640.0h 2.39% *unknown*
    19899.5h 1.86% Zeichentrickserie
    19666.5h 1.84% Infomercial
    19179.8h 1.79% Animationsserie
    15585.7h 1.46% Comedyserie
    14980.2h 1.40% Morgenmagazin
    14572.0h 1.36% Religionsmagazin
    14122.3h 1.32% Talkshow
    13820.0h 1.29% Magazin
    10589.1h 0.99% E-Sport
    10286.8h 0.96% Sitcom
    9697.2h  0.91% Wetterbericht
    9553.9h  0.89% Programmende
    9364.2h  0.87% Komödie
    9334.7h  0.87% Quiz
    8326.0h  0.78% Börsenmagazin
    8053.8h  0.75% Politikmagazin
    8042.5h  0.75% Wissensmagazin
    8039.3h  0.75% Realityshow
    7239.8h  0.68% Wirtschaftsmagazin
    7049.3h  0.66% Telenovela
    6974.6h  0.65% Dramaserie
