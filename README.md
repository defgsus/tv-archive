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

**110** channels, **1,213,541.6** hours playtime between **2023-01-17** and **2025-01-05**


### playtime per genre (top 30)

    79290.0h 6.53% Nachrichten
    54983.0h 4.53% Verkaufsshow
    50302.6h 4.15% Krimiserie
    44972.1h 3.71% Werbesendung
    37781.9h 3.11% Dokureihe
    35683.6h 2.94% Dokusoap
    35326.9h 2.91% Regionalmagazin
    32328.4h 2.66% Dokumentation
    28861.2h 2.38% *unknown*
    22807.1h 1.88% Zeichentrickserie
    22456.7h 1.85% Infomercial
    21678.3h 1.79% Animationsserie
    17105.6h 1.41% Comedyserie
    16919.7h 1.39% Morgenmagazin
    15999.5h 1.32% Talkshow
    15901.8h 1.31% Religionsmagazin
    14830.2h 1.22% Magazin
    11995.1h 0.99% E-Sport
    11615.4h 0.96% Sitcom
    11128.1h 0.92% Komödie
    10979.0h 0.90% Wetterbericht
    10727.2h 0.88% Quiz
    10666.4h 0.88% Programmende
    9374.3h  0.77% Realityshow
    9225.8h  0.76% Politikmagazin
    9021.6h  0.74% Wissensmagazin
    8745.2h  0.72% Börsenmagazin
    8029.4h  0.66% Wirtschaftsmagazin
    8022.1h  0.66% Dramaserie
    8019.8h  0.66% Arztserie
