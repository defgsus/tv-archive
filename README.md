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

**109** channels, **1,067,225.8** hours playtime between **2023-01-17** and **2024-09-30**


### playtime per genre (top 30)

    69384.3h 6.50% Nachrichten
    49401.0h 4.63% Verkaufsshow
    44078.8h 4.13% Krimiserie
    38828.2h 3.64% Werbesendung
    33469.0h 3.14% Dokureihe
    32035.6h 3.00% Dokusoap
    31136.2h 2.92% Regionalmagazin
    27928.5h 2.62% Dokumentation
    25594.8h 2.40% *unknown*
    19826.1h 1.86% Zeichentrickserie
    19601.7h 1.84% Infomercial
    19116.9h 1.79% Animationsserie
    15539.0h 1.46% Comedyserie
    14917.8h 1.40% Morgenmagazin
    14541.1h 1.36% Religionsmagazin
    14085.6h 1.32% Talkshow
    13804.0h 1.29% Magazin
    10552.0h 0.99% E-Sport
    10234.9h 0.96% Sitcom
    9659.3h  0.91% Wetterbericht
    9525.8h  0.89% Programmende
    9348.6h  0.88% Komödie
    9281.4h  0.87% Quiz
    8308.9h  0.78% Börsenmagazin
    8019.3h  0.75% Wissensmagazin
    8008.4h  0.75% Politikmagazin
    8002.4h  0.75% Realityshow
    7215.4h  0.68% Wirtschaftsmagazin
    7011.4h  0.66% Telenovela
    6945.2h  0.65% Dramaserie
