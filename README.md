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

**99** channels, **709,265.8** hours playtime between **2023-01-17** and **2024-02-17**


### playtime per genre (top 30)

    46235.5h 6.52% Nachrichten
    34060.9h 4.80% Verkaufsshow
    28729.8h 4.05% Krimiserie
    24375.5h 3.44% Werbesendung
    22785.4h 3.21% Dokureihe
    21381.7h 3.01% Dokusoap
    20550.6h 2.90% Regionalmagazin
    18274.3h 2.58% Dokumentation
    17950.9h 2.53% *unknown*
    13154.6h 1.85% Zeichentrickserie
    12891.4h 1.82% Infomercial
    12468.9h 1.76% Animationsserie
    10753.3h 1.52% Comedyserie
    10068.3h 1.42% Morgenmagazin
    9585.3h  1.35% Religionsmagazin
    9479.0h  1.34% Magazin
    9392.6h  1.32% Talkshow
    6989.9h  0.99% E-Sport
    6778.5h  0.96% Programmende
    6744.8h  0.95% Sitcom
    6329.8h  0.89% Börsenmagazin
    6315.3h  0.89% Wetterbericht
    6000.0h  0.85% Komödie
    5923.0h  0.84% Quiz
    5321.1h  0.75% Wissensmagazin
    5204.5h  0.73% Realityshow
    5166.6h  0.73% Wirtschaftsmagazin
    5085.9h  0.72% Politikmagazin
    5066.2h  0.71% Telenovela
    4918.8h  0.69% Musikmagazin
