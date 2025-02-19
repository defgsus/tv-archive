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

**195** channels, **2,004,302*** programs, **1,285,147.8** hours playtime between **2023-01-17** and **2025-02-20**


### playtime per genre (top 30)

    84,186.3h 6.55% Nachrichten
    57,241.8h 4.45% Verkaufsshow
    53,077.6h 4.13% Krimiserie
    47,732.5h 3.71% Werbesendung
    39,629.6h 3.08% Dokureihe
    37,480.7h 2.92% Dokusoap
    37,137.2h 2.89% Regionalmagazin
    35,242.7h 2.74% Dokumentation
    30,355.0h 2.36% *unknown*
    24,119.8h 1.88% Zeichentrickserie
    23,841.5h 1.86% Infomercial
    22,879.0h 1.78% Animationsserie
    17,855.4h 1.39% Morgenmagazin
    17,772.0h 1.38% Comedyserie
    16,886.2h 1.31% Talkshow
    16,506.6h 1.28% Religionsmagazin
    16,139.9h 1.26% Magazin
    12,664.6h 0.99% E-Sport
    12,223.4h 0.95% Sitcom
    11,657.4h 0.91% Komödie
    11,600.5h 0.90% Wetterbericht
    11,389.4h 0.89% Quiz
    11,169.9h 0.87% Programmende
    9,951.3h  0.77% Realityshow
    9,780.6h  0.76% Politikmagazin
    9,357.3h  0.73% Wissensmagazin
    8,946.0h  0.70% Börsenmagazin
    8,507.0h  0.66% Arztserie
    8,496.2h  0.66% Dramaserie
    8,435.2h  0.66% Wirtschaftsmagazin
