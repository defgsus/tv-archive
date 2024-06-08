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

**108** channels, **892,654.9** hours playtime between **2023-01-17** and **2024-06-09**


### playtime per genre (top 30)

    58335.5h 6.54% Nachrichten
    42211.1h 4.73% Verkaufsshow
    36319.4h 4.07% Krimiserie
    31434.2h 3.52% Werbesendung
    28083.2h 3.15% Dokureihe
    27005.9h 3.03% Dokusoap
    25942.5h 2.91% Regionalmagazin
    23192.5h 2.60% Dokumentation
    22539.4h 2.52% *unknown*
    16416.3h 1.84% Zeichentrickserie
    16254.7h 1.82% Infomercial
    15913.2h 1.78% Animationsserie
    13387.8h 1.50% Comedyserie
    12735.5h 1.43% Magazin
    12562.2h 1.41% Morgenmagazin
    12075.3h 1.35% Religionsmagazin
    11890.0h 1.33% Talkshow
    8844.9h  0.99% E-Sport
    8302.6h  0.93% Sitcom
    8199.6h  0.92% Programmende
    7957.6h  0.89% Wetterbericht
    7758.5h  0.87% Börsenmagazin
    7738.7h  0.87% Quiz
    7704.1h  0.86% Komödie
    6619.9h  0.74% Politikmagazin
    6609.1h  0.74% Wissensmagazin
    6591.4h  0.74% Realityshow
    6308.7h  0.71% Wirtschaftsmagazin
    6234.5h  0.70% Telenovela
    5891.3h  0.66% Musikmagazin
