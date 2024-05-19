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

**108** channels, **861,654.1** hours playtime between **2023-01-17** and **2024-05-20**


### playtime per genre (top 30)

    56232.2h 6.53% Nachrichten
    41024.0h 4.76% Verkaufsshow
    35065.4h 4.07% Krimiserie
    30181.9h 3.50% Werbesendung
    27121.8h 3.15% Dokureihe
    26049.0h 3.02% Dokusoap
    25043.9h 2.91% Regionalmagazin
    22333.9h 2.59% Dokumentation
    21899.4h 2.54% *unknown*
    15839.7h 1.84% Zeichentrickserie
    15675.5h 1.82% Infomercial
    15342.7h 1.78% Animationsserie
    12976.5h 1.51% Comedyserie
    12234.3h 1.42% Magazin
    12129.1h 1.41% Morgenmagazin
    11661.4h 1.35% Religionsmagazin
    11480.9h 1.33% Talkshow
    8550.6h  0.99% E-Sport
    7966.6h  0.92% Programmende
    7952.4h  0.92% Sitcom
    7658.6h  0.89% Wetterbericht
    7558.9h  0.88% Börsenmagazin
    7449.6h  0.86% Quiz
    7402.9h  0.86% Komödie
    6372.7h  0.74% Wissensmagazin
    6355.5h  0.74% Realityshow
    6325.2h  0.73% Politikmagazin
    6128.3h  0.71% Wirtschaftsmagazin
    6109.7h  0.71% Telenovela
    5713.3h  0.66% Musikmagazin
