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

**110** channels, **1,265,473.8** hours playtime between **2023-01-17** and **2025-02-09**


### playtime per genre (top 30)

    82991.2h 6.56% Nachrichten
    56840.4h 4.49% Verkaufsshow
    52544.4h 4.15% Krimiserie
    47229.7h 3.73% Werbesendung
    39274.6h 3.10% Dokureihe
    37122.7h 2.93% Dokusoap
    36805.7h 2.91% Regionalmagazin
    33882.0h 2.68% Dokumentation
    30104.2h 2.38% *unknown*
    23881.5h 1.89% Zeichentrickserie
    23561.4h 1.86% Infomercial
    22645.3h 1.79% Animationsserie
    17683.0h 1.40% Morgenmagazin
    17653.6h 1.40% Comedyserie
    16692.8h 1.32% Talkshow
    16383.9h 1.29% Religionsmagazin
    15126.5h 1.20% Magazin
    12544.6h 0.99% E-Sport
    12118.2h 0.96% Sitcom
    11565.3h 0.91% Komödie
    11478.9h 0.91% Wetterbericht
    11280.8h 0.89% Quiz
    11080.8h 0.88% Programmende
    9853.1h  0.78% Realityshow
    9674.3h  0.76% Politikmagazin
    9293.9h  0.73% Wissensmagazin
    8913.4h  0.70% Börsenmagazin
    8408.8h  0.66% Dramaserie
    8408.8h  0.66% Arztserie
    8359.9h  0.66% Wirtschaftsmagazin
