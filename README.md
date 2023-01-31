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

**96** channels, **28,234.6** hours playtime between **2023-01-17** and **2023-02-01**


### playtime per genre (top 30)

    1978.7h 7.01% Nachrichten
    1512.4h 5.36% Verkaufsshow
    1196.8h 4.24% Krimiserie
    978.2h  3.46% Dokusoap
    925.0h  3.28% Werbesendung
    868.2h  3.08% Dokureihe
    812.3h  2.88% Regionalmagazin
    712.6h  2.52% Dokumentation
    693.4h  2.46% *unknown*
    552.5h  1.96% Zeichentrickserie
    542.4h  1.92% Infomercial
    494.8h  1.75% Animationsserie
    480.9h  1.70% Comedyserie
    385.2h  1.36% Morgenmagazin
    371.3h  1.32% Religionsmagazin
    365.8h  1.30% Talkshow
    335.0h  1.19% Programmende
    329.5h  1.17% Magazin
    313.8h  1.11% E-Sport
    251.3h  0.89% Börsenmagazin
    250.8h  0.89% Sitcom
    239.2h  0.85% Wirtschaftsmagazin
    238.3h  0.84% Wetterbericht
    226.5h  0.80% Wissensmagazin
    219.0h  0.78% Quiz
    217.5h  0.77% Dramaserie
    213.7h  0.76% Musikmagazin
    200.5h  0.71% Tennis
    199.8h  0.71% Realityshow
    198.0h  0.70% Gesundheitsmagazin
