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

**109** channels, **1,061,727.0** hours playtime between **2023-01-17** and **2024-09-25**


### playtime per genre (top 30)

    69074.2h 6.51% Nachrichten
    49193.0h 4.63% Verkaufsshow
    43868.5h 4.13% Krimiserie
    38584.7h 3.63% Werbesendung
    33312.2h 3.14% Dokureihe
    31910.0h 3.01% Dokusoap
    31013.6h 2.92% Regionalmagazin
    27776.4h 2.62% Dokumentation
    25481.0h 2.40% *unknown*
    19708.5h 1.86% Zeichentrickserie
    19492.1h 1.84% Infomercial
    19023.2h 1.79% Animationsserie
    15491.7h 1.46% Comedyserie
    14866.0h 1.40% Morgenmagazin
    14457.7h 1.36% Religionsmagazin
    13991.7h 1.32% Talkshow
    13758.4h 1.30% Magazin
    10507.0h 0.99% E-Sport
    10183.0h 0.96% Sitcom
    9614.8h  0.91% Wetterbericht
    9484.6h  0.89% Programmende
    9293.0h  0.88% Komödie
    9242.4h  0.87% Quiz
    8299.8h  0.78% Börsenmagazin
    7974.0h  0.75% Politikmagazin
    7968.8h  0.75% Wissensmagazin
    7957.5h  0.75% Realityshow
    7190.9h  0.68% Wirtschaftsmagazin
    6991.9h  0.66% Telenovela
    6913.1h  0.65% Dramaserie
