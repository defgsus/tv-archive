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

**110** channels, **1,239,532.0** hours playtime between **2023-01-17** and **2025-01-22**


### playtime per genre (top 30)

    81137.6h 6.55% Nachrichten
    55968.1h 4.52% Verkaufsshow
    51407.2h 4.15% Krimiserie
    46094.1h 3.72% Werbesendung
    38533.5h 3.11% Dokureihe
    36409.1h 2.94% Dokusoap
    36072.4h 2.91% Regionalmagazin
    33089.2h 2.67% Dokumentation
    29580.2h 2.39% *unknown*
    23346.6h 1.88% Zeichentrickserie
    22958.5h 1.85% Infomercial
    22159.6h 1.79% Animationsserie
    17369.8h 1.40% Comedyserie
    17304.2h 1.40% Morgenmagazin
    16344.8h 1.32% Talkshow
    16148.1h 1.30% Religionsmagazin
    15007.2h 1.21% Magazin
    12283.1h 0.99% E-Sport
    11869.7h 0.96% Sitcom
    11339.9h 0.91% Komödie
    11229.0h 0.91% Wetterbericht
    11014.2h 0.89% Quiz
    10866.4h 0.88% Programmende
    9610.3h  0.78% Realityshow
    9458.9h  0.76% Politikmagazin
    9156.6h  0.74% Wissensmagazin
    8826.6h  0.71% Börsenmagazin
    8223.9h  0.66% Dramaserie
    8209.0h  0.66% Arztserie
    8187.9h  0.66% Wirtschaftsmagazin
