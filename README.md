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

**109** channels, **1,203,113.5** hours playtime between **2023-01-17** and **2024-12-29**


### playtime per genre (top 30)

    78659.1h 6.54% Nachrichten
    54603.4h 4.54% Verkaufsshow
    50005.1h 4.16% Krimiserie
    44513.2h 3.70% Werbesendung
    37416.5h 3.11% Dokureihe
    35440.4h 2.95% Dokusoap
    35121.5h 2.92% Regionalmagazin
    31958.0h 2.66% Dokumentation
    28499.4h 2.37% *unknown*
    22577.2h 1.88% Zeichentrickserie
    22275.4h 1.85% Infomercial
    21499.1h 1.79% Animationsserie
    16984.8h 1.41% Comedyserie
    16819.5h 1.40% Morgenmagazin
    15918.8h 1.32% Talkshow
    15807.5h 1.31% Religionsmagazin
    14743.6h 1.23% Magazin
    11898.6h 0.99% E-Sport
    11542.0h 0.96% Sitcom
    10898.0h 0.91% Komödie
    10885.2h 0.90% Wetterbericht
    10643.1h 0.88% Quiz
    10583.8h 0.88% Programmende
    9276.3h  0.77% Realityshow
    9167.5h  0.76% Politikmagazin
    8969.2h  0.75% Wissensmagazin
    8727.9h  0.73% Börsenmagazin
    7988.2h  0.66% Wirtschaftsmagazin
    7985.4h  0.66% Arztserie
    7967.8h  0.66% Dramaserie
