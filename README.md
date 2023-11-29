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

**97** channels, **570,423.0** hours playtime between **2023-01-17** and **2023-11-30**


### playtime per genre (top 30)

    37533.7h 6.58% Nachrichten
    27323.8h 4.79% Verkaufsshow
    23027.0h 4.04% Krimiserie
    19366.2h 3.40% Werbesendung
    18571.5h 3.26% Dokureihe
    17218.8h 3.02% Dokusoap
    16515.9h 2.90% Regionalmagazin
    14533.4h 2.55% Dokumentation
    13910.3h 2.44% *unknown*
    10550.5h 1.85% Zeichentrickserie
    10393.4h 1.82% Infomercial
    10149.1h 1.78% Animationsserie
    8878.0h  1.56% Comedyserie
    8132.6h  1.43% Morgenmagazin
    7701.8h  1.35% Religionsmagazin
    7635.8h  1.34% Talkshow
    7301.3h  1.28% Magazin
    5706.6h  1.00% Programmende
    5581.7h  0.98% E-Sport
    5501.2h  0.96% Sitcom
    5228.6h  0.92% Wetterbericht
    5180.3h  0.91% Börsenmagazin
    4753.2h  0.83% Quiz
    4407.5h  0.77% Komödie
    4344.7h  0.76% Wissensmagazin
    4279.9h  0.75% Wirtschaftsmagazin
    4171.9h  0.73% Musikmagazin
    4141.7h  0.73% Telenovela
    4034.9h  0.71% Politikmagazin
    4021.1h  0.70% Realityshow
