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

**109** channels, **1,072,664.1** hours playtime between **2023-01-17** and **2024-10-03**


### playtime per genre (top 30)

    69795.6h 6.51% Nachrichten
    49623.6h 4.63% Verkaufsshow
    44358.4h 4.14% Krimiserie
    39055.3h 3.64% Werbesendung
    33580.3h 3.13% Dokureihe
    32187.0h 3.00% Dokusoap
    31344.1h 2.92% Regionalmagazin
    28059.8h 2.62% Dokumentation
    25687.9h 2.39% *unknown*
    19934.7h 1.86% Zeichentrickserie
    19703.9h 1.84% Infomercial
    19211.4h 1.79% Animationsserie
    15616.0h 1.46% Comedyserie
    15017.1h 1.40% Morgenmagazin
    14585.9h 1.36% Religionsmagazin
    14148.6h 1.32% Talkshow
    13827.7h 1.29% Magazin
    10608.6h 0.99% E-Sport
    10309.6h 0.96% Sitcom
    9716.2h  0.91% Wetterbericht
    9567.5h  0.89% Programmende
    9380.0h  0.87% Komödie
    9355.5h  0.87% Quiz
    8334.4h  0.78% Börsenmagazin
    8074.9h  0.75% Politikmagazin
    8064.6h  0.75% Realityshow
    8058.6h  0.75% Wissensmagazin
    7255.2h  0.68% Wirtschaftsmagazin
    7068.6h  0.66% Telenovela
    7002.0h  0.65% Dramaserie
