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

**96** channels, **256,887.2** hours playtime between **2023-01-17** and **2023-06-08**


### playtime per genre (top 30)

    17156.1h 6.68% Nachrichten
    12388.3h 4.82% Verkaufsshow
    10308.3h 4.01% Krimiserie
    8539.3h  3.32% Werbesendung
    8361.7h  3.26% Dokureihe
    7662.6h  2.98% Dokusoap
    7353.0h  2.86% Regionalmagazin
    6579.6h  2.56% Dokumentation
    6393.2h  2.49% *unknown*
    4846.6h  1.89% Zeichentrickserie
    4706.5h  1.83% Infomercial
    4573.1h  1.78% Animationsserie
    4284.8h  1.67% Comedyserie
    3561.7h  1.39% Morgenmagazin
    3390.3h  1.32% Talkshow
    3371.4h  1.31% Religionsmagazin
    3293.4h  1.28% Programmende
    2990.8h  1.16% Magazin
    2574.8h  1.00% E-Sport
    2418.0h  0.94% Sitcom
    2349.8h  0.91% Wetterbericht
    2315.5h  0.90% Börsenmagazin
    2018.3h  0.79% Wirtschaftsmagazin
    2000.1h  0.78% Musikmagazin
    1999.8h  0.78% Quiz
    1989.0h  0.77% Wissensmagazin
    1899.3h  0.74% Komödie
    1826.0h  0.71% Telenovela
    1760.8h  0.69% Sportmagazin
    1684.0h  0.66% Gesundheitsmagazin
