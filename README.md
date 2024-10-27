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

**109** channels, **1,110,653.8** hours playtime between **2023-01-17** and **2024-10-28**


### playtime per genre (top 30)

    72294.4h 6.51% Nachrichten
    51120.2h 4.60% Verkaufsshow
    46138.2h 4.15% Krimiserie
    40688.5h 3.66% Werbesendung
    34771.8h 3.13% Dokureihe
    33216.1h 2.99% Dokusoap
    32450.6h 2.92% Regionalmagazin
    29116.9h 2.62% Dokumentation
    26351.7h 2.37% *unknown*
    20732.8h 1.87% Zeichentrickserie
    20447.5h 1.84% Infomercial
    19859.8h 1.79% Animationsserie
    16021.5h 1.44% Comedyserie
    15524.3h 1.40% Morgenmagazin
    14954.5h 1.35% Religionsmagazin
    14700.9h 1.32% Talkshow
    14070.6h 1.27% Magazin
    10988.4h 0.99% E-Sport
    10690.9h 0.96% Sitcom
    10050.3h 0.90% Wetterbericht
    9859.2h  0.89% Programmende
    9770.8h  0.88% Komödie
    9732.1h  0.88% Quiz
    8452.7h  0.76% Realityshow
    8445.8h  0.76% Börsenmagazin
    8387.4h  0.76% Politikmagazin
    8348.8h  0.75% Wissensmagazin
    7464.3h  0.67% Wirtschaftsmagazin
    7315.2h  0.66% Telenovela
    7254.1h  0.65% Dramaserie
