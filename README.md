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

**97** channels, **617,089.4** hours playtime between **2023-01-17** and **2023-12-27**


### playtime per genre (top 30)

    40390.5h 6.55% Nachrichten
    29578.7h 4.79% Verkaufsshow
    24793.4h 4.02% Krimiserie
    20968.8h 3.40% Werbesendung
    20028.0h 3.25% Dokureihe
    18458.8h 2.99% Dokusoap
    17781.6h 2.88% Regionalmagazin
    15915.4h 2.58% Dokumentation
    15198.2h 2.46% *unknown*
    11374.4h 1.84% Zeichentrickserie
    11203.1h 1.82% Infomercial
    10867.1h 1.76% Animationsserie
    9406.5h  1.52% Comedyserie
    8743.0h  1.42% Morgenmagazin
    8368.6h  1.36% Religionsmagazin
    8211.3h  1.33% Talkshow
    8035.6h  1.30% Magazin
    6083.5h  0.99% E-Sport
    6060.1h  0.98% Programmende
    5976.1h  0.97% Sitcom
    5632.9h  0.91% Wetterbericht
    5542.8h  0.90% Börsenmagazin
    5077.0h  0.82% Quiz
    5057.3h  0.82% Komödie
    4679.2h  0.76% Wissensmagazin
    4574.2h  0.74% Wirtschaftsmagazin
    4463.4h  0.72% Realityshow
    4450.3h  0.72% Telenovela
    4446.9h  0.72% Musikmagazin
    4367.1h  0.71% Politikmagazin
