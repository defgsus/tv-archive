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

**99** channels, **693,251.4** hours playtime between **2023-01-17** and **2024-02-08**


### playtime per genre (top 30)

    45198.7h 6.52% Nachrichten
    33239.4h 4.79% Verkaufsshow
    27999.9h 4.04% Krimiserie
    23789.7h 3.43% Werbesendung
    22386.6h 3.23% Dokureihe
    20846.8h 3.01% Dokusoap
    20057.1h 2.89% Regionalmagazin
    17888.7h 2.58% Dokumentation
    17488.4h 2.52% *unknown*
    12860.3h 1.86% Zeichentrickserie
    12597.9h 1.82% Infomercial
    12191.5h 1.76% Animationsserie
    10492.8h 1.51% Comedyserie
    9817.6h  1.42% Morgenmagazin
    9375.2h  1.35% Religionsmagazin
    9219.6h  1.33% Magazin
    9184.9h  1.32% Talkshow
    6816.8h  0.98% E-Sport
    6654.7h  0.96% Programmende
    6619.2h  0.95% Sitcom
    6194.5h  0.89% Wetterbericht
    6178.7h  0.89% Börsenmagazin
    5867.0h  0.85% Komödie
    5772.4h  0.83% Quiz
    5218.7h  0.75% Wissensmagazin
    5097.8h  0.74% Realityshow
    5052.4h  0.73% Wirtschaftsmagazin
    4957.6h  0.72% Politikmagazin
    4938.6h  0.71% Telenovela
    4837.5h  0.70% Musikmagazin
