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

**97** channels, **419,892.5** hours playtime between **2023-01-17** and **2023-09-07**


### playtime per genre (top 30)

    27724.9h 6.60% Nachrichten
    19892.7h 4.74% Verkaufsshow
    17035.5h 4.06% Krimiserie
    14170.1h 3.37% Werbesendung
    13852.1h 3.30% Dokureihe
    12751.0h 3.04% Dokusoap
    12089.2h 2.88% Regionalmagazin
    10614.9h 2.53% Dokumentation
    10038.4h 2.39% *unknown*
    7929.5h  1.89% Zeichentrickserie
    7665.7h  1.83% Infomercial
    7434.6h  1.77% Animationsserie
    6827.6h  1.63% Comedyserie
    5932.3h  1.41% Morgenmagazin
    5613.9h  1.34% Religionsmagazin
    5532.2h  1.32% Talkshow
    5239.9h  1.25% Magazin
    4551.1h  1.08% Programmende
    4149.4h  0.99% E-Sport
    3972.0h  0.95% Wetterbericht
    3941.7h  0.94% Sitcom
    3800.1h  0.91% Börsenmagazin
    3445.1h  0.82% Quiz
    3323.9h  0.79% Musikmagazin
    3282.2h  0.78% Komödie
    3187.6h  0.76% Wirtschaftsmagazin
    3138.7h  0.75% Wissensmagazin
    2955.1h  0.70% Telenovela
    2769.9h  0.66% Reportagereihe
    2728.2h  0.65% Politikmagazin
