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

**109** channels, **1,137,716.1** hours playtime between **2023-01-17** and **2024-11-14**


### playtime per genre (top 30)

    74154.7h 6.52% Nachrichten
    52092.4h 4.58% Verkaufsshow
    47395.4h 4.17% Krimiserie
    41828.1h 3.68% Werbesendung
    35502.3h 3.12% Dokureihe
    33957.2h 2.98% Dokusoap
    33284.6h 2.93% Regionalmagazin
    29905.0h 2.63% Dokumentation
    26906.6h 2.36% *unknown*
    21276.6h 1.87% Zeichentrickserie
    20969.8h 1.84% Infomercial
    20340.3h 1.79% Animationsserie
    16337.1h 1.44% Comedyserie
    15914.1h 1.40% Morgenmagazin
    15205.8h 1.34% Religionsmagazin
    15056.1h 1.32% Talkshow
    14262.9h 1.25% Magazin
    11234.7h 0.99% E-Sport
    11003.8h 0.97% Sitcom
    10290.9h 0.90% Wetterbericht
    10066.8h 0.88% Programmende
    10041.1h 0.88% Quiz
    10002.3h 0.88% Komödie
    8699.8h  0.76% Realityshow
    8627.6h  0.76% Politikmagazin
    8546.9h  0.75% Wissensmagazin
    8537.9h  0.75% Börsenmagazin
    7628.1h  0.67% Wirtschaftsmagazin
    7519.7h  0.66% Telenovela
    7464.9h  0.66% Dramaserie
