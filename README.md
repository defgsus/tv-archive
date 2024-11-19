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

**109** channels, **1,146,783.9** hours playtime between **2023-01-17** and **2024-11-20**


### playtime per genre (top 30)

    74765.4h 6.52% Nachrichten
    52412.6h 4.57% Verkaufsshow
    47849.6h 4.17% Krimiserie
    42203.7h 3.68% Werbesendung
    35792.4h 3.12% Dokureihe
    34183.9h 2.98% Dokusoap
    33548.3h 2.93% Regionalmagazin
    30136.0h 2.63% Dokumentation
    27091.7h 2.36% *unknown*
    21460.7h 1.87% Zeichentrickserie
    21153.2h 1.84% Infomercial
    20488.0h 1.79% Animationsserie
    16431.2h 1.43% Comedyserie
    16035.3h 1.40% Morgenmagazin
    15300.0h 1.33% Religionsmagazin
    15188.6h 1.32% Talkshow
    14335.3h 1.25% Magazin
    11327.0h 0.99% E-Sport
    11096.7h 0.97% Sitcom
    10375.3h 0.90% Wetterbericht
    10135.6h 0.88% Programmende
    10133.4h 0.88% Quiz
    10081.8h 0.88% Komödie
    8788.3h  0.77% Realityshow
    8697.8h  0.76% Politikmagazin
    8618.1h  0.75% Wissensmagazin
    8561.3h  0.75% Börsenmagazin
    7674.2h  0.67% Wirtschaftsmagazin
    7577.2h  0.66% Telenovela
    7534.5h  0.66% Dramaserie
