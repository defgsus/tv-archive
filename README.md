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

**110** channels, **1,274,154.0** hours playtime between **2023-01-17** and **2025-02-14**


### playtime per genre (top 30)

    83641.9h 6.56% Nachrichten
    57125.7h 4.48% Verkaufsshow
    52974.0h 4.16% Krimiserie
    47605.3h 3.74% Werbesendung
    39525.9h 3.10% Dokureihe
    37388.2h 2.93% Dokusoap
    37086.2h 2.91% Regionalmagazin
    34173.7h 2.68% Dokumentation
    30272.6h 2.38% *unknown*
    24057.6h 1.89% Zeichentrickserie
    23774.0h 1.87% Infomercial
    22806.4h 1.79% Animationsserie
    17828.5h 1.40% Morgenmagazin
    17740.3h 1.39% Comedyserie
    16820.6h 1.32% Talkshow
    16465.2h 1.29% Religionsmagazin
    15164.2h 1.19% Magazin
    12633.4h 0.99% E-Sport
    12207.8h 0.96% Sitcom
    11627.9h 0.91% Komödie
    11567.3h 0.91% Wetterbericht
    11378.8h 0.89% Quiz
    11149.4h 0.88% Programmende
    9930.3h  0.78% Realityshow
    9766.6h  0.77% Politikmagazin
    9340.9h  0.73% Wissensmagazin
    8946.5h  0.70% Börsenmagazin
    8489.2h  0.67% Arztserie
    8488.5h  0.67% Dramaserie
    8430.5h  0.66% Wirtschaftsmagazin
