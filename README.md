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

**97** channels, **595,539.8** hours playtime between **2023-01-17** and **2023-12-15**


### playtime per genre (top 30)

    39144.2h 6.57% Nachrichten
    28579.5h 4.80% Verkaufsshow
    24085.1h 4.04% Krimiserie
    20244.9h 3.40% Werbesendung
    19356.6h 3.25% Dokureihe
    17916.1h 3.01% Dokusoap
    17249.7h 2.90% Regionalmagazin
    15240.3h 2.56% Dokumentation
    14570.6h 2.45% *unknown*
    10996.2h 1.85% Zeichentrickserie
    10855.2h 1.82% Infomercial
    10562.6h 1.77% Animationsserie
    9157.0h  1.54% Comedyserie
    8506.2h  1.43% Morgenmagazin
    8065.6h  1.35% Religionsmagazin
    7976.3h  1.34% Talkshow
    7684.6h  1.29% Magazin
    5893.4h  0.99% Programmende
    5848.2h  0.98% E-Sport
    5772.5h  0.97% Sitcom
    5450.8h  0.92% Wetterbericht
    5400.0h  0.91% Börsenmagazin
    4947.9h  0.83% Quiz
    4617.2h  0.78% Komödie
    4539.0h  0.76% Wissensmagazin
    4454.4h  0.75% Wirtschaftsmagazin
    4331.8h  0.73% Telenovela
    4314.7h  0.72% Musikmagazin
    4294.4h  0.72% Realityshow
    4243.7h  0.71% Politikmagazin
