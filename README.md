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

**109** channels, **1,054,438.5** hours playtime between **2023-01-17** and **2024-09-20**


### playtime per genre (top 30)

    68624.6h 6.51% Nachrichten
    48946.9h 4.64% Verkaufsshow
    43533.7h 4.13% Krimiserie
    38281.4h 3.63% Werbesendung
    33092.5h 3.14% Dokureihe
    31739.3h 3.01% Dokusoap
    30822.6h 2.92% Regionalmagazin
    27583.2h 2.62% Dokumentation
    25349.8h 2.40% *unknown*
    19567.0h 1.86% Zeichentrickserie
    19350.3h 1.84% Infomercial
    18887.9h 1.79% Animationsserie
    15416.1h 1.46% Comedyserie
    14779.1h 1.40% Morgenmagazin
    14337.4h 1.36% Religionsmagazin
    13877.8h 1.32% Talkshow
    13704.8h 1.30% Magazin
    10432.0h 0.99% E-Sport
    10112.4h 0.96% Sitcom
    9547.6h  0.91% Wetterbericht
    9429.4h  0.89% Programmende
    9260.4h  0.88% Komödie
    9161.9h  0.87% Quiz
    8282.9h  0.79% Börsenmagazin
    7922.0h  0.75% Politikmagazin
    7911.8h  0.75% Wissensmagazin
    7897.2h  0.75% Realityshow
    7162.2h  0.68% Wirtschaftsmagazin
    6953.9h  0.66% Telenovela
    6886.7h  0.65% Dramaserie
