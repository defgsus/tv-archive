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

**102** channels, **822,827.4** hours playtime between **2023-01-17** and **2024-04-23**


### playtime per genre (top 30)

    53599.2h 6.51% Nachrichten
    39478.5h 4.80% Verkaufsshow
    33488.4h 4.07% Krimiserie
    28751.2h 3.49% Werbesendung
    26038.3h 3.16% Dokureihe
    24819.6h 3.02% Dokusoap
    23927.8h 2.91% Regionalmagazin
    21291.5h 2.59% Dokumentation
    21058.7h 2.56% *unknown*
    15102.0h 1.84% Zeichentrickserie
    14942.6h 1.82% Infomercial
    14649.6h 1.78% Animationsserie
    12464.1h 1.51% Comedyserie
    11605.2h 1.41% Morgenmagazin
    11504.6h 1.40% Magazin
    11106.9h 1.35% Religionsmagazin
    10959.9h 1.33% Talkshow
    8135.8h  0.99% E-Sport
    7662.6h  0.93% Programmende
    7580.1h  0.92% Sitcom
    7298.5h  0.89% Wetterbericht
    7240.3h  0.88% Börsenmagazin
    7106.7h  0.86% Quiz
    7022.5h  0.85% Komödie
    6099.6h  0.74% Wissensmagazin
    6002.4h  0.73% Politikmagazin
    5942.0h  0.72% Realityshow
    5887.1h  0.72% Wirtschaftsmagazin
    5883.2h  0.72% Telenovela
    5493.0h  0.67% Musikmagazin
