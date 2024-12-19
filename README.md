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

**109** channels, **1,190,983.7** hours playtime between **2023-01-17** and **2024-12-20**


### playtime per genre (top 30)

    77968.8h 6.55% Nachrichten
    54107.8h 4.54% Verkaufsshow
    49663.5h 4.17% Krimiserie
    43985.1h 3.69% Werbesendung
    37036.0h 3.11% Dokureihe
    35209.1h 2.96% Dokusoap
    34885.3h 2.93% Regionalmagazin
    31484.3h 2.64% Dokumentation
    28156.0h 2.36% *unknown*
    22333.0h 1.88% Zeichentrickserie
    22061.8h 1.85% Infomercial
    21302.8h 1.79% Animationsserie
    16881.6h 1.42% Comedyserie
    16715.1h 1.40% Morgenmagazin
    15796.3h 1.33% Talkshow
    15700.8h 1.32% Religionsmagazin
    14669.5h 1.23% Magazin
    11789.6h 0.99% E-Sport
    11460.4h 0.96% Sitcom
    10775.8h 0.90% Wetterbericht
    10564.4h 0.89% Quiz
    10519.7h 0.88% Komödie
    10496.2h 0.88% Programmende
    9201.2h  0.77% Realityshow
    9111.9h  0.77% Politikmagazin
    8914.2h  0.75% Wissensmagazin
    8712.9h  0.73% Börsenmagazin
    7956.1h  0.67% Wirtschaftsmagazin
    7917.2h  0.66% Dramaserie
    7909.5h  0.66% Telenovela
