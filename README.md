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

**96** channels, **256,887.0** hours playtime between **2023-01-17** and **2023-06-08**


### playtime per genre (top 30)

    17156.2h 6.68% Nachrichten
    12391.3h 4.82% Verkaufsshow
    10310.9h 4.01% Krimiserie
    8539.3h  3.32% Werbesendung
    8363.6h  3.26% Dokureihe
    7662.6h  2.98% Dokusoap
    7353.0h  2.86% Regionalmagazin
    6579.6h  2.56% Dokumentation
    6393.2h  2.49% *unknown*
    4847.5h  1.89% Zeichentrickserie
    4706.5h  1.83% Infomercial
    4572.9h  1.78% Animationsserie
    4284.8h  1.67% Comedyserie
    3562.2h  1.39% Morgenmagazin
    3389.5h  1.32% Talkshow
    3371.4h  1.31% Religionsmagazin
    3293.5h  1.28% Programmende
    2986.8h  1.16% Magazin
    2574.8h  1.00% E-Sport
    2418.0h  0.94% Sitcom
    2350.0h  0.91% Wetterbericht
    2315.8h  0.90% Börsenmagazin
    2018.3h  0.79% Wirtschaftsmagazin
    2000.7h  0.78% Quiz
    2000.1h  0.78% Musikmagazin
    1988.9h  0.77% Wissensmagazin
    1899.3h  0.74% Komödie
    1826.1h  0.71% Telenovela
    1760.8h  0.69% Sportmagazin
    1684.0h  0.66% Gesundheitsmagazin
