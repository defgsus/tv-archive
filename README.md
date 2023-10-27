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

**97** channels, **511,145.7** hours playtime between **2023-01-17** and **2023-10-28**


### playtime per genre (top 30)

    33703.7h 6.59% Nachrichten
    24412.8h 4.78% Verkaufsshow
    20567.3h 4.02% Krimiserie
    17289.8h 3.38% Werbesendung
    16823.3h 3.29% Dokureihe
    15573.1h 3.05% Dokusoap
    14776.8h 2.89% Regionalmagazin
    12957.2h 2.53% Dokumentation
    12285.5h 2.40% *unknown*
    9542.4h  1.87% Zeichentrickserie
    9309.3h  1.82% Infomercial
    9141.2h  1.79% Animationsserie
    8100.3h  1.58% Comedyserie
    7269.0h  1.42% Morgenmagazin
    6868.1h  1.34% Religionsmagazin
    6805.1h  1.33% Talkshow
    6434.1h  1.26% Magazin
    5251.0h  1.03% Programmende
    5020.0h  0.98% E-Sport
    4884.7h  0.96% Sitcom
    4752.2h  0.93% Wetterbericht
    4623.0h  0.90% Börsenmagazin
    4285.8h  0.84% Quiz
    3970.6h  0.78% Komödie
    3871.5h  0.76% Wissensmagazin
    3861.2h  0.76% Wirtschaftsmagazin
    3838.7h  0.75% Musikmagazin
    3682.4h  0.72% Telenovela
    3526.9h  0.69% Politikmagazin
    3389.9h  0.66% Realityshow
