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

**110** channels, **1,244,735.2** hours playtime between **2023-01-17** and **2025-01-26**


### playtime per genre (top 30)

    81516.2h 6.55% Nachrichten
    56163.0h 4.51% Verkaufsshow
    51617.9h 4.15% Krimiserie
    46316.1h 3.72% Werbesendung
    38672.6h 3.11% Dokureihe
    36552.3h 2.94% Dokusoap
    36214.4h 2.91% Regionalmagazin
    33251.5h 2.67% Dokumentation
    29681.9h 2.38% *unknown*
    23452.6h 1.88% Zeichentrickserie
    23061.1h 1.85% Infomercial
    22258.8h 1.79% Animationsserie
    17436.7h 1.40% Comedyserie
    17379.5h 1.40% Morgenmagazin
    16409.5h 1.32% Talkshow
    16189.4h 1.30% Religionsmagazin
    15033.8h 1.21% Magazin
    12339.7h 0.99% E-Sport
    11921.0h 0.96% Sitcom
    11398.0h 0.92% Komödie
    11277.4h 0.91% Wetterbericht
    11066.5h 0.89% Quiz
    10907.8h 0.88% Programmende
    9661.4h  0.78% Realityshow
    9493.4h  0.76% Politikmagazin
    9182.9h  0.74% Wissensmagazin
    8844.6h  0.71% Börsenmagazin
    8264.6h  0.66% Dramaserie
    8247.9h  0.66% Arztserie
    8221.0h  0.66% Wirtschaftsmagazin
