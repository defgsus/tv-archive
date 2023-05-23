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

**96** channels, **229,941.5** hours playtime between **2023-01-17** and **2023-05-24**


### playtime per genre (top 30)

    15439.1h 6.71% Nachrichten
    11118.3h 4.84% Verkaufsshow
    9304.0h  4.05% Krimiserie
    7646.4h  3.33% Werbesendung
    7499.9h  3.26% Dokureihe
    6843.2h  2.98% Dokusoap
    6582.7h  2.86% Regionalmagazin
    5862.8h  2.55% Dokumentation
    5689.1h  2.47% *unknown*
    4286.6h  1.86% Zeichentrickserie
    4213.3h  1.83% Infomercial
    4147.2h  1.80% Animationsserie
    3832.7h  1.67% Comedyserie
    3180.8h  1.38% Morgenmagazin
    3085.6h  1.34% Programmende
    3031.8h  1.32% Talkshow
    3014.8h  1.31% Religionsmagazin
    2635.3h  1.15% Magazin
    2305.8h  1.00% E-Sport
    2169.4h  0.94% Sitcom
    2104.3h  0.92% Börsenmagazin
    2085.9h  0.91% Wetterbericht
    1808.1h  0.79% Wirtschaftsmagazin
    1783.4h  0.78% Wissensmagazin
    1783.3h  0.78% Musikmagazin
    1772.5h  0.77% Quiz
    1619.8h  0.70% Telenovela
    1615.2h  0.70% Komödie
    1605.2h  0.70% Sportmagazin
    1543.9h  0.67% Gesundheitsmagazin
