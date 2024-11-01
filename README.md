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

**109** channels, **1,117,905.1** hours playtime between **2023-01-17** and **2024-11-02**


### playtime per genre (top 30)

    72820.1h 6.51% Nachrichten
    51415.0h 4.60% Verkaufsshow
    46490.8h 4.16% Krimiserie
    40985.7h 3.67% Werbesendung
    34918.7h 3.12% Dokureihe
    33439.4h 2.99% Dokusoap
    32692.9h 2.92% Regionalmagazin
    29332.5h 2.62% Dokumentation
    26456.9h 2.37% *unknown*
    20886.0h 1.87% Zeichentrickserie
    20579.4h 1.84% Infomercial
    19979.5h 1.79% Animationsserie
    16108.2h 1.44% Comedyserie
    15660.0h 1.40% Morgenmagazin
    15014.3h 1.34% Religionsmagazin
    14788.2h 1.32% Talkshow
    14109.9h 1.26% Magazin
    11054.4h 0.99% E-Sport
    10781.2h 0.96% Sitcom
    10121.1h 0.91% Wetterbericht
    9912.5h  0.89% Programmende
    9822.6h  0.88% Quiz
    9819.0h  0.88% Komödie
    8520.3h  0.76% Realityshow
    8480.9h  0.76% Börsenmagazin
    8458.6h  0.76% Politikmagazin
    8396.6h  0.75% Wissensmagazin
    7519.7h  0.67% Wirtschaftsmagazin
    7383.1h  0.66% Telenovela
    7313.7h  0.65% Dramaserie
