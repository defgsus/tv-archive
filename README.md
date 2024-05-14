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

**108** channels, **854,277.7** hours playtime between **2023-01-17** and **2024-05-15**


### playtime per genre (top 30)

    55779.3h 6.53% Nachrichten
    40700.3h 4.76% Verkaufsshow
    34798.4h 4.07% Krimiserie
    29903.2h 3.50% Werbesendung
    26905.0h 3.15% Dokureihe
    25814.5h 3.02% Dokusoap
    24858.4h 2.91% Regionalmagazin
    22135.9h 2.59% Dokumentation
    21750.8h 2.55% *unknown*
    15708.8h 1.84% Zeichentrickserie
    15538.1h 1.82% Infomercial
    15214.1h 1.78% Animationsserie
    12898.2h 1.51% Comedyserie
    12108.5h 1.42% Magazin
    12044.8h 1.41% Morgenmagazin
    11552.7h 1.35% Religionsmagazin
    11376.7h 1.33% Talkshow
    8484.3h  0.99% E-Sport
    7911.0h  0.93% Programmende
    7881.6h  0.92% Sitcom
    7591.2h  0.89% Wetterbericht
    7520.6h  0.88% Börsenmagazin
    7389.1h  0.86% Quiz
    7306.7h  0.86% Komödie
    6313.2h  0.74% Wissensmagazin
    6286.4h  0.74% Politikmagazin
    6279.8h  0.74% Realityshow
    6090.6h  0.71% Wirtschaftsmagazin
    6078.0h  0.71% Telenovela
    5665.0h  0.66% Musikmagazin
