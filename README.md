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

**109** channels, **1,076,252.1** hours playtime between **2023-01-17** and **2024-10-06**


### playtime per genre (top 30)

    70018.2h 6.51% Nachrichten
    49774.2h 4.62% Verkaufsshow
    44519.6h 4.14% Krimiserie
    39205.4h 3.64% Werbesendung
    33683.8h 3.13% Dokureihe
    32276.6h 3.00% Dokusoap
    31422.2h 2.92% Regionalmagazin
    28167.4h 2.62% Dokumentation
    25759.1h 2.39% *unknown*
    20011.5h 1.86% Zeichentrickserie
    19776.0h 1.84% Infomercial
    19281.4h 1.79% Animationsserie
    15648.9h 1.45% Comedyserie
    15055.0h 1.40% Morgenmagazin
    14618.0h 1.36% Religionsmagazin
    14202.7h 1.32% Talkshow
    13847.7h 1.29% Magazin
    10641.2h 0.99% E-Sport
    10349.5h 0.96% Sitcom
    9744.8h  0.91% Wetterbericht
    9596.0h  0.89% Programmende
    9431.8h  0.88% Komödie
    9395.9h  0.87% Quiz
    8342.9h  0.78% Börsenmagazin
    8086.3h  0.75% Politikmagazin
    8083.9h  0.75% Realityshow
    8080.5h  0.75% Wissensmagazin
    7270.6h  0.68% Wirtschaftsmagazin
    7086.1h  0.66% Telenovela
    7023.8h  0.65% Dramaserie
