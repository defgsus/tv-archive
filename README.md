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

**109** channels, **1,058,073.9** hours playtime between **2023-01-17** and **2024-09-23**


### playtime per genre (top 30)

    68801.9h 6.50% Nachrichten
    49064.7h 4.64% Verkaufsshow
    43660.9h 4.13% Krimiserie
    38424.7h 3.63% Werbesendung
    33218.9h 3.14% Dokureihe
    31818.5h 3.01% Dokusoap
    30871.1h 2.92% Regionalmagazin
    27705.0h 2.62% Dokumentation
    25427.2h 2.40% *unknown*
    19634.4h 1.86% Zeichentrickserie
    19425.1h 1.84% Infomercial
    18958.9h 1.79% Animationsserie
    15441.5h 1.46% Comedyserie
    14797.1h 1.40% Morgenmagazin
    14405.7h 1.36% Religionsmagazin
    13947.4h 1.32% Talkshow
    13737.7h 1.30% Magazin
    10475.0h 0.99% E-Sport
    10131.9h 0.96% Sitcom
    9578.0h  0.91% Wetterbericht
    9457.3h  0.89% Programmende
    9291.1h  0.88% Komödie
    9183.9h  0.87% Quiz
    8282.8h  0.78% Börsenmagazin
    7945.4h  0.75% Wissensmagazin
    7925.5h  0.75% Politikmagazin
    7920.5h  0.75% Realityshow
    7167.1h  0.68% Wirtschaftsmagazin
    6955.4h  0.66% Telenovela
    6881.7h  0.65% Dramaserie
