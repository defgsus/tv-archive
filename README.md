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

**109** channels, **950,581.7** hours playtime between **2023-01-17** and **2024-07-16**


### playtime per genre (top 30)

    61914.8h 6.51% Nachrichten
    44422.2h 4.67% Verkaufsshow
    38898.3h 4.09% Krimiserie
    33902.0h 3.57% Werbesendung
    29904.6h 3.15% Dokureihe
    28771.4h 3.03% Dokusoap
    27633.5h 2.91% Regionalmagazin
    24653.5h 2.59% Dokumentation
    23732.9h 2.50% *unknown*
    17552.3h 1.85% Zeichentrickserie
    17363.5h 1.83% Infomercial
    17004.3h 1.79% Animationsserie
    14144.1h 1.49% Comedyserie
    13378.1h 1.41% Magazin
    13376.3h 1.41% Morgenmagazin
    12890.4h 1.36% Religionsmagazin
    12578.0h 1.32% Talkshow
    9414.4h  0.99% E-Sport
    8951.6h  0.94% Sitcom
    8641.4h  0.91% Programmende
    8515.4h  0.90% Wetterbericht
    8285.2h  0.87% Komödie
    8214.5h  0.86% Quiz
    7939.8h  0.84% Börsenmagazin
    7158.4h  0.75% Politikmagazin
    7066.0h  0.74% Realityshow
    7061.6h  0.74% Wissensmagazin
    6599.0h  0.69% Wirtschaftsmagazin
    6405.6h  0.67% Telenovela
    6185.1h  0.65% Dramaserie
