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

**96** channels, **26,441.3** hours playtime between **2023-01-17** and **2023-01-31**


### playtime per genre (top 30)

    1842.2h 6.97% Nachrichten
    1423.2h 5.38% Verkaufsshow
    1098.1h 4.15% Krimiserie
    916.7h  3.47% Dokusoap
    864.6h  3.27% Werbesendung
    815.5h  3.08% Dokureihe
    755.2h  2.86% Regionalmagazin
    680.3h  2.57% Dokumentation
    659.6h  2.49% *unknown*
    515.8h  1.95% Zeichentrickserie
    509.6h  1.93% Infomercial
    460.9h  1.74% Animationsserie
    444.8h  1.68% Comedyserie
    350.5h  1.33% Morgenmagazin
    348.4h  1.32% Religionsmagazin
    347.5h  1.31% Talkshow
    321.4h  1.22% Programmende
    311.6h  1.18% Magazin
    285.8h  1.08% E-Sport
    233.3h  0.88% Sitcom
    224.2h  0.85% Wirtschaftsmagazin
    222.7h  0.84% Börsenmagazin
    222.4h  0.84% Wetterbericht
    213.3h  0.81% Wissensmagazin
    208.9h  0.79% Quiz
    202.1h  0.76% Dramaserie
    197.6h  0.75% Tennis
    196.7h  0.74% Musikmagazin
    185.1h  0.70% Gesundheitsmagazin
    184.0h  0.70% Realityshow
