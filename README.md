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

**98** channels, **648,835.3** hours playtime between **2023-01-17** and **2024-01-14**


### playtime per genre (top 30)

    42333.0h 6.52% Nachrichten
    30995.1h 4.78% Verkaufsshow
    26034.2h 4.01% Krimiserie
    22106.2h 3.41% Werbesendung
    21070.7h 3.25% Dokureihe
    19383.5h 2.99% Dokusoap
    18653.1h 2.87% Regionalmagazin
    16856.1h 2.60% Dokumentation
    16158.5h 2.49% *unknown*
    11981.2h 1.85% Zeichentrickserie
    11771.8h 1.81% Infomercial
    11408.8h 1.76% Animationsserie
    9834.3h  1.52% Comedyserie
    9175.5h  1.41% Morgenmagazin
    8770.5h  1.35% Religionsmagazin
    8564.7h  1.32% Talkshow
    8559.9h  1.32% Magazin
    6374.9h  0.98% E-Sport
    6301.4h  0.97% Programmende
    6265.0h  0.97% Sitcom
    5879.8h  0.91% Wetterbericht
    5774.9h  0.89% Börsenmagazin
    5512.9h  0.85% Komödie
    5350.9h  0.82% Quiz
    4884.1h  0.75% Wissensmagazin
    4757.2h  0.73% Wirtschaftsmagazin
    4711.5h  0.73% Realityshow
    4618.1h  0.71% Telenovela
    4614.2h  0.71% Musikmagazin
    4561.1h  0.70% Politikmagazin
