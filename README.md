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

**110** channels, **1,249,829.4** hours playtime between **2023-01-17** and **2025-01-29**


### playtime per genre (top 30)

    81886.1h 6.55% Nachrichten
    56307.2h 4.51% Verkaufsshow
    51851.5h 4.15% Krimiserie
    46536.4h 3.72% Werbesendung
    38828.3h 3.11% Dokureihe
    36685.3h 2.94% Dokusoap
    36347.3h 2.91% Regionalmagazin
    33418.9h 2.67% Dokumentation
    29808.9h 2.39% *unknown*
    23558.6h 1.88% Zeichentrickserie
    23159.5h 1.85% Infomercial
    22352.2h 1.79% Animationsserie
    17490.4h 1.40% Comedyserie
    17452.3h 1.40% Morgenmagazin
    16474.8h 1.32% Talkshow
    16246.8h 1.30% Religionsmagazin
    15067.1h 1.21% Magazin
    12403.5h 0.99% E-Sport
    11968.5h 0.96% Sitcom
    11449.5h 0.92% Komödie
    11326.5h 0.91% Wetterbericht
    11123.4h 0.89% Quiz
    10956.6h 0.88% Programmende
    9712.6h  0.78% Realityshow
    9550.8h  0.76% Politikmagazin
    9210.9h  0.74% Wissensmagazin
    8862.2h  0.71% Börsenmagazin
    8301.5h  0.66% Dramaserie
    8288.4h  0.66% Arztserie
    8255.8h  0.66% Wirtschaftsmagazin
