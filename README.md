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

**110** channels, **1,263,731.7** hours playtime between **2023-01-17** and **2025-02-07**


### playtime per genre (top 30)

    82901.7h 6.56% Nachrichten
    56770.8h 4.49% Verkaufsshow
    52487.7h 4.15% Krimiserie
    47162.2h 3.73% Werbesendung
    39230.9h 3.10% Dokureihe
    37080.7h 2.93% Dokusoap
    36785.2h 2.91% Regionalmagazin
    33847.3h 2.68% Dokumentation
    30059.2h 2.38% *unknown*
    23846.5h 1.89% Zeichentrickserie
    23511.6h 1.86% Infomercial
    22615.3h 1.79% Animationsserie
    17675.0h 1.40% Morgenmagazin
    17632.0h 1.40% Comedyserie
    16666.0h 1.32% Talkshow
    16364.8h 1.29% Religionsmagazin
    15122.7h 1.20% Magazin
    12519.7h 0.99% E-Sport
    12111.2h 0.96% Sitcom
    11532.3h 0.91% Komödie
    11462.9h 0.91% Wetterbericht
    11272.6h 0.89% Quiz
    11066.5h 0.88% Programmende
    9839.4h  0.78% Realityshow
    9677.5h  0.77% Politikmagazin
    9284.4h  0.73% Wissensmagazin
    8913.7h  0.71% Börsenmagazin
    8412.7h  0.67% Dramaserie
    8403.3h  0.66% Arztserie
    8356.8h  0.66% Wirtschaftsmagazin
