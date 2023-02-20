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

**96** channels, **64,711.3** hours playtime between **2023-01-17** and **2023-02-21**


### playtime per genre (top 30)

    4555.0h 7.04% Nachrichten
    3303.9h 5.11% Verkaufsshow
    2725.1h 4.21% Krimiserie
    2206.8h 3.41% Werbesendung
    2184.3h 3.38% Dokusoap
    1901.1h 2.94% Dokureihe
    1862.6h 2.88% Regionalmagazin
    1594.7h 2.46% *unknown*
    1588.3h 2.45% Dokumentation
    1218.6h 1.88% Zeichentrickserie
    1192.6h 1.84% Animationsserie
    1189.0h 1.84% Infomercial
    1065.5h 1.65% Comedyserie
    907.1h  1.40% Morgenmagazin
    864.3h  1.34% Programmende
    852.7h  1.32% Religionsmagazin
    848.0h  1.31% Talkshow
    706.2h  1.09% Magazin
    667.6h  1.03% E-Sport
    604.1h  0.93% Sitcom
    568.5h  0.88% Wetterbericht
    558.1h  0.86% Börsenmagazin
    529.8h  0.82% Wirtschaftsmagazin
    497.4h  0.77% Wissensmagazin
    486.4h  0.75% Quiz
    473.2h  0.73% Musikmagazin
    466.0h  0.72% Dramaserie
    452.6h  0.70% Gesundheitsmagazin
    436.6h  0.67% Telenovela
    427.2h  0.66% Sportmagazin
