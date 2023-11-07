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

**97** channels, **530,892.1** hours playtime between **2023-01-17** and **2023-11-08**


### playtime per genre (top 30)

    34939.8h 6.58% Nachrichten
    25357.6h 4.78% Verkaufsshow
    21353.6h 4.02% Krimiserie
    17990.8h 3.39% Werbesendung
    17395.8h 3.28% Dokureihe
    16140.3h 3.04% Dokusoap
    15320.1h 2.89% Regionalmagazin
    13533.3h 2.55% Dokumentation
    12869.4h 2.42% *unknown*
    9874.4h  1.86% Zeichentrickserie
    9663.6h  1.82% Infomercial
    9491.0h  1.79% Animationsserie
    8370.1h  1.58% Comedyserie
    7544.3h  1.42% Morgenmagazin
    7167.8h  1.35% Religionsmagazin
    7074.8h  1.33% Talkshow
    6717.3h  1.27% Magazin
    5401.7h  1.02% Programmende
    5209.9h  0.98% E-Sport
    5073.8h  0.96% Sitcom
    4908.1h  0.92% Wetterbericht
    4810.0h  0.91% Börsenmagazin
    4436.1h  0.84% Quiz
    4154.3h  0.78% Komödie
    4011.0h  0.76% Wissensmagazin
    3993.1h  0.75% Wirtschaftsmagazin
    3947.5h  0.74% Musikmagazin
    3819.1h  0.72% Telenovela
    3666.0h  0.69% Politikmagazin
    3597.2h  0.68% Realityshow
