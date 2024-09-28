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

**109** channels, **1,065,413.1** hours playtime between **2023-01-17** and **2024-09-29**


### playtime per genre (top 30)

    69292.4h 6.50% Nachrichten
    49338.8h 4.63% Verkaufsshow
    44015.2h 4.13% Krimiserie
    38748.4h 3.64% Werbesendung
    33410.6h 3.14% Dokureihe
    31998.3h 3.00% Dokusoap
    31101.2h 2.92% Regionalmagazin
    27887.9h 2.62% Dokumentation
    25550.6h 2.40% *unknown*
    19792.6h 1.86% Zeichentrickserie
    19563.1h 1.84% Infomercial
    19086.7h 1.79% Animationsserie
    15528.9h 1.46% Comedyserie
    14908.9h 1.40% Morgenmagazin
    14505.5h 1.36% Religionsmagazin
    14045.3h 1.32% Talkshow
    13778.6h 1.29% Magazin
    10536.2h 0.99% E-Sport
    10226.5h 0.96% Sitcom
    9647.2h  0.91% Wetterbericht
    9513.0h  0.89% Programmende
    9320.1h  0.87% Komödie
    9275.7h  0.87% Quiz
    8308.9h  0.78% Börsenmagazin
    7997.9h  0.75% Politikmagazin
    7997.1h  0.75% Wissensmagazin
    7990.4h  0.75% Realityshow
    7208.9h  0.68% Wirtschaftsmagazin
    7011.0h  0.66% Telenovela
    6936.7h  0.65% Dramaserie
