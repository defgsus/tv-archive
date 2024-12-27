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

**109** channels, **1,201,385.4** hours playtime between **2023-01-17** and **2024-12-28**


### playtime per genre (top 30)

    78565.1h 6.54% Nachrichten
    54547.4h 4.54% Verkaufsshow
    49966.4h 4.16% Krimiserie
    44441.7h 3.70% Werbesendung
    37346.3h 3.11% Dokureihe
    35391.3h 2.95% Dokusoap
    35100.2h 2.92% Regionalmagazin
    31886.9h 2.65% Dokumentation
    28451.4h 2.37% *unknown*
    22544.2h 1.88% Zeichentrickserie
    22242.2h 1.85% Infomercial
    21461.2h 1.79% Animationsserie
    16973.5h 1.41% Comedyserie
    16811.5h 1.40% Morgenmagazin
    15897.8h 1.32% Talkshow
    15791.9h 1.31% Religionsmagazin
    14736.1h 1.23% Magazin
    11878.5h 0.99% E-Sport
    11525.2h 0.96% Sitcom
    10870.8h 0.90% Wetterbericht
    10841.2h 0.90% Komödie
    10630.3h 0.88% Quiz
    10569.6h 0.88% Programmende
    9271.1h  0.77% Realityshow
    9165.9h  0.76% Politikmagazin
    8961.8h  0.75% Wissensmagazin
    8728.0h  0.73% Börsenmagazin
    7988.6h  0.66% Wirtschaftsmagazin
    7972.1h  0.66% Arztserie
    7963.6h  0.66% Dramaserie
