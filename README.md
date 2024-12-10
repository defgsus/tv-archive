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

**109** channels, **1,177,019.1** hours playtime between **2023-01-17** and **2024-12-11**


### playtime per genre (top 30)

    76948.0h 6.54% Nachrichten
    53554.1h 4.55% Verkaufsshow
    49119.3h 4.17% Krimiserie
    43414.0h 3.69% Werbesendung
    36662.9h 3.11% Dokureihe
    34893.6h 2.96% Dokusoap
    34461.8h 2.93% Regionalmagazin
    31034.0h 2.64% Dokumentation
    27741.2h 2.36% *unknown*
    22067.1h 1.87% Zeichentrickserie
    21779.9h 1.85% Infomercial
    21046.0h 1.79% Animationsserie
    16737.5h 1.42% Comedyserie
    16489.8h 1.40% Morgenmagazin
    15614.0h 1.33% Talkshow
    15591.8h 1.32% Religionsmagazin
    14556.4h 1.24% Magazin
    11631.5h 0.99% E-Sport
    11340.6h 0.96% Sitcom
    10640.3h 0.90% Wetterbericht
    10417.9h 0.89% Quiz
    10385.5h 0.88% Programmende
    10367.5h 0.88% Komödie
    9077.5h  0.77% Realityshow
    8978.9h  0.76% Politikmagazin
    8820.8h  0.75% Wissensmagazin
    8664.3h  0.74% Börsenmagazin
    7862.9h  0.67% Wirtschaftsmagazin
    7806.6h  0.66% Telenovela
    7788.4h  0.66% Dramaserie
