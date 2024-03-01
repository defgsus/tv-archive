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

**99** channels, **734,170.2** hours playtime between **2023-01-17** and **2024-03-02**


### playtime per genre (top 30)

    47819.8h 6.51% Nachrichten
    35243.2h 4.80% Verkaufsshow
    29852.0h 4.07% Krimiserie
    25380.8h 3.46% Werbesendung
    23495.4h 3.20% Dokureihe
    22179.4h 3.02% Dokusoap
    21314.7h 2.90% Regionalmagazin
    18924.2h 2.58% Dokumentation
    18772.5h 2.56% *unknown*
    13596.4h 1.85% Zeichentrickserie
    13348.7h 1.82% Infomercial
    12930.6h 1.76% Animationsserie
    11130.7h 1.52% Comedyserie
    10431.4h 1.42% Morgenmagazin
    9919.1h  1.35% Religionsmagazin
    9889.7h  1.35% Magazin
    9747.1h  1.33% Talkshow
    7261.9h  0.99% E-Sport
    6973.0h  0.95% Programmende
    6933.7h  0.94% Sitcom
    6558.3h  0.89% Börsenmagazin
    6528.7h  0.89% Wetterbericht
    6221.8h  0.85% Komödie
    6192.6h  0.84% Quiz
    5493.1h  0.75% Wissensmagazin
    5350.1h  0.73% Realityshow
    5327.9h  0.73% Wirtschaftsmagazin
    5294.5h  0.72% Politikmagazin
    5246.7h  0.71% Telenovela
    5043.1h  0.69% Musikmagazin
