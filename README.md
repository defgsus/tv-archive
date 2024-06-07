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

**108** channels, **890,810.8** hours playtime between **2023-01-17** and **2024-06-08**


### playtime per genre (top 30)

    58245.8h 6.54% Nachrichten
    42116.9h 4.73% Verkaufsshow
    36268.9h 4.07% Krimiserie
    31360.9h 3.52% Werbesendung
    28027.3h 3.15% Dokureihe
    26947.9h 3.03% Dokusoap
    25917.0h 2.91% Regionalmagazin
    23108.1h 2.59% Dokumentation
    22508.8h 2.53% *unknown*
    16381.4h 1.84% Zeichentrickserie
    16216.9h 1.82% Infomercial
    15878.6h 1.78% Animationsserie
    13365.8h 1.50% Comedyserie
    12703.0h 1.43% Magazin
    12554.2h 1.41% Morgenmagazin
    12054.7h 1.35% Religionsmagazin
    11865.8h 1.33% Talkshow
    8822.8h  0.99% E-Sport
    8282.5h  0.93% Sitcom
    8186.2h  0.92% Programmende
    7939.9h  0.89% Wetterbericht
    7758.6h  0.87% Börsenmagazin
    7727.8h  0.87% Quiz
    7674.6h  0.86% Komödie
    6615.5h  0.74% Politikmagazin
    6596.5h  0.74% Wissensmagazin
    6593.4h  0.74% Realityshow
    6305.2h  0.71% Wirtschaftsmagazin
    6233.8h  0.70% Telenovela
    5881.3h  0.66% Musikmagazin
