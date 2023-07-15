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

**96** channels, **324,951.8** hours playtime between **2023-01-17** and **2023-07-16**


### playtime per genre (top 30)

    21627.5h 6.66% Nachrichten
    15548.3h 4.78% Verkaufsshow
    13046.9h 4.02% Krimiserie
    10904.2h 3.36% Werbesendung
    10595.0h 3.26% Dokureihe
    9852.1h  3.03% Dokusoap
    9302.8h  2.86% Regionalmagazin
    8167.4h  2.51% Dokumentation
    7976.7h  2.45% *unknown*
    6187.4h  1.90% Zeichentrickserie
    5942.0h  1.83% Infomercial
    5719.3h  1.76% Animationsserie
    5377.7h  1.65% Comedyserie
    4552.1h  1.40% Morgenmagazin
    4305.7h  1.33% Talkshow
    4292.8h  1.32% Religionsmagazin
    3873.1h  1.19% Magazin
    3817.3h  1.17% Programmende
    3219.6h  0.99% E-Sport
    3083.7h  0.95% Sitcom
    3026.7h  0.93% Wetterbericht
    2892.9h  0.89% Börsenmagazin
    2578.6h  0.79% Quiz
    2549.5h  0.78% Musikmagazin
    2518.1h  0.77% Wirtschaftsmagazin
    2487.4h  0.77% Wissensmagazin
    2473.9h  0.76% Komödie
    2268.7h  0.70% Telenovela
    2152.8h  0.66% Sportmagazin
    2081.3h  0.64% Wirtschaftstalk
