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

**109** channels, **1,069,072.4** hours playtime between **2023-01-17** and **2024-10-01**


### playtime per genre (top 30)

    69523.3h 6.50% Nachrichten
    49498.4h 4.63% Verkaufsshow
    44163.9h 4.13% Krimiserie
    38904.2h 3.64% Werbesendung
    33498.1h 3.13% Dokureihe
    32099.3h 3.00% Dokusoap
    31205.1h 2.92% Regionalmagazin
    27962.8h 2.62% Dokumentation
    25618.6h 2.40% *unknown*
    19861.7h 1.86% Zeichentrickserie
    19633.0h 1.84% Infomercial
    19147.9h 1.79% Animationsserie
    15566.4h 1.46% Comedyserie
    14953.7h 1.40% Morgenmagazin
    14560.7h 1.36% Religionsmagazin
    14100.4h 1.32% Talkshow
    13817.2h 1.29% Magazin
    10571.7h 0.99% E-Sport
    10266.4h 0.96% Sitcom
    9678.0h  0.91% Wetterbericht
    9540.4h  0.89% Programmende
    9347.5h  0.87% Komödie
    9315.0h  0.87% Quiz
    8317.5h  0.78% Börsenmagazin
    8036.0h  0.75% Politikmagazin
    8026.9h  0.75% Wissensmagazin
    8019.1h  0.75% Realityshow
    7229.0h  0.68% Wirtschaftsmagazin
    7029.2h  0.66% Telenovela
    6965.8h  0.65% Dramaserie
