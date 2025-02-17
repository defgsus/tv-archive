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

**110** channels, **1,277,449.9** hours playtime between **2023-01-17** and **2025-02-18**


### playtime per genre (top 30)

    83827.9h 6.56% Nachrichten
    57241.8h 4.48% Verkaufsshow
    53081.6h 4.16% Krimiserie
    47732.5h 3.74% Werbesendung
    39633.3h 3.10% Dokureihe
    37482.9h 2.93% Dokusoap
    37142.4h 2.91% Regionalmagazin
    34290.3h 2.68% Dokumentation
    30355.0h 2.38% *unknown*
    24119.8h 1.89% Zeichentrickserie
    23841.5h 1.87% Infomercial
    22879.0h 1.79% Animationsserie
    17855.4h 1.40% Morgenmagazin
    17772.0h 1.39% Comedyserie
    16887.2h 1.32% Talkshow
    16506.6h 1.29% Religionsmagazin
    15183.8h 1.19% Magazin
    12664.6h 0.99% E-Sport
    12223.4h 0.96% Sitcom
    11657.4h 0.91% Komödie
    11600.5h 0.91% Wetterbericht
    11389.4h 0.89% Quiz
    11170.5h 0.87% Programmende
    9951.3h  0.78% Realityshow
    9780.6h  0.77% Politikmagazin
    9357.3h  0.73% Wissensmagazin
    8946.0h  0.70% Börsenmagazin
    8510.0h  0.67% Arztserie
    8496.2h  0.67% Dramaserie
    8435.2h  0.66% Wirtschaftsmagazin
