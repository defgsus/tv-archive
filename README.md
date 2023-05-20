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

**96** channels, **224,617.8** hours playtime between **2023-01-17** and **2023-05-21**


### playtime per genre (top 30)

    15111.1h 6.73% Nachrichten
    10881.1h 4.84% Verkaufsshow
    9087.7h  4.05% Krimiserie
    7458.6h  3.32% Werbesendung
    7314.3h  3.26% Dokureihe
    6674.4h  2.97% Dokusoap
    6448.7h  2.87% Regionalmagazin
    5741.0h  2.56% Dokumentation
    5543.4h  2.47% *unknown*
    4181.7h  1.86% Zeichentrickserie
    4115.4h  1.83% Infomercial
    4056.1h  1.81% Animationsserie
    3746.0h  1.67% Comedyserie
    3103.2h  1.38% Morgenmagazin
    3044.6h  1.36% Programmende
    2957.4h  1.32% Talkshow
    2933.1h  1.31% Religionsmagazin
    2581.0h  1.15% Magazin
    2240.5h  1.00% E-Sport
    2119.9h  0.94% Sitcom
    2037.7h  0.91% Börsenmagazin
    2035.2h  0.91% Wetterbericht
    1772.4h  0.79% Wirtschaftsmagazin
    1743.8h  0.78% Wissensmagazin
    1730.1h  0.77% Musikmagazin
    1729.3h  0.77% Quiz
    1586.2h  0.71% Komödie
    1580.2h  0.70% Telenovela
    1564.8h  0.70% Sportmagazin
    1516.6h  0.68% Gesundheitsmagazin
