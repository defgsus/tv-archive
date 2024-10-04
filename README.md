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

**109** channels, **1,074,479.8** hours playtime between **2023-01-17** and **2024-10-05**


### playtime per genre (top 30)

    69932.8h 6.51% Nachrichten
    49702.8h 4.63% Verkaufsshow
    44456.8h 4.14% Krimiserie
    39129.9h 3.64% Werbesendung
    33625.0h 3.13% Dokureihe
    32236.6h 3.00% Dokusoap
    31400.8h 2.92% Regionalmagazin
    28089.0h 2.61% Dokumentation
    25726.0h 2.39% *unknown*
    19969.7h 1.86% Zeichentrickserie
    19739.0h 1.84% Infomercial
    19243.0h 1.79% Animationsserie
    15630.8h 1.45% Comedyserie
    15051.0h 1.40% Morgenmagazin
    14601.9h 1.36% Religionsmagazin
    14184.0h 1.32% Talkshow
    13834.5h 1.29% Magazin
    10626.6h 0.99% E-Sport
    10330.4h 0.96% Sitcom
    9732.9h  0.91% Wetterbericht
    9581.7h  0.89% Programmende
    9414.3h  0.88% Komödie
    9378.5h  0.87% Quiz
    8342.9h  0.78% Börsenmagazin
    8084.4h  0.75% Politikmagazin
    8079.8h  0.75% Realityshow
    8068.5h  0.75% Wissensmagazin
    7269.1h  0.68% Wirtschaftsmagazin
    7084.6h  0.66% Telenovela
    7018.0h  0.65% Dramaserie
