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

**109** channels, **908,899.5** hours playtime between **2023-01-17** and **2024-06-19**


### playtime per genre (top 30)

    59397.7h 6.54% Nachrichten
    42814.1h 4.71% Verkaufsshow
    37046.8h 4.08% Krimiserie
    32114.5h 3.53% Werbesendung
    28603.8h 3.15% Dokureihe
    27473.7h 3.02% Dokusoap
    26436.1h 2.91% Regionalmagazin
    23615.6h 2.60% Dokumentation
    22845.1h 2.51% *unknown*
    16719.8h 1.84% Zeichentrickserie
    16560.3h 1.82% Infomercial
    16221.6h 1.78% Animationsserie
    13604.0h 1.50% Comedyserie
    12960.0h 1.43% Magazin
    12796.1h 1.41% Morgenmagazin
    12314.6h 1.35% Religionsmagazin
    12101.6h 1.33% Talkshow
    8990.7h  0.99% E-Sport
    8488.2h  0.93% Sitcom
    8324.4h  0.92% Programmende
    8116.8h  0.89% Wetterbericht
    7863.7h  0.87% Quiz
    7859.4h  0.86% Komödie
    7811.6h  0.86% Börsenmagazin
    6818.1h  0.75% Politikmagazin
    6743.0h  0.74% Wissensmagazin
    6732.2h  0.74% Realityshow
    6388.5h  0.70% Wirtschaftsmagazin
    6286.3h  0.69% Telenovela
    5971.0h  0.66% Musikmagazin
