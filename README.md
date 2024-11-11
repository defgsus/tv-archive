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

**109** channels, **1,134,122.7** hours playtime between **2023-01-17** and **2024-11-12**


### playtime per genre (top 30)

    73884.5h 6.51% Nachrichten
    51974.2h 4.58% Verkaufsshow
    47216.8h 4.16% Krimiserie
    41665.4h 3.67% Werbesendung
    35432.2h 3.12% Dokureihe
    33848.1h 2.98% Dokusoap
    33151.1h 2.92% Regionalmagazin
    29830.2h 2.63% Dokumentation
    26856.9h 2.37% *unknown*
    21206.6h 1.87% Zeichentrickserie
    20895.5h 1.84% Infomercial
    20279.5h 1.79% Animationsserie
    16283.6h 1.44% Comedyserie
    15851.8h 1.40% Morgenmagazin
    15176.8h 1.34% Religionsmagazin
    15008.2h 1.32% Talkshow
    14240.8h 1.26% Magazin
    11200.2h 0.99% E-Sport
    10954.0h 0.97% Sitcom
    10254.1h 0.90% Wetterbericht
    10039.0h 0.89% Programmende
    9995.4h  0.88% Quiz
    9988.3h  0.88% Komödie
    8660.5h  0.76% Realityshow
    8580.9h  0.76% Politikmagazin
    8521.5h  0.75% Börsenmagazin
    8518.4h  0.75% Wissensmagazin
    7598.9h  0.67% Wirtschaftsmagazin
    7481.2h  0.66% Telenovela
    7420.8h  0.65% Dramaserie
