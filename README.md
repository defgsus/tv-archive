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

**97** channels, **566,849.2** hours playtime between **2023-01-17** and **2023-11-28**


### playtime per genre (top 30)

    37275.2h 6.58% Nachrichten
    27139.9h 4.79% Verkaufsshow
    22873.8h 4.04% Krimiserie
    19240.1h 3.39% Werbesendung
    18462.7h 3.26% Dokureihe
    17123.2h 3.02% Dokusoap
    16384.8h 2.89% Regionalmagazin
    14475.0h 2.55% Dokumentation
    13814.6h 2.44% *unknown*
    10492.5h 1.85% Zeichentrickserie
    10327.4h 1.82% Infomercial
    10087.9h 1.78% Animationsserie
    8827.2h  1.56% Comedyserie
    8063.1h  1.42% Morgenmagazin
    7660.0h  1.35% Religionsmagazin
    7581.2h  1.34% Talkshow
    7243.2h  1.28% Magazin
    5678.1h  1.00% Programmende
    5555.4h  0.98% E-Sport
    5446.2h  0.96% Sitcom
    5197.2h  0.92% Wetterbericht
    5138.2h  0.91% Börsenmagazin
    4722.9h  0.83% Quiz
    4391.3h  0.77% Komödie
    4310.8h  0.76% Wissensmagazin
    4249.9h  0.75% Wirtschaftsmagazin
    4155.5h  0.73% Musikmagazin
    4101.0h  0.72% Telenovela
    3986.7h  0.70% Politikmagazin
    3981.0h  0.70% Realityshow
