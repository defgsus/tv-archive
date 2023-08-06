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

**96** channels, **364,377.0** hours playtime between **2023-01-17** and **2023-08-07**


### playtime per genre (top 30)

    24097.4h 6.61% Nachrichten
    17343.8h 4.76% Verkaufsshow
    14705.1h 4.04% Krimiserie
    12281.4h 3.37% Werbesendung
    11996.3h 3.29% Dokureihe
    11006.3h 3.02% Dokusoap
    10430.4h 2.86% Regionalmagazin
    9186.2h  2.52% Dokumentation
    8880.5h  2.44% *unknown*
    6893.6h  1.89% Zeichentrickserie
    6662.5h  1.83% Infomercial
    6434.6h  1.77% Animationsserie
    5970.9h  1.64% Comedyserie
    5092.0h  1.40% Morgenmagazin
    4854.4h  1.33% Religionsmagazin
    4816.6h  1.32% Talkshow
    4351.6h  1.19% Magazin
    4116.3h  1.13% Programmende
    3606.1h  0.99% E-Sport
    3424.7h  0.94% Sitcom
    3424.3h  0.94% Wetterbericht
    3298.7h  0.91% Börsenmagazin
    2899.0h  0.80% Quiz
    2866.9h  0.79% Musikmagazin
    2803.8h  0.77% Komödie
    2792.2h  0.77% Wirtschaftsmagazin
    2745.8h  0.75% Wissensmagazin
    2511.6h  0.69% Telenovela
    2370.1h  0.65% Sportmagazin
    2352.7h  0.65% Reportagereihe
