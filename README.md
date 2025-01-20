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

**110** channels, **1,237,765.7** hours playtime between **2023-01-17** and **2025-01-21**


### playtime per genre (top 30)

    80998.1h 6.54% Nachrichten
    55884.6h 4.51% Verkaufsshow
    51312.8h 4.15% Krimiserie
    46014.2h 3.72% Werbesendung
    38493.0h 3.11% Dokureihe
    36363.9h 2.94% Dokusoap
    36009.4h 2.91% Regionalmagazin
    33038.7h 2.67% Dokumentation
    29536.3h 2.39% *unknown*
    23308.3h 1.88% Zeichentrickserie
    22926.8h 1.85% Infomercial
    22131.0h 1.79% Animationsserie
    17347.9h 1.40% Comedyserie
    17270.8h 1.40% Morgenmagazin
    16318.0h 1.32% Talkshow
    16133.0h 1.30% Religionsmagazin
    14998.1h 1.21% Magazin
    12268.9h 0.99% E-Sport
    11853.2h 0.96% Sitcom
    11326.9h 0.92% Komödie
    11212.0h 0.91% Wetterbericht
    10997.7h 0.89% Quiz
    10852.3h 0.88% Programmende
    9590.8h  0.77% Realityshow
    9441.4h  0.76% Politikmagazin
    9150.1h  0.74% Wissensmagazin
    8818.6h  0.71% Börsenmagazin
    8205.2h  0.66% Dramaserie
    8194.8h  0.66% Arztserie
    8175.3h  0.66% Wirtschaftsmagazin
