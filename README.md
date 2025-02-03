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

**110** channels, **1,258,559.5** hours playtime between **2023-01-17** and **2025-02-04**


### playtime per genre (top 30)

    82488.5h 6.55% Nachrichten
    56600.0h 4.50% Verkaufsshow
    52217.0h 4.15% Krimiserie
    46942.2h 3.73% Werbesendung
    39075.6h 3.10% Dokureihe
    36914.8h 2.93% Dokusoap
    36597.3h 2.91% Regionalmagazin
    33664.8h 2.67% Dokumentation
    29991.7h 2.38% *unknown*
    23737.0h 1.89% Zeichentrickserie
    23387.9h 1.86% Infomercial
    22518.5h 1.79% Animationsserie
    17584.5h 1.40% Comedyserie
    17572.7h 1.40% Morgenmagazin
    16595.0h 1.32% Talkshow
    16326.4h 1.30% Religionsmagazin
    15104.8h 1.20% Magazin
    12480.4h 0.99% E-Sport
    12052.1h 0.96% Sitcom
    11511.5h 0.91% Komödie
    11408.9h 0.91% Wetterbericht
    11216.9h 0.89% Quiz
    11025.0h 0.88% Programmende
    9792.8h  0.78% Realityshow
    9616.9h  0.76% Politikmagazin
    9258.7h  0.74% Wissensmagazin
    8887.1h  0.71% Börsenmagazin
    8361.4h  0.66% Dramaserie
    8351.9h  0.66% Arztserie
    8311.5h  0.66% Wirtschaftsmagazin
