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

**96** channels, **228,180.5** hours playtime between **2023-01-17** and **2023-05-23**


### playtime per genre (top 30)

    15321.2h 6.71% Nachrichten
    11045.2h 4.84% Verkaufsshow
    9210.4h  4.04% Krimiserie
    7584.0h  3.32% Werbesendung
    7455.2h  3.27% Dokureihe
    6792.2h  2.98% Dokusoap
    6530.4h  2.86% Regionalmagazin
    5826.9h  2.55% Dokumentation
    5646.9h  2.47% *unknown*
    4250.5h  1.86% Zeichentrickserie
    4180.9h  1.83% Infomercial
    4117.8h  1.80% Animationsserie
    3802.9h  1.67% Comedyserie
    3146.1h  1.38% Morgenmagazin
    3073.2h  1.35% Programmende
    3012.2h  1.32% Talkshow
    2994.1h  1.31% Religionsmagazin
    2617.6h  1.15% Magazin
    2282.1h  1.00% E-Sport
    2151.0h  0.94% Sitcom
    2077.8h  0.91% Börsenmagazin
    2068.1h  0.91% Wetterbericht
    1795.1h  0.79% Wirtschaftsmagazin
    1772.0h  0.78% Wissensmagazin
    1766.8h  0.77% Musikmagazin
    1762.5h  0.77% Quiz
    1599.7h  0.70% Telenovela
    1596.9h  0.70% Komödie
    1593.4h  0.70% Sportmagazin
    1532.2h  0.67% Gesundheitsmagazin
