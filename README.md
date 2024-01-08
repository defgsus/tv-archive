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

**97** channels, **640,019.1** hours playtime between **2023-01-17** and **2024-01-09**


### playtime per genre (top 30)

    41744.0h 6.52% Nachrichten
    30590.8h 4.78% Verkaufsshow
    25610.0h 4.00% Krimiserie
    21767.3h 3.40% Werbesendung
    20784.0h 3.25% Dokureihe
    19134.6h 2.99% Dokusoap
    18364.5h 2.87% Regionalmagazin
    16672.6h 2.61% Dokumentation
    15925.1h 2.49% *unknown*
    11814.0h 1.85% Zeichentrickserie
    11602.2h 1.81% Infomercial
    11253.0h 1.76% Animationsserie
    9707.6h  1.52% Comedyserie
    9033.1h  1.41% Morgenmagazin
    8665.3h  1.35% Religionsmagazin
    8437.3h  1.32% Talkshow
    8389.1h  1.31% Magazin
    6310.7h  0.99% E-Sport
    6240.6h  0.98% Programmende
    6197.3h  0.97% Sitcom
    5815.8h  0.91% Wetterbericht
    5706.2h  0.89% Börsenmagazin
    5442.0h  0.85% Komödie
    5267.3h  0.82% Quiz
    4817.2h  0.75% Wissensmagazin
    4693.5h  0.73% Wirtschaftsmagazin
    4645.2h  0.73% Realityshow
    4574.4h  0.71% Musikmagazin
    4543.2h  0.71% Telenovela
    4493.1h  0.70% Politikmagazin
