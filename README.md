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

**110** channels, **1,272,416.1** hours playtime between **2023-01-17** and **2025-02-13**


### playtime per genre (top 30)

    83506.0h 6.56% Nachrichten
    57065.1h 4.48% Verkaufsshow
    52868.6h 4.15% Krimiserie
    47531.4h 3.74% Werbesendung
    39461.5h 3.10% Dokureihe
    37339.2h 2.93% Dokusoap
    37028.1h 2.91% Regionalmagazin
    34123.4h 2.68% Dokumentation
    30243.4h 2.38% *unknown*
    24020.0h 1.89% Zeichentrickserie
    23729.7h 1.86% Infomercial
    22773.3h 1.79% Animationsserie
    17795.1h 1.40% Morgenmagazin
    17724.9h 1.39% Comedyserie
    16793.0h 1.32% Talkshow
    16453.3h 1.29% Religionsmagazin
    15155.6h 1.19% Magazin
    12618.0h 0.99% E-Sport
    12191.1h 0.96% Sitcom
    11614.8h 0.91% Komödie
    11549.0h 0.91% Wetterbericht
    11353.5h 0.89% Quiz
    11135.8h 0.88% Programmende
    9918.6h  0.78% Realityshow
    9745.4h  0.77% Politikmagazin
    9331.8h  0.73% Wissensmagazin
    8938.4h  0.70% Börsenmagazin
    8475.0h  0.67% Arztserie
    8472.9h  0.67% Dramaserie
    8413.5h  0.66% Wirtschaftsmagazin
