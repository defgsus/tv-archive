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

**96** channels, **208,468.2** hours playtime between **2023-01-17** and **2023-05-12**


### playtime per genre (top 30)

    14097.4h 6.76% Nachrichten
    10166.3h 4.88% Verkaufsshow
    8498.4h  4.08% Krimiserie
    6923.4h  3.32% Werbesendung
    6746.0h  3.24% Dokureihe
    6197.0h  2.97% Dokusoap
    6023.2h  2.89% Regionalmagazin
    5293.4h  2.54% Dokumentation
    5147.6h  2.47% *unknown*
    3869.2h  1.86% Zeichentrickserie
    3820.8h  1.83% Infomercial
    3773.5h  1.81% Animationsserie
    3492.6h  1.68% Comedyserie
    2900.2h  1.39% Morgenmagazin
    2882.4h  1.38% Programmende
    2741.0h  1.31% Talkshow
    2724.7h  1.31% Religionsmagazin
    2350.6h  1.13% Magazin
    2106.6h  1.01% E-Sport
    1974.2h  0.95% Sitcom
    1894.0h  0.91% Börsenmagazin
    1887.6h  0.91% Wetterbericht
    1653.7h  0.79% Wirtschaftsmagazin
    1629.6h  0.78% Wissensmagazin
    1611.4h  0.77% Musikmagazin
    1601.8h  0.77% Quiz
    1480.3h  0.71% Telenovela
    1451.4h  0.70% Sportmagazin
    1428.7h  0.69% Gesundheitsmagazin
    1418.4h  0.68% Dramaserie
