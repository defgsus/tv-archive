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

**97** channels, **419,895.6** hours playtime between **2023-01-17** and **2023-09-07**


### playtime per genre (top 30)

    27726.1h 6.60% Nachrichten
    19887.6h 4.74% Verkaufsshow
    17036.3h 4.06% Krimiserie
    14173.1h 3.38% Werbesendung
    13851.6h 3.30% Dokureihe
    12751.2h 3.04% Dokusoap
    12089.4h 2.88% Regionalmagazin
    10613.9h 2.53% Dokumentation
    10038.9h 2.39% *unknown*
    7929.8h  1.89% Zeichentrickserie
    7665.7h  1.83% Infomercial
    7434.2h  1.77% Animationsserie
    6827.7h  1.63% Comedyserie
    5932.3h  1.41% Morgenmagazin
    5613.9h  1.34% Religionsmagazin
    5532.1h  1.32% Talkshow
    5241.9h  1.25% Magazin
    4551.2h  1.08% Programmende
    4149.4h  0.99% E-Sport
    3970.9h  0.95% Wetterbericht
    3941.3h  0.94% Sitcom
    3798.6h  0.90% Börsenmagazin
    3445.1h  0.82% Quiz
    3323.9h  0.79% Musikmagazin
    3282.2h  0.78% Komödie
    3187.6h  0.76% Wirtschaftsmagazin
    3138.7h  0.75% Wissensmagazin
    2955.8h  0.70% Telenovela
    2769.8h  0.66% Reportagereihe
    2728.2h  0.65% Politikmagazin
