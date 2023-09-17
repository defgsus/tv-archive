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

**97** channels, **439,568.2** hours playtime between **2023-01-17** and **2023-09-18**


### playtime per genre (top 30)

    28980.7h 6.59% Nachrichten
    20873.8h 4.75% Verkaufsshow
    17781.0h 4.05% Krimiserie
    14837.0h 3.38% Werbesendung
    14487.9h 3.30% Dokureihe
    13350.8h 3.04% Dokusoap
    12642.8h 2.88% Regionalmagazin
    11085.8h 2.52% Dokumentation
    10420.6h 2.37% *unknown*
    8290.5h  1.89% Zeichentrickserie
    8019.9h  1.82% Infomercial
    7793.1h  1.77% Animationsserie
    7106.6h  1.62% Comedyserie
    6201.7h  1.41% Morgenmagazin
    5892.4h  1.34% Religionsmagazin
    5833.5h  1.33% Talkshow
    5496.2h  1.25% Magazin
    4702.8h  1.07% Programmende
    4343.7h  0.99% E-Sport
    4145.2h  0.94% Wetterbericht
    4127.4h  0.94% Sitcom
    3959.2h  0.90% Börsenmagazin
    3632.9h  0.83% Quiz
    3438.6h  0.78% Musikmagazin
    3417.4h  0.78% Komödie
    3321.2h  0.76% Wirtschaftsmagazin
    3286.5h  0.75% Wissensmagazin
    3095.3h  0.70% Telenovela
    2895.9h  0.66% Reportagereihe
    2866.8h  0.65% Politikmagazin
