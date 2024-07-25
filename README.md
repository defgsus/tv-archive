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

**109** channels, **966,783.8** hours playtime between **2023-01-17** and **2024-07-26**


### playtime per genre (top 30)

    62992.3h 6.52% Nachrichten
    45125.8h 4.67% Verkaufsshow
    39649.2h 4.10% Krimiserie
    34589.7h 3.58% Werbesendung
    30409.1h 3.15% Dokureihe
    29282.4h 3.03% Dokusoap
    28159.8h 2.91% Regionalmagazin
    25139.9h 2.60% Dokumentation
    24025.7h 2.49% *unknown*
    17899.5h 1.85% Zeichentrickserie
    17678.0h 1.83% Infomercial
    17296.2h 1.79% Animationsserie
    14358.8h 1.49% Comedyserie
    13619.4h 1.41% Morgenmagazin
    13425.0h 1.39% Magazin
    13116.0h 1.36% Religionsmagazin
    12761.8h 1.32% Talkshow
    9580.8h  0.99% E-Sport
    9135.8h  0.94% Sitcom
    8759.1h  0.91% Programmende
    8682.8h  0.90% Wetterbericht
    8424.5h  0.87% Komödie
    8344.9h  0.86% Quiz
    8002.3h  0.83% Börsenmagazin
    7291.0h  0.75% Politikmagazin
    7188.6h  0.74% Wissensmagazin
    7177.1h  0.74% Realityshow
    6689.4h  0.69% Wirtschaftsmagazin
    6460.6h  0.67% Telenovela
    6309.5h  0.65% Dramaserie
