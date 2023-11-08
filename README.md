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

**97** channels, **532,689.4** hours playtime between **2023-01-17** and **2023-11-09**


### playtime per genre (top 30)

    35080.3h 6.59% Nachrichten
    25451.4h 4.78% Verkaufsshow
    21412.5h 4.02% Krimiserie
    18047.4h 3.39% Werbesendung
    17444.6h 3.27% Dokureihe
    16188.8h 3.04% Dokusoap
    15387.6h 2.89% Regionalmagazin
    13576.7h 2.55% Dokumentation
    12910.0h 2.42% *unknown*
    9903.1h  1.86% Zeichentrickserie
    9696.0h  1.82% Infomercial
    9522.3h  1.79% Animationsserie
    8397.8h  1.58% Comedyserie
    7579.8h  1.42% Morgenmagazin
    7179.9h  1.35% Religionsmagazin
    7104.8h  1.33% Talkshow
    6763.5h  1.27% Magazin
    5416.2h  1.02% Programmende
    5227.4h  0.98% E-Sport
    5103.4h  0.96% Sitcom
    4924.2h  0.92% Wetterbericht
    4823.9h  0.91% Börsenmagazin
    4452.2h  0.84% Quiz
    4166.7h  0.78% Komödie
    4030.8h  0.76% Wissensmagazin
    4010.8h  0.75% Wirtschaftsmagazin
    3955.8h  0.74% Musikmagazin
    3837.2h  0.72% Telenovela
    3684.5h  0.69% Politikmagazin
    3611.5h  0.68% Realityshow
