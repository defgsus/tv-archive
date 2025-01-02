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

**109** channels, **1,211,802.1** hours playtime between **2023-01-17** and **2025-01-03**


### playtime per genre (top 30)

    79186.2h 6.53% Nachrichten
    54951.6h 4.53% Verkaufsshow
    50256.4h 4.15% Krimiserie
    44894.1h 3.70% Werbesendung
    37736.2h 3.11% Dokureihe
    35650.1h 2.94% Dokusoap
    35308.7h 2.91% Regionalmagazin
    32253.8h 2.66% Dokumentation
    28794.7h 2.38% *unknown*
    22771.1h 1.88% Zeichentrickserie
    22420.3h 1.85% Infomercial
    21633.9h 1.79% Animationsserie
    17082.8h 1.41% Comedyserie
    16910.7h 1.40% Morgenmagazin
    15974.9h 1.32% Talkshow
    15886.0h 1.31% Religionsmagazin
    14809.0h 1.22% Magazin
    11957.0h 0.99% E-Sport
    11602.1h 0.96% Sitcom
    11093.9h 0.92% Komödie
    10962.7h 0.90% Wetterbericht
    10726.6h 0.89% Quiz
    10653.1h 0.88% Programmende
    9362.6h  0.77% Realityshow
    9231.4h  0.76% Politikmagazin
    9009.8h  0.74% Wissensmagazin
    8744.6h  0.72% Börsenmagazin
    8029.7h  0.66% Wirtschaftsmagazin
    8022.6h  0.66% Dramaserie
    8022.6h  0.66% Arztserie
