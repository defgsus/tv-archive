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

**109** channels, **1,161,681.5** hours playtime between **2023-01-17** and **2024-12-01**


### playtime per genre (top 30)

    75849.2h 6.53% Nachrichten
    53011.2h 4.56% Verkaufsshow
    48470.4h 4.17% Krimiserie
    42794.7h 3.68% Werbesendung
    36209.7h 3.12% Dokureihe
    34544.1h 2.97% Dokusoap
    33991.2h 2.93% Regionalmagazin
    30554.7h 2.63% Dokumentation
    27393.3h 2.36% *unknown*
    21770.2h 1.87% Zeichentrickserie
    21469.0h 1.85% Infomercial
    20769.8h 1.79% Animationsserie
    16578.0h 1.43% Comedyserie
    16263.0h 1.40% Morgenmagazin
    15442.3h 1.33% Religionsmagazin
    15423.1h 1.33% Talkshow
    14452.7h 1.24% Magazin
    11474.0h 0.99% E-Sport
    11215.3h 0.97% Sitcom
    10493.6h 0.90% Wetterbericht
    10267.8h 0.88% Quiz
    10259.4h 0.88% Programmende
    10196.0h 0.88% Komödie
    8932.1h  0.77% Realityshow
    8830.3h  0.76% Politikmagazin
    8720.4h  0.75% Wissensmagazin
    8613.7h  0.74% Börsenmagazin
    7767.0h  0.67% Wirtschaftsmagazin
    7690.0h  0.66% Telenovela
    7676.6h  0.66% Dramaserie
