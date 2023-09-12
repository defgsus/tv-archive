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

**97** channels, **430,630.3** hours playtime between **2023-01-17** and **2023-09-13**


### playtime per genre (top 30)

    28419.2h 6.60% Nachrichten
    20431.3h 4.74% Verkaufsshow
    17468.9h 4.06% Krimiserie
    14529.1h 3.37% Werbesendung
    14194.4h 3.30% Dokureihe
    13089.6h 3.04% Dokusoap
    12399.2h 2.88% Regionalmagazin
    10855.2h 2.52% Dokumentation
    10234.5h 2.38% *unknown*
    8132.3h  1.89% Zeichentrickserie
    7858.3h  1.82% Infomercial
    7627.7h  1.77% Animationsserie
    6985.4h  1.62% Comedyserie
    6083.8h  1.41% Morgenmagazin
    5760.4h  1.34% Religionsmagazin
    5699.9h  1.32% Talkshow
    5382.6h  1.25% Magazin
    4633.3h  1.08% Programmende
    4265.2h  0.99% E-Sport
    4065.7h  0.94% Wetterbericht
    4040.9h  0.94% Sitcom
    3914.3h  0.91% Börsenmagazin
    3553.3h  0.83% Quiz
    3395.0h  0.79% Musikmagazin
    3333.0h  0.77% Komödie
    3262.9h  0.76% Wirtschaftsmagazin
    3217.6h  0.75% Wissensmagazin
    3034.4h  0.70% Telenovela
    2835.6h  0.66% Reportagereihe
    2806.3h  0.65% Politikmagazin
