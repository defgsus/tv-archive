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

**102** channels, **804,823.7** hours playtime between **2023-01-17** and **2024-04-12**


### playtime per genre (top 30)

    52370.2h 6.51% Nachrichten
    38568.9h 4.79% Verkaufsshow
    32760.5h 4.07% Krimiserie
    28063.8h 3.49% Werbesendung
    25524.0h 3.17% Dokureihe
    24249.5h 3.01% Dokusoap
    23391.8h 2.91% Regionalmagazin
    20922.4h 2.60% *unknown*
    20839.1h 2.59% Dokumentation
    14779.5h 1.84% Zeichentrickserie
    14588.9h 1.81% Infomercial
    14296.9h 1.78% Animationsserie
    12201.5h 1.52% Comedyserie
    11368.7h 1.41% Morgenmagazin
    11149.5h 1.39% Magazin
    10870.5h 1.35% Religionsmagazin
    10707.1h 1.33% Talkshow
    7918.3h  0.98% E-Sport
    7523.9h  0.93% Programmende
    7452.1h  0.93% Sitcom
    7144.0h  0.89% Wetterbericht
    7099.9h  0.88% Börsenmagazin
    6917.4h  0.86% Quiz
    6887.5h  0.86% Komödie
    5972.1h  0.74% Wissensmagazin
    5863.2h  0.73% Politikmagazin
    5796.1h  0.72% Realityshow
    5769.0h  0.72% Wirtschaftsmagazin
    5748.9h  0.71% Telenovela
    5399.9h  0.67% Musikmagazin
