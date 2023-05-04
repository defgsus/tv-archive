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

**96** channels, **195,789.8** hours playtime between **2023-01-17** and **2023-05-05**


### playtime per genre (top 30)

    13285.7h 6.79% Nachrichten
    9579.3h  4.89% Verkaufsshow
    7982.8h  4.08% Krimiserie
    6506.2h  3.32% Werbesendung
    6312.3h  3.22% Dokureihe
    5838.1h  2.98% Dokusoap
    5658.9h  2.89% Regionalmagazin
    4964.2h  2.54% Dokumentation
    4754.5h  2.43% *unknown*
    3626.2h  1.85% Zeichentrickserie
    3582.6h  1.83% Infomercial
    3561.9h  1.82% Animationsserie
    3276.0h  1.67% Comedyserie
    2720.7h  1.39% Morgenmagazin
    2707.9h  1.38% Programmende
    2566.0h  1.31% Talkshow
    2549.2h  1.30% Religionsmagazin
    2185.5h  1.12% Magazin
    1974.3h  1.01% E-Sport
    1856.0h  0.95% Sitcom
    1770.8h  0.90% Börsenmagazin
    1770.5h  0.90% Wetterbericht
    1556.4h  0.79% Wirtschaftsmagazin
    1532.5h  0.78% Wissensmagazin
    1505.2h  0.77% Musikmagazin
    1504.0h  0.77% Quiz
    1383.8h  0.71% Telenovela
    1358.0h  0.69% Sportmagazin
    1354.0h  0.69% Gesundheitsmagazin
    1333.5h  0.68% Dramaserie
