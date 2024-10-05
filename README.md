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

**109** channels, **1,076,297.8** hours playtime between **2023-01-17** and **2024-10-06**


### playtime per genre (top 30)

    70022.6h 6.51% Nachrichten
    49774.3h 4.62% Verkaufsshow
    44521.2h 4.14% Krimiserie
    39205.4h 3.64% Werbesendung
    33684.9h 3.13% Dokureihe
    32278.8h 3.00% Dokusoap
    31422.4h 2.92% Regionalmagazin
    28169.8h 2.62% Dokumentation
    25763.7h 2.39% *unknown*
    20010.8h 1.86% Zeichentrickserie
    19776.0h 1.84% Infomercial
    19281.5h 1.79% Animationsserie
    15649.2h 1.45% Comedyserie
    15059.0h 1.40% Morgenmagazin
    14617.8h 1.36% Religionsmagazin
    14202.8h 1.32% Talkshow
    13848.5h 1.29% Magazin
    10641.2h 0.99% E-Sport
    10348.7h 0.96% Sitcom
    9744.5h  0.91% Wetterbericht
    9596.0h  0.89% Programmende
    9430.1h  0.88% Komödie
    9395.9h  0.87% Quiz
    8342.9h  0.78% Börsenmagazin
    8086.3h  0.75% Politikmagazin
    8083.9h  0.75% Realityshow
    8080.5h  0.75% Wissensmagazin
    7270.6h  0.68% Wirtschaftsmagazin
    7086.1h  0.66% Telenovela
    7023.8h  0.65% Dramaserie
