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

**109** channels, **1,114,298.1** hours playtime between **2023-01-17** and **2024-10-30**


### playtime per genre (top 30)

    72565.3h 6.51% Nachrichten
    51278.8h 4.60% Verkaufsshow
    46345.3h 4.16% Krimiserie
    40839.7h 3.67% Werbesendung
    34848.6h 3.13% Dokureihe
    33319.6h 2.99% Dokusoap
    32592.3h 2.92% Regionalmagazin
    29224.9h 2.62% Dokumentation
    26409.9h 2.37% *unknown*
    20810.6h 1.87% Zeichentrickserie
    20513.1h 1.84% Infomercial
    19921.6h 1.79% Animationsserie
    16059.0h 1.44% Comedyserie
    15594.1h 1.40% Morgenmagazin
    14985.6h 1.34% Religionsmagazin
    14738.5h 1.32% Talkshow
    14090.6h 1.26% Magazin
    11024.5h 0.99% E-Sport
    10737.2h 0.96% Sitcom
    10085.9h 0.91% Wetterbericht
    9886.5h  0.89% Programmende
    9787.1h  0.88% Quiz
    9768.4h  0.88% Komödie
    8482.1h  0.76% Realityshow
    8463.1h  0.76% Börsenmagazin
    8428.6h  0.76% Politikmagazin
    8373.0h  0.75% Wissensmagazin
    7489.3h  0.67% Wirtschaftsmagazin
    7348.2h  0.66% Telenovela
    7275.7h  0.65% Dramaserie
