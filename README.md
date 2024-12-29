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

**109** channels, **1,204,855.4** hours playtime between **2023-01-17** and **2024-12-30**


### playtime per genre (top 30)

    78758.0h 6.54% Nachrichten
    54671.1h 4.54% Verkaufsshow
    50054.2h 4.15% Krimiserie
    44590.7h 3.70% Werbesendung
    37476.3h 3.11% Dokureihe
    35492.4h 2.95% Dokusoap
    35146.4h 2.92% Regionalmagazin
    32009.5h 2.66% Dokumentation
    28568.4h 2.37% *unknown*
    22614.0h 1.88% Zeichentrickserie
    22308.2h 1.85% Infomercial
    21528.2h 1.79% Animationsserie
    16996.8h 1.41% Comedyserie
    16828.4h 1.40% Morgenmagazin
    15943.8h 1.32% Talkshow
    15837.7h 1.31% Religionsmagazin
    14758.2h 1.22% Magazin
    11918.2h 0.99% E-Sport
    11545.3h 0.96% Sitcom
    10946.4h 0.91% Komödie
    10899.5h 0.90% Wetterbericht
    10645.6h 0.88% Quiz
    10597.2h 0.88% Programmende
    9291.3h  0.77% Realityshow
    9170.8h  0.76% Politikmagazin
    8980.4h  0.75% Wissensmagazin
    8727.9h  0.72% Börsenmagazin
    7993.6h  0.66% Wirtschaftsmagazin
    7990.7h  0.66% Arztserie
    7969.4h  0.66% Dramaserie
