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

**101** channels, **779,938.3** hours playtime between **2023-01-17** and **2024-03-29**


### playtime per genre (top 30)

    50793.3h 6.51% Nachrichten
    37471.2h 4.80% Verkaufsshow
    31846.3h 4.08% Krimiserie
    27141.1h 3.48% Werbesendung
    24774.8h 3.18% Dokureihe
    23544.6h 3.02% Dokusoap
    22696.1h 2.91% Regionalmagazin
    20129.9h 2.58% Dokumentation
    20013.9h 2.57% *unknown*
    14361.4h 1.84% Zeichentrickserie
    14192.9h 1.82% Infomercial
    13850.6h 1.78% Animationsserie
    11843.1h 1.52% Comedyserie
    11082.0h 1.42% Morgenmagazin
    10701.7h 1.37% Magazin
    10535.1h 1.35% Religionsmagazin
    10408.1h 1.33% Talkshow
    7677.5h  0.98% E-Sport
    7330.4h  0.94% Programmende
    7284.9h  0.93% Sitcom
    6925.8h  0.89% Wetterbericht
    6917.7h  0.89% Börsenmagazin
    6678.4h  0.86% Quiz
    6551.4h  0.84% Komödie
    5822.0h  0.75% Wissensmagazin
    5680.4h  0.73% Politikmagazin
    5625.1h  0.72% Wirtschaftsmagazin
    5618.4h  0.72% Realityshow
    5593.8h  0.72% Telenovela
    5280.1h  0.68% Musikmagazin
