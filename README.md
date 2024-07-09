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

**109** channels, **941,518.8** hours playtime between **2023-01-17** and **2024-07-10**


### playtime per genre (top 30)

    61383.0h 6.52% Nachrichten
    44053.5h 4.68% Verkaufsshow
    38515.2h 4.09% Krimiserie
    33512.3h 3.56% Werbesendung
    29628.7h 3.15% Dokureihe
    28499.5h 3.03% Dokusoap
    27381.5h 2.91% Regionalmagazin
    24418.6h 2.59% Dokumentation
    23500.5h 2.50% *unknown*
    17358.6h 1.84% Zeichentrickserie
    17187.0h 1.83% Infomercial
    16836.9h 1.79% Animationsserie
    14030.9h 1.49% Comedyserie
    13347.8h 1.42% Magazin
    13257.7h 1.41% Morgenmagazin
    12767.6h 1.36% Religionsmagazin
    12476.1h 1.33% Talkshow
    9321.7h  0.99% E-Sport
    8855.6h  0.94% Sitcom
    8565.1h  0.91% Programmende
    8426.2h  0.89% Wetterbericht
    8165.6h  0.87% Komödie
    8143.9h  0.86% Quiz
    7913.3h  0.84% Börsenmagazin
    7100.4h  0.75% Politikmagazin
    7008.9h  0.74% Realityshow
    6996.4h  0.74% Wissensmagazin
    6556.1h  0.70% Wirtschaftsmagazin
    6384.2h  0.68% Telenovela
    6135.1h  0.65% Musikmagazin
