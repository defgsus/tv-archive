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

**96** channels, **206,644.2** hours playtime between **2023-01-17** and **2023-05-11**


### playtime per genre (top 30)

    13960.7h 6.76% Nachrichten
    10088.4h 4.88% Verkaufsshow
    8413.6h  4.07% Krimiserie
    6872.9h  3.33% Werbesendung
    6694.6h  3.24% Dokureihe
    6132.0h  2.97% Dokusoap
    5961.6h  2.88% Regionalmagazin
    5267.1h  2.55% Dokumentation
    5069.7h  2.45% *unknown*
    3838.0h  1.86% Zeichentrickserie
    3786.7h  1.83% Infomercial
    3746.2h  1.81% Animationsserie
    3454.2h  1.67% Comedyserie
    2865.9h  1.39% Morgenmagazin
    2847.0h  1.38% Programmende
    2720.0h  1.32% Talkshow
    2702.8h  1.31% Religionsmagazin
    2314.6h  1.12% Magazin
    2080.9h  1.01% E-Sport
    1957.0h  0.95% Sitcom
    1882.7h  0.91% Börsenmagazin
    1870.8h  0.91% Wetterbericht
    1637.4h  0.79% Wirtschaftsmagazin
    1619.2h  0.78% Wissensmagazin
    1596.3h  0.77% Musikmagazin
    1584.7h  0.77% Quiz
    1462.5h  0.71% Telenovela
    1443.7h  0.70% Sportmagazin
    1421.4h  0.69% Gesundheitsmagazin
    1405.7h  0.68% Dramaserie
