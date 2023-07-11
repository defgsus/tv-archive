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

**96** channels, **317,746.9** hours playtime between **2023-01-17** and **2023-07-12**


### playtime per genre (top 30)

    21153.6h 6.66% Nachrichten
    15208.8h 4.79% Verkaufsshow
    12754.4h 4.01% Krimiserie
    10657.6h 3.35% Werbesendung
    10333.9h 3.25% Dokureihe
    9626.9h  3.03% Dokusoap
    9098.3h  2.86% Regionalmagazin
    7994.3h  2.52% Dokumentation
    7822.0h  2.46% *unknown*
    6047.9h  1.90% Zeichentrickserie
    5815.8h  1.83% Infomercial
    5596.5h  1.76% Animationsserie
    5263.9h  1.66% Comedyserie
    4446.8h  1.40% Morgenmagazin
    4215.2h  1.33% Talkshow
    4205.4h  1.32% Religionsmagazin
    3770.3h  1.19% Magazin
    3761.8h  1.18% Programmende
    3143.2h  0.99% E-Sport
    3010.6h  0.95% Sitcom
    2949.3h  0.93% Wetterbericht
    2849.4h  0.90% Börsenmagazin
    2520.5h  0.79% Quiz
    2499.4h  0.79% Musikmagazin
    2467.0h  0.78% Wirtschaftsmagazin
    2433.9h  0.77% Wissensmagazin
    2417.5h  0.76% Komödie
    2224.2h  0.70% Telenovela
    2123.6h  0.67% Sportmagazin
    2012.3h  0.63% Dramaserie
