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

**109** channels, **954,211.2** hours playtime between **2023-01-17** and **2024-07-18**


### playtime per genre (top 30)

    62173.9h 6.52% Nachrichten
    44581.4h 4.67% Verkaufsshow
    39084.7h 4.10% Krimiserie
    34050.3h 3.57% Werbesendung
    30017.3h 3.15% Dokureihe
    28887.9h 3.03% Dokusoap
    27774.9h 2.91% Regionalmagazin
    24764.9h 2.60% Dokumentation
    23799.0h 2.49% *unknown*
    17626.8h 1.85% Zeichentrickserie
    17431.9h 1.83% Infomercial
    17067.5h 1.79% Animationsserie
    14192.2h 1.49% Comedyserie
    13445.4h 1.41% Morgenmagazin
    13385.4h 1.40% Magazin
    12944.1h 1.36% Religionsmagazin
    12625.5h 1.32% Talkshow
    9446.0h  0.99% E-Sport
    9003.5h  0.94% Sitcom
    8668.4h  0.91% Programmende
    8550.7h  0.90% Wetterbericht
    8305.9h  0.87% Komödie
    8236.1h  0.86% Quiz
    7957.7h  0.83% Börsenmagazin
    7199.6h  0.75% Politikmagazin
    7091.9h  0.74% Realityshow
    7089.6h  0.74% Wissensmagazin
    6621.8h  0.69% Wirtschaftsmagazin
    6419.1h  0.67% Telenovela
    6223.9h  0.65% Dramaserie
