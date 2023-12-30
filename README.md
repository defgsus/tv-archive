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

**97** channels, **624,215.0** hours playtime between **2023-01-17** and **2023-12-31**


### playtime per genre (top 30)

    40789.1h 6.53% Nachrichten
    29914.0h 4.79% Verkaufsshow
    25025.9h 4.01% Krimiserie
    21213.1h 3.40% Werbesendung
    20309.7h 3.25% Dokureihe
    18616.2h 2.98% Dokusoap
    17959.6h 2.88% Regionalmagazin
    16167.5h 2.59% Dokumentation
    15434.9h 2.47% *unknown*
    11496.2h 1.84% Zeichentrickserie
    11335.6h 1.82% Infomercial
    11003.0h 1.76% Animationsserie
    9494.8h  1.52% Comedyserie
    8846.7h  1.42% Morgenmagazin
    8451.9h  1.35% Religionsmagazin
    8277.4h  1.33% Talkshow
    8147.1h  1.31% Magazin
    6134.6h  0.98% E-Sport
    6115.1h  0.98% Programmende
    6053.6h  0.97% Sitcom
    5695.8h  0.91% Wetterbericht
    5594.5h  0.90% Börsenmagazin
    5229.0h  0.84% Komödie
    5115.5h  0.82% Quiz
    4719.8h  0.76% Wissensmagazin
    4608.8h  0.74% Wirtschaftsmagazin
    4502.6h  0.72% Realityshow
    4488.4h  0.72% Musikmagazin
    4476.2h  0.72% Telenovela
    4399.9h  0.70% Politikmagazin
