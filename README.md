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

**97** channels, **563,234.2** hours playtime between **2023-01-17** and **2023-11-26**


### playtime per genre (top 30)

    37055.6h 6.58% Nachrichten
    26971.9h 4.79% Verkaufsshow
    22742.0h 4.04% Krimiserie
    19106.6h 3.39% Werbesendung
    18364.6h 3.26% Dokureihe
    17008.0h 3.02% Dokusoap
    16286.1h 2.89% Regionalmagazin
    14354.1h 2.55% Dokumentation
    13706.1h 2.43% *unknown*
    10429.2h 1.85% Zeichentrickserie
    10265.1h 1.82% Infomercial
    10033.4h 1.78% Animationsserie
    8788.8h  1.56% Comedyserie
    8021.7h  1.42% Morgenmagazin
    7601.1h  1.35% Religionsmagazin
    7531.2h  1.34% Talkshow
    7198.4h  1.28% Magazin
    5650.4h  1.00% Programmende
    5515.6h  0.98% E-Sport
    5412.1h  0.96% Sitcom
    5167.3h  0.92% Wetterbericht
    5107.9h  0.91% Börsenmagazin
    4695.1h  0.83% Quiz
    4383.2h  0.78% Komödie
    4277.3h  0.76% Wissensmagazin
    4224.5h  0.75% Wirtschaftsmagazin
    4133.9h  0.73% Musikmagazin
    4080.5h  0.72% Telenovela
    3959.0h  0.70% Politikmagazin
    3948.2h  0.70% Realityshow
