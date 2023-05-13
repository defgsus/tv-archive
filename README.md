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

**96** channels, **212,081.2** hours playtime between **2023-01-17** and **2023-05-14**


### playtime per genre (top 30)

    14306.0h 6.75% Nachrichten
    10331.9h 4.87% Verkaufsshow
    8639.6h  4.07% Krimiserie
    7043.6h  3.32% Werbesendung
    6859.9h  3.23% Dokureihe
    6275.2h  2.96% Dokusoap
    6107.6h  2.88% Regionalmagazin
    5391.0h  2.54% Dokumentation
    5233.8h  2.47% *unknown*
    3941.1h  1.86% Zeichentrickserie
    3890.2h  1.83% Infomercial
    3836.4h  1.81% Animationsserie
    3534.3h  1.67% Comedyserie
    2940.4h  1.39% Morgenmagazin
    2930.8h  1.38% Programmende
    2788.3h  1.31% Talkshow
    2767.8h  1.31% Religionsmagazin
    2402.3h  1.13% Magazin
    2137.5h  1.01% E-Sport
    2006.8h  0.95% Sitcom
    1923.6h  0.91% Börsenmagazin
    1921.5h  0.91% Wetterbericht
    1676.8h  0.79% Wirtschaftsmagazin
    1656.7h  0.78% Wissensmagazin
    1635.2h  0.77% Musikmagazin
    1626.2h  0.77% Quiz
    1498.8h  0.71% Telenovela
    1478.2h  0.70% Sportmagazin
    1447.2h  0.68% Gesundheitsmagazin
    1435.3h  0.68% Dramaserie
