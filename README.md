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

**109** channels, **1,119,731.3** hours playtime between **2023-01-17** and **2024-11-03**


### playtime per genre (top 30)

    72914.9h 6.51% Nachrichten
    51488.4h 4.60% Verkaufsshow
    46549.4h 4.16% Krimiserie
    41061.7h 3.67% Werbesendung
    34993.5h 3.13% Dokureihe
    33468.3h 2.99% Dokusoap
    32720.2h 2.92% Regionalmagazin
    29406.6h 2.63% Dokumentation
    26516.9h 2.37% *unknown*
    20923.6h 1.87% Zeichentrickserie
    20616.0h 1.84% Infomercial
    20020.1h 1.79% Animationsserie
    16130.3h 1.44% Comedyserie
    15668.0h 1.40% Morgenmagazin
    15029.9h 1.34% Religionsmagazin
    14812.9h 1.32% Talkshow
    14123.3h 1.26% Magazin
    11072.6h 0.99% E-Sport
    10802.3h 0.96% Sitcom
    10131.6h 0.90% Wetterbericht
    9926.2h  0.89% Programmende
    9851.9h  0.88% Komödie
    9833.5h  0.88% Quiz
    8524.2h  0.76% Realityshow
    8480.7h  0.76% Börsenmagazin
    8459.1h  0.76% Politikmagazin
    8408.1h  0.75% Wissensmagazin
    7522.7h  0.67% Wirtschaftsmagazin
    7384.5h  0.66% Telenovela
    7322.6h  0.65% Dramaserie
