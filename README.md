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

**101** channels, **778,182.8** hours playtime between **2023-01-17** and **2024-03-28**


### playtime per genre (top 30)

    50662.6h 6.51% Nachrichten
    37393.5h 4.81% Verkaufsshow
    31746.8h 4.08% Krimiserie
    27075.2h 3.48% Werbesendung
    24727.3h 3.18% Dokureihe
    23493.5h 3.02% Dokusoap
    22633.4h 2.91% Regionalmagazin
    20081.3h 2.58% Dokumentation
    19967.5h 2.57% *unknown*
    14331.4h 1.84% Zeichentrickserie
    14160.2h 1.82% Infomercial
    13816.6h 1.78% Animationsserie
    11808.0h 1.52% Comedyserie
    11048.1h 1.42% Morgenmagazin
    10663.4h 1.37% Magazin
    10516.8h 1.35% Religionsmagazin
    10393.8h 1.34% Talkshow
    7662.7h  0.98% E-Sport
    7317.4h  0.94% Programmende
    7272.1h  0.93% Sitcom
    6908.4h  0.89% Wetterbericht
    6907.5h  0.89% Börsenmagazin
    6657.0h  0.86% Quiz
    6540.1h  0.84% Komödie
    5812.4h  0.75% Wissensmagazin
    5666.9h  0.73% Politikmagazin
    5611.7h  0.72% Wirtschaftsmagazin
    5606.8h  0.72% Realityshow
    5574.6h  0.72% Telenovela
    5272.2h  0.68% Musikmagazin
