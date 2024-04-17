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

**102** channels, **814,135.8** hours playtime between **2023-01-17** and **2024-04-18**


### playtime per genre (top 30)

    53014.9h 6.51% Nachrichten
    39064.6h 4.80% Verkaufsshow
    33146.0h 4.07% Krimiserie
    28421.6h 3.49% Werbesendung
    25793.0h 3.17% Dokureihe
    24555.7h 3.02% Dokusoap
    23681.3h 2.91% Regionalmagazin
    21067.0h 2.59% Dokumentation
    20868.3h 2.56% *unknown*
    14943.0h 1.84% Zeichentrickserie
    14779.4h 1.82% Infomercial
    14477.0h 1.78% Animationsserie
    12344.9h 1.52% Comedyserie
    11500.4h 1.41% Morgenmagazin
    11349.6h 1.39% Magazin
    10985.1h 1.35% Religionsmagazin
    10836.5h 1.33% Talkshow
    8038.4h  0.99% E-Sport
    7592.6h  0.93% Programmende
    7522.1h  0.92% Sitcom
    7223.8h  0.89% Wetterbericht
    7179.9h  0.88% Börsenmagazin
    7019.9h  0.86% Quiz
    6962.2h  0.86% Komödie
    6039.0h  0.74% Wissensmagazin
    5945.9h  0.73% Politikmagazin
    5865.7h  0.72% Realityshow
    5833.6h  0.72% Wirtschaftsmagazin
    5824.5h  0.72% Telenovela
    5451.8h  0.67% Musikmagazin
