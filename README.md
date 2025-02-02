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

**110** channels, **1,256,809.5** hours playtime between **2023-01-17** and **2025-02-03**


### playtime per genre (top 30)

    82346.9h 6.55% Nachrichten
    56538.5h 4.50% Verkaufsshow
    52119.3h 4.15% Krimiserie
    46866.7h 3.73% Werbesendung
    39031.7h 3.11% Dokureihe
    36869.3h 2.93% Dokusoap
    36536.0h 2.91% Regionalmagazin
    33625.6h 2.68% Dokumentation
    29956.9h 2.38% *unknown*
    23701.0h 1.89% Zeichentrickserie
    23346.5h 1.86% Infomercial
    22487.0h 1.79% Animationsserie
    17559.8h 1.40% Comedyserie
    17536.8h 1.40% Morgenmagazin
    16581.1h 1.32% Talkshow
    16316.3h 1.30% Religionsmagazin
    15100.4h 1.20% Magazin
    12451.9h 0.99% E-Sport
    12030.0h 0.96% Sitcom
    11515.2h 0.92% Komödie
    11390.5h 0.91% Wetterbericht
    11179.3h 0.89% Quiz
    11011.2h 0.88% Programmende
    9775.4h  0.78% Realityshow
    9591.1h  0.76% Politikmagazin
    9253.8h  0.74% Wissensmagazin
    8879.2h  0.71% Börsenmagazin
    8350.0h  0.66% Dramaserie
    8338.7h  0.66% Arztserie
    8295.9h  0.66% Wirtschaftsmagazin
