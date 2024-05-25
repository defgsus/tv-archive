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

**108** channels, **870,736.2** hours playtime between **2023-01-17** and **2024-05-26**


### playtime per genre (top 30)

    56868.2h 6.53% Nachrichten
    41375.4h 4.75% Verkaufsshow
    35435.8h 4.07% Krimiserie
    30528.4h 3.51% Werbesendung
    27422.9h 3.15% Dokureihe
    26337.3h 3.02% Dokusoap
    25295.8h 2.91% Regionalmagazin
    22622.4h 2.60% Dokumentation
    22092.8h 2.54% *unknown*
    16002.2h 1.84% Zeichentrickserie
    15836.5h 1.82% Infomercial
    15512.1h 1.78% Animationsserie
    13091.5h 1.50% Comedyserie
    12366.3h 1.42% Magazin
    12251.5h 1.41% Morgenmagazin
    11776.5h 1.35% Religionsmagazin
    11591.7h 1.33% Talkshow
    8623.4h  0.99% E-Sport
    8044.9h  0.92% Sitcom
    8034.4h  0.92% Programmende
    7744.6h  0.89% Wetterbericht
    7630.0h  0.88% Börsenmagazin
    7531.3h  0.86% Quiz
    7519.3h  0.86% Komödie
    6431.3h  0.74% Wissensmagazin
    6418.6h  0.74% Realityshow
    6382.3h  0.73% Politikmagazin
    6184.1h  0.71% Wirtschaftsmagazin
    6147.2h  0.71% Telenovela
    5762.9h  0.66% Musikmagazin
