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

**109** channels, **1,109,259.1** hours playtime between **2023-01-17** and **2024-10-27**


### playtime per genre (top 30)

    72201.8h 6.51% Nachrichten
    51055.3h 4.60% Verkaufsshow
    46123.4h 4.16% Krimiserie
    40606.7h 3.66% Werbesendung
    34709.1h 3.13% Dokureihe
    33219.2h 2.99% Dokusoap
    32417.3h 2.92% Regionalmagazin
    29076.4h 2.62% Dokumentation
    26317.4h 2.37% *unknown*
    20722.0h 1.87% Zeichentrickserie
    20409.5h 1.84% Infomercial
    19856.4h 1.79% Animationsserie
    16009.5h 1.44% Comedyserie
    15515.2h 1.40% Morgenmagazin
    14923.1h 1.35% Religionsmagazin
    14668.0h 1.32% Talkshow
    14081.3h 1.27% Magazin
    10962.0h 0.99% E-Sport
    10685.0h 0.96% Sitcom
    10042.6h 0.91% Wetterbericht
    9844.9h  0.89% Programmende
    9727.7h  0.88% Quiz
    9714.1h  0.88% Komödie
    8445.8h  0.76% Börsenmagazin
    8435.7h  0.76% Realityshow
    8379.1h  0.76% Politikmagazin
    8326.1h  0.75% Wissensmagazin
    7457.3h  0.67% Wirtschaftsmagazin
    7314.8h  0.66% Telenovela
    7248.9h  0.65% Dramaserie
