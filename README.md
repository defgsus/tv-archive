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

**109** channels, **1,201,354.3** hours playtime between **2023-01-17** and **2024-12-27**


### playtime per genre (top 30)

    78537.0h 6.54% Nachrichten
    54534.0h 4.54% Verkaufsshow
    49921.5h 4.16% Krimiserie
    44429.2h 3.70% Werbesendung
    37362.2h 3.11% Dokureihe
    35376.5h 2.94% Dokusoap
    35073.9h 2.92% Regionalmagazin
    31926.7h 2.66% Dokumentation
    28458.0h 2.37% *unknown*
    22540.2h 1.88% Zeichentrickserie
    22231.6h 1.85% Infomercial
    21452.7h 1.79% Animationsserie
    16969.0h 1.41% Comedyserie
    16782.8h 1.40% Morgenmagazin
    15892.2h 1.32% Talkshow
    15784.8h 1.31% Religionsmagazin
    14733.9h 1.23% Magazin
    11880.2h 0.99% E-Sport
    11518.4h 0.96% Sitcom
    10903.2h 0.91% Komödie
    10869.8h 0.90% Wetterbericht
    10613.8h 0.88% Quiz
    10569.4h 0.88% Programmende
    9265.0h  0.77% Realityshow
    9171.7h  0.76% Politikmagazin
    8961.4h  0.75% Wissensmagazin
    8723.7h  0.73% Börsenmagazin
    7993.5h  0.67% Wirtschaftsmagazin
    7965.2h  0.66% Arztserie
    7964.4h  0.66% Dramaserie
