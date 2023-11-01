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

**97** channels, **520,108.2** hours playtime between **2023-01-17** and **2023-11-02**


### playtime per genre (top 30)

    34247.3h 6.58% Nachrichten
    24835.5h 4.78% Verkaufsshow
    20870.7h 4.01% Krimiserie
    17615.7h 3.39% Werbesendung
    17119.4h 3.29% Dokureihe
    15835.9h 3.04% Dokusoap
    15008.1h 2.89% Regionalmagazin
    13245.0h 2.55% Dokumentation
    12536.7h 2.41% *unknown*
    9689.2h  1.86% Zeichentrickserie
    9469.8h  1.82% Infomercial
    9299.6h  1.79% Animationsserie
    8220.4h  1.58% Comedyserie
    7389.4h  1.42% Morgenmagazin
    7007.8h  1.35% Religionsmagazin
    6917.4h  1.33% Talkshow
    6559.3h  1.26% Magazin
    5319.1h  1.02% Programmende
    5099.8h  0.98% E-Sport
    4975.2h  0.96% Sitcom
    4814.8h  0.93% Wetterbericht
    4703.8h  0.90% Börsenmagazin
    4352.1h  0.84% Quiz
    4062.3h  0.78% Komödie
    3932.1h  0.76% Wissensmagazin
    3921.3h  0.75% Wirtschaftsmagazin
    3890.7h  0.75% Musikmagazin
    3737.8h  0.72% Telenovela
    3591.1h  0.69% Politikmagazin
    3485.9h  0.67% Realityshow
