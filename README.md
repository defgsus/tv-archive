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

**109** channels, **1,059,891.4** hours playtime between **2023-01-17** and **2024-09-24**


### playtime per genre (top 30)

    68938.8h 6.50% Nachrichten
    49125.6h 4.63% Verkaufsshow
    43754.1h 4.13% Krimiserie
    38505.9h 3.63% Werbesendung
    33255.8h 3.14% Dokureihe
    31878.1h 3.01% Dokusoap
    30944.3h 2.92% Regionalmagazin
    27744.7h 2.62% Dokumentation
    25454.9h 2.40% *unknown*
    19672.1h 1.86% Zeichentrickserie
    19456.7h 1.84% Infomercial
    18990.3h 1.79% Animationsserie
    15468.3h 1.46% Comedyserie
    14832.0h 1.40% Morgenmagazin
    14429.2h 1.36% Religionsmagazin
    13965.4h 1.32% Talkshow
    13751.7h 1.30% Magazin
    10495.5h 0.99% E-Sport
    10163.5h 0.96% Sitcom
    9596.5h  0.91% Wetterbericht
    9470.9h  0.89% Programmende
    9290.3h  0.88% Komödie
    9220.4h  0.87% Quiz
    8291.5h  0.78% Börsenmagazin
    7954.4h  0.75% Wissensmagazin
    7953.8h  0.75% Politikmagazin
    7934.1h  0.75% Realityshow
    7180.1h  0.68% Wirtschaftsmagazin
    6972.6h  0.66% Telenovela
    6899.8h  0.65% Dramaserie
