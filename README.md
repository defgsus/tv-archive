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

**110** channels, **1,274,144.5** hours playtime between **2023-01-17** and **2025-02-15**


### playtime per genre (top 30)

    83633.4h 6.56% Nachrichten
    57136.1h 4.48% Verkaufsshow
    52959.2h 4.16% Krimiserie
    47597.7h 3.74% Werbesendung
    39528.5h 3.10% Dokureihe
    37375.2h 2.93% Dokusoap
    37084.5h 2.91% Regionalmagazin
    34169.3h 2.68% Dokumentation
    30272.5h 2.38% *unknown*
    24057.0h 1.89% Zeichentrickserie
    23772.8h 1.87% Infomercial
    22807.5h 1.79% Animationsserie
    17828.5h 1.40% Morgenmagazin
    17741.3h 1.39% Comedyserie
    16820.2h 1.32% Talkshow
    16466.5h 1.29% Religionsmagazin
    15162.2h 1.19% Magazin
    12626.3h 0.99% E-Sport
    12206.3h 0.96% Sitcom
    11625.4h 0.91% Komödie
    11567.1h 0.91% Wetterbericht
    11369.8h 0.89% Quiz
    11148.7h 0.87% Programmende
    9932.3h  0.78% Realityshow
    9762.9h  0.77% Politikmagazin
    9339.8h  0.73% Wissensmagazin
    8946.2h  0.70% Börsenmagazin
    8490.5h  0.67% Arztserie
    8484.8h  0.67% Dramaserie
    8429.3h  0.66% Wirtschaftsmagazin
