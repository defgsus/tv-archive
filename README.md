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

**109** channels, **945,187.2** hours playtime between **2023-01-17** and **2024-07-13**


### playtime per genre (top 30)

    61624.7h 6.52% Nachrichten
    44203.1h 4.68% Verkaufsshow
    38691.2h 4.09% Krimiserie
    33671.2h 3.56% Werbesendung
    29704.5h 3.14% Dokureihe
    28626.7h 3.03% Dokusoap
    27508.1h 2.91% Regionalmagazin
    24524.8h 2.59% Dokumentation
    23581.1h 2.49% *unknown*
    17434.5h 1.84% Zeichentrickserie
    17259.1h 1.83% Infomercial
    16907.1h 1.79% Animationsserie
    14082.2h 1.49% Comedyserie
    13362.8h 1.41% Magazin
    13333.7h 1.41% Morgenmagazin
    12809.0h 1.36% Religionsmagazin
    12517.0h 1.32% Talkshow
    9367.3h  0.99% E-Sport
    8901.6h  0.94% Sitcom
    8600.0h  0.91% Programmende
    8463.1h  0.90% Wetterbericht
    8192.8h  0.87% Komödie
    8171.9h  0.86% Quiz
    7931.3h  0.84% Börsenmagazin
    7129.1h  0.75% Politikmagazin
    7039.3h  0.74% Realityshow
    7020.3h  0.74% Wissensmagazin
    6582.9h  0.70% Wirtschaftsmagazin
    6397.7h  0.68% Telenovela
    6160.6h  0.65% Dramaserie
