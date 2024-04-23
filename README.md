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

**102** channels, **824,545.5** hours playtime between **2023-01-17** and **2024-04-24**


### playtime per genre (top 30)

    53731.6h 6.52% Nachrichten
    39560.4h 4.80% Verkaufsshow
    33584.8h 4.07% Krimiserie
    28815.4h 3.49% Werbesendung
    26083.7h 3.16% Dokureihe
    24876.3h 3.02% Dokusoap
    23990.7h 2.91% Regionalmagazin
    21325.4h 2.59% Dokumentation
    21106.8h 2.56% *unknown*
    15134.4h 1.84% Zeichentrickserie
    14972.9h 1.82% Infomercial
    14679.9h 1.78% Animationsserie
    12489.0h 1.51% Comedyserie
    11636.1h 1.41% Morgenmagazin
    11529.5h 1.40% Magazin
    11131.4h 1.35% Religionsmagazin
    10981.7h 1.33% Talkshow
    8156.6h  0.99% E-Sport
    7676.4h  0.93% Programmende
    7592.4h  0.92% Sitcom
    7315.6h  0.89% Wetterbericht
    7268.3h  0.88% Börsenmagazin
    7121.1h  0.86% Quiz
    7027.1h  0.85% Komödie
    6108.1h  0.74% Wissensmagazin
    6024.5h  0.73% Politikmagazin
    5963.4h  0.72% Realityshow
    5901.8h  0.72% Telenovela
    5899.1h  0.72% Wirtschaftsmagazin
    5504.2h  0.67% Musikmagazin
