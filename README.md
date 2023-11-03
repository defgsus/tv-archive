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

**97** channels, **523,708.4** hours playtime between **2023-01-17** and **2023-11-04**


### playtime per genre (top 30)

    34510.3h 6.59% Nachrichten
    25019.1h 4.78% Verkaufsshow
    21054.2h 4.02% Krimiserie
    17731.0h 3.39% Werbesendung
    17212.1h 3.29% Dokureihe
    15944.5h 3.04% Dokusoap
    15132.6h 2.89% Regionalmagazin
    13340.9h 2.55% Dokumentation
    12641.6h 2.41% *unknown*
    9746.9h  1.86% Zeichentrickserie
    9534.5h  1.82% Infomercial
    9368.8h  1.79% Animationsserie
    8276.4h  1.58% Comedyserie
    7460.9h  1.42% Morgenmagazin
    7052.2h  1.35% Religionsmagazin
    6971.6h  1.33% Talkshow
    6618.5h  1.26% Magazin
    5347.0h  1.02% Programmende
    5145.2h  0.98% E-Sport
    5007.5h  0.96% Sitcom
    4847.4h  0.93% Wetterbericht
    4743.1h  0.91% Börsenmagazin
    4388.8h  0.84% Quiz
    4094.6h  0.78% Komödie
    3962.7h  0.76% Wissensmagazin
    3952.6h  0.75% Wirtschaftsmagazin
    3912.8h  0.75% Musikmagazin
    3776.8h  0.72% Telenovela
    3621.0h  0.69% Politikmagazin
    3536.3h  0.68% Realityshow
