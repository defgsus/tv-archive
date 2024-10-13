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

**109** channels, **1,088,926.5** hours playtime between **2023-01-17** and **2024-10-14**


### playtime per genre (top 30)

    70846.2h 6.51% Nachrichten
    50274.5h 4.62% Verkaufsshow
    45101.5h 4.14% Krimiserie
    39757.5h 3.65% Werbesendung
    34110.2h 3.13% Dokureihe
    32622.7h 3.00% Dokusoap
    31788.3h 2.92% Regionalmagazin
    28524.0h 2.62% Dokumentation
    25989.7h 2.39% *unknown*
    20277.6h 1.86% Zeichentrickserie
    20023.0h 1.84% Infomercial
    19491.5h 1.79% Animationsserie
    15793.5h 1.45% Comedyserie
    15215.6h 1.40% Morgenmagazin
    14748.3h 1.35% Religionsmagazin
    14383.6h 1.32% Talkshow
    13940.1h 1.28% Magazin
    10777.2h 0.99% E-Sport
    10467.0h 0.96% Sitcom
    9857.1h  0.91% Wetterbericht
    9692.5h  0.89% Programmende
    9575.6h  0.88% Komödie
    9521.1h  0.87% Quiz
    8377.9h  0.77% Börsenmagazin
    8231.4h  0.76% Realityshow
    8188.4h  0.75% Politikmagazin
    8187.0h  0.75% Wissensmagazin
    7337.2h  0.67% Wirtschaftsmagazin
    7160.3h  0.66% Telenovela
    7106.0h  0.65% Dramaserie
