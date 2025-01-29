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

**110** channels, **1,251,595.1** hours playtime between **2023-01-17** and **2025-01-30**


### playtime per genre (top 30)

    82020.2h 6.55% Nachrichten
    56368.1h 4.50% Verkaufsshow
    51928.3h 4.15% Krimiserie
    46619.2h 3.72% Werbesendung
    38867.4h 3.11% Dokureihe
    36739.9h 2.94% Dokusoap
    36423.2h 2.91% Regionalmagazin
    33458.8h 2.67% Dokumentation
    29858.3h 2.39% *unknown*
    23591.0h 1.88% Zeichentrickserie
    23212.6h 1.85% Infomercial
    22384.4h 1.79% Animationsserie
    17510.9h 1.40% Comedyserie
    17486.3h 1.40% Morgenmagazin
    16493.1h 1.32% Talkshow
    16256.5h 1.30% Religionsmagazin
    15080.1h 1.20% Magazin
    12408.1h 0.99% E-Sport
    11992.8h 0.96% Sitcom
    11454.2h 0.92% Komödie
    11344.0h 0.91% Wetterbericht
    11144.7h 0.89% Quiz
    10969.7h 0.88% Programmende
    9731.7h  0.78% Realityshow
    9573.5h  0.76% Politikmagazin
    9219.4h  0.74% Wissensmagazin
    8870.1h  0.71% Börsenmagazin
    8313.0h  0.66% Dramaserie
    8305.7h  0.66% Arztserie
    8271.5h  0.66% Wirtschaftsmagazin
