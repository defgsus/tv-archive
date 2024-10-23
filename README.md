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

**109** channels, **1,105,209.8** hours playtime between **2023-01-17** and **2024-10-24**


### playtime per genre (top 30)

    71978.3h 6.51% Nachrichten
    50909.9h 4.61% Verkaufsshow
    45911.6h 4.15% Krimiserie
    40466.6h 3.66% Werbesendung
    34553.1h 3.13% Dokureihe
    33062.9h 2.99% Dokusoap
    32328.0h 2.93% Regionalmagazin
    28966.8h 2.62% Dokumentation
    26241.3h 2.37% *unknown*
    20620.0h 1.87% Zeichentrickserie
    20337.0h 1.84% Infomercial
    19774.8h 1.79% Animationsserie
    15981.1h 1.45% Comedyserie
    15473.3h 1.40% Morgenmagazin
    14893.4h 1.35% Religionsmagazin
    14610.4h 1.32% Talkshow
    14037.7h 1.27% Magazin
    10927.7h 0.99% E-Sport
    10647.0h 0.96% Sitcom
    10015.0h 0.91% Wetterbericht
    9817.0h  0.89% Programmende
    9698.0h  0.88% Quiz
    9676.1h  0.88% Komödie
    8436.8h  0.76% Börsenmagazin
    8417.2h  0.76% Realityshow
    8365.6h  0.76% Politikmagazin
    8302.4h  0.75% Wissensmagazin
    7440.3h  0.67% Wirtschaftsmagazin
    7293.8h  0.66% Telenovela
    7230.4h  0.65% Dramaserie
