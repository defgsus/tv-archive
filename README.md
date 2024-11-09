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

**109** channels, **1,130,515.8** hours playtime between **2023-01-17** and **2024-11-10**


### playtime per genre (top 30)

    73641.8h 6.51% Nachrichten
    51848.4h 4.59% Verkaufsshow
    47059.1h 4.16% Krimiserie
    41514.6h 3.67% Werbesendung
    35328.6h 3.12% Dokureihe
    33755.9h 2.99% Dokusoap
    33048.7h 2.92% Regionalmagazin
    29725.2h 2.63% Dokumentation
    26799.0h 2.37% *unknown*
    21139.8h 1.87% Zeichentrickserie
    20827.7h 1.84% Infomercial
    20219.4h 1.79% Animationsserie
    16248.0h 1.44% Comedyserie
    15809.0h 1.40% Morgenmagazin
    15131.0h 1.34% Religionsmagazin
    14964.1h 1.32% Talkshow
    14205.3h 1.26% Magazin
    11158.9h 0.99% E-Sport
    10921.5h 0.97% Sitcom
    10223.2h 0.90% Wetterbericht
    10009.1h 0.89% Programmende
    9965.7h  0.88% Komödie
    9960.2h  0.88% Quiz
    8626.5h  0.76% Realityshow
    8551.5h  0.76% Politikmagazin
    8512.8h  0.75% Börsenmagazin
    8487.5h  0.75% Wissensmagazin
    7579.8h  0.67% Wirtschaftsmagazin
    7462.9h  0.66% Telenovela
    7396.7h  0.65% Arztserie
