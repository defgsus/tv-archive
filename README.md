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

**109** channels, **1,106,974.2** hours playtime between **2023-01-17** and **2024-10-25**


### playtime per genre (top 30)

    72108.6h 6.51% Nachrichten
    50984.8h 4.61% Verkaufsshow
    46002.6h 4.16% Krimiserie
    40541.2h 3.66% Werbesendung
    34607.9h 3.13% Dokureihe
    33102.8h 2.99% Dokusoap
    32396.5h 2.93% Regionalmagazin
    29037.9h 2.62% Dokumentation
    26278.9h 2.37% *unknown*
    20658.9h 1.87% Zeichentrickserie
    20372.2h 1.84% Infomercial
    19804.5h 1.79% Animationsserie
    16001.8h 1.45% Comedyserie
    15501.7h 1.40% Morgenmagazin
    14905.5h 1.35% Religionsmagazin
    14630.4h 1.32% Talkshow
    14043.5h 1.27% Magazin
    10945.9h 0.99% E-Sport
    10670.8h 0.96% Sitcom
    10032.2h 0.91% Wetterbericht
    9831.5h  0.89% Programmende
    9730.3h  0.88% Quiz
    9676.6h  0.87% Komödie
    8446.5h  0.76% Realityshow
    8445.7h  0.76% Börsenmagazin
    8386.6h  0.76% Politikmagazin
    8316.4h  0.75% Wissensmagazin
    7456.5h  0.67% Wirtschaftsmagazin
    7312.2h  0.66% Telenovela
    7250.3h  0.65% Dramaserie
