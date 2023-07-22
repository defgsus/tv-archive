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

**96** channels, **337,496.0** hours playtime between **2023-01-17** and **2023-07-23**


### playtime per genre (top 30)

    22437.6h 6.65% Nachrichten
    16125.3h 4.78% Verkaufsshow
    13574.1h 4.02% Krimiserie
    11332.2h 3.36% Werbesendung
    11009.1h 3.26% Dokureihe
    10219.8h 3.03% Dokusoap
    9665.4h  2.86% Regionalmagazin
    8488.1h  2.52% Dokumentation
    8232.1h  2.44% *unknown*
    6410.9h  1.90% Zeichentrickserie
    6169.7h  1.83% Infomercial
    5947.3h  1.76% Animationsserie
    5576.0h  1.65% Comedyserie
    4727.1h  1.40% Morgenmagazin
    4467.0h  1.32% Talkshow
    4466.8h  1.32% Religionsmagazin
    4023.2h  1.19% Magazin
    3913.5h  1.16% Programmende
    3342.0h  0.99% E-Sport
    3199.1h  0.95% Sitcom
    3156.7h  0.94% Wetterbericht
    3036.2h  0.90% Börsenmagazin
    2691.3h  0.80% Quiz
    2642.2h  0.78% Musikmagazin
    2606.9h  0.77% Wirtschaftsmagazin
    2585.3h  0.77% Komödie
    2569.1h  0.76% Wissensmagazin
    2332.3h  0.69% Telenovela
    2226.3h  0.66% Sportmagazin
    2155.8h  0.64% Reportagereihe
