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

**99** channels, **657,756.4** hours playtime between **2023-01-17** and **2024-01-19**


### playtime per genre (top 30)

    42940.1h 6.53% Nachrichten
    31425.5h 4.78% Verkaufsshow
    26438.7h 4.02% Krimiserie
    22431.1h 3.41% Werbesendung
    21351.5h 3.25% Dokureihe
    19664.0h 2.99% Dokusoap
    18955.3h 2.88% Regionalmagazin
    17051.5h 2.59% Dokumentation
    16409.1h 2.49% *unknown*
    12158.9h 1.85% Zeichentrickserie
    11941.2h 1.82% Infomercial
    11562.0h 1.76% Animationsserie
    9967.9h  1.52% Comedyserie
    9315.1h  1.42% Morgenmagazin
    8891.2h  1.35% Religionsmagazin
    8721.3h  1.33% Magazin
    8689.2h  1.32% Talkshow
    6474.4h  0.98% E-Sport
    6370.8h  0.97% Programmende
    6347.6h  0.97% Sitcom
    5941.6h  0.90% Wetterbericht
    5842.5h  0.89% Börsenmagazin
    5573.6h  0.85% Komödie
    5441.9h  0.83% Quiz
    4948.5h  0.75% Wissensmagazin
    4820.0h  0.73% Wirtschaftsmagazin
    4787.1h  0.73% Realityshow
    4692.0h  0.71% Telenovela
    4662.3h  0.71% Musikmagazin
    4652.0h  0.71% Politikmagazin
