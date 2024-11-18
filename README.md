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

**109** channels, **1,144,960.3** hours playtime between **2023-01-17** and **2024-11-19**


### playtime per genre (top 30)

    74627.8h 6.52% Nachrichten
    52351.7h 4.57% Verkaufsshow
    47739.7h 4.17% Krimiserie
    42131.1h 3.68% Werbesendung
    35732.4h 3.12% Dokureihe
    34129.8h 2.98% Dokusoap
    33477.4h 2.92% Regionalmagazin
    30098.8h 2.63% Dokumentation
    27061.4h 2.36% *unknown*
    21424.4h 1.87% Zeichentrickserie
    21115.9h 1.84% Infomercial
    20457.5h 1.79% Animationsserie
    16412.2h 1.43% Comedyserie
    16001.9h 1.40% Morgenmagazin
    15282.9h 1.33% Religionsmagazin
    15159.3h 1.32% Talkshow
    14324.0h 1.25% Magazin
    11306.0h 0.99% E-Sport
    11072.9h 0.97% Sitcom
    10357.6h 0.90% Wetterbericht
    10121.8h 0.88% Programmende
    10115.1h 0.88% Quiz
    10073.5h 0.88% Komödie
    8759.7h  0.77% Realityshow
    8680.7h  0.76% Politikmagazin
    8605.3h  0.75% Wissensmagazin
    8553.2h  0.75% Börsenmagazin
    7662.7h  0.67% Wirtschaftsmagazin
    7557.8h  0.66% Telenovela
    7516.1h  0.66% Dramaserie
