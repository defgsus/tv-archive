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

**96** channels, **70,188.4** hours playtime between **2023-01-17** and **2023-02-24**


### playtime per genre (top 30)

    4985.1h 7.10% Nachrichten
    3576.3h 5.10% Verkaufsshow
    2984.7h 4.25% Krimiserie
    2387.1h 3.40% Werbesendung
    2379.2h 3.39% Dokusoap
    2073.4h 2.95% Regionalmagazin
    2058.6h 2.93% Dokureihe
    1716.0h 2.44% *unknown*
    1704.2h 2.43% Dokumentation
    1311.5h 1.87% Animationsserie
    1308.3h 1.86% Zeichentrickserie
    1286.9h 1.83% Infomercial
    1161.1h 1.65% Comedyserie
    1011.3h 1.44% Morgenmagazin
    948.2h  1.35% Programmende
    917.0h  1.31% Talkshow
    914.6h  1.30% Religionsmagazin
    753.7h  1.07% Magazin
    725.0h  1.03% E-Sport
    665.8h  0.95% Sitcom
    619.9h  0.88% Wetterbericht
    614.3h  0.88% Börsenmagazin
    578.9h  0.82% Wirtschaftsmagazin
    551.6h  0.79% Wissensmagazin
    527.5h  0.75% Quiz
    516.3h  0.74% Dramaserie
    515.6h  0.73% Musikmagazin
    498.8h  0.71% Gesundheitsmagazin
    489.9h  0.70% Telenovela
    457.9h  0.65% Gerichtsshow
