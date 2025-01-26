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

**110** channels, **1,246,451.1** hours playtime between **2023-01-17** and **2025-01-27**


### playtime per genre (top 30)

    81613.1h 6.55% Nachrichten
    56230.8h 4.51% Verkaufsshow
    51675.2h 4.15% Krimiserie
    46388.0h 3.72% Werbesendung
    38742.0h 3.11% Dokureihe
    36594.4h 2.94% Dokusoap
    36247.4h 2.91% Regionalmagazin
    33305.8h 2.67% Dokumentation
    29746.7h 2.39% *unknown*
    23485.4h 1.88% Zeichentrickserie
    23095.4h 1.85% Infomercial
    22290.3h 1.79% Animationsserie
    17449.0h 1.40% Comedyserie
    17388.3h 1.40% Morgenmagazin
    16443.2h 1.32% Talkshow
    16222.6h 1.30% Religionsmagazin
    15045.7h 1.21% Magazin
    12349.6h 0.99% E-Sport
    11930.3h 0.96% Sitcom
    11416.0h 0.92% Komödie
    11291.8h 0.91% Wetterbericht
    11070.7h 0.89% Quiz
    10928.3h 0.88% Programmende
    9671.9h  0.78% Realityshow
    9507.9h  0.76% Politikmagazin
    9198.1h  0.74% Wissensmagazin
    8844.6h  0.71% Börsenmagazin
    8268.1h  0.66% Dramaserie
    8254.5h  0.66% Arztserie
    8230.9h  0.66% Wirtschaftsmagazin
