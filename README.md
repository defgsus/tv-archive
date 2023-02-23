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

**96** channels, **70,190.7** hours playtime between **2023-01-17** and **2023-02-24**


### playtime per genre (top 30)

    4984.0h 7.10% Nachrichten
    3576.0h 5.09% Verkaufsshow
    2984.3h 4.25% Krimiserie
    2387.1h 3.40% Werbesendung
    2379.2h 3.39% Dokusoap
    2073.4h 2.95% Regionalmagazin
    2058.5h 2.93% Dokureihe
    1719.0h 2.45% *unknown*
    1702.8h 2.43% Dokumentation
    1310.9h 1.87% Animationsserie
    1308.3h 1.86% Zeichentrickserie
    1286.9h 1.83% Infomercial
    1158.3h 1.65% Comedyserie
    1011.3h 1.44% Morgenmagazin
    948.1h  1.35% Programmende
    915.9h  1.30% Talkshow
    914.6h  1.30% Religionsmagazin
    753.5h  1.07% Magazin
    725.1h  1.03% E-Sport
    666.1h  0.95% Sitcom
    619.7h  0.88% Wetterbericht
    614.3h  0.88% Börsenmagazin
    579.3h  0.83% Wirtschaftsmagazin
    551.0h  0.79% Wissensmagazin
    527.5h  0.75% Quiz
    515.6h  0.73% Dramaserie
    513.1h  0.73% Musikmagazin
    498.8h  0.71% Gesundheitsmagazin
    489.2h  0.70% Telenovela
    458.3h  0.65% Gerichtsshow
