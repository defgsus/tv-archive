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

**109** channels, **1,103,327.4** hours playtime between **2023-01-17** and **2024-10-23**


### playtime per genre (top 30)

    71832.0h 6.51% Nachrichten
    50837.3h 4.61% Verkaufsshow
    45831.5h 4.15% Krimiserie
    40381.1h 3.66% Werbesendung
    34521.2h 3.13% Dokureihe
    33001.3h 2.99% Dokusoap
    32258.8h 2.92% Regionalmagazin
    28918.0h 2.62% Dokumentation
    26215.5h 2.38% *unknown*
    20582.3h 1.87% Zeichentrickserie
    20300.4h 1.84% Infomercial
    19742.2h 1.79% Animationsserie
    15949.6h 1.45% Comedyserie
    15434.4h 1.40% Morgenmagazin
    14879.5h 1.35% Religionsmagazin
    14583.7h 1.32% Talkshow
    14026.3h 1.27% Magazin
    10911.3h 0.99% E-Sport
    10623.1h 0.96% Sitcom
    9996.3h  0.91% Wetterbericht
    9803.5h  0.89% Programmende
    9677.2h  0.88% Quiz
    9671.9h  0.88% Komödie
    8427.8h  0.76% Börsenmagazin
    8393.7h  0.76% Realityshow
    8343.9h  0.76% Politikmagazin
    8290.6h  0.75% Wissensmagazin
    7423.9h  0.67% Wirtschaftsmagazin
    7274.6h  0.66% Telenovela
    7209.4h  0.65% Dramaserie
