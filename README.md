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

**96** channels, **330,280.6** hours playtime between **2023-01-17** and **2023-07-19**


### playtime per genre (top 30)

    21970.9h 6.65% Nachrichten
    15790.1h 4.78% Verkaufsshow
    13272.8h 4.02% Krimiserie
    11080.2h 3.35% Werbesendung
    10775.0h 3.26% Dokureihe
    9992.6h  3.03% Dokusoap
    9457.7h  2.86% Regionalmagazin
    8317.5h  2.52% Dokumentation
    8080.4h  2.45% *unknown*
    6286.7h  1.90% Zeichentrickserie
    6036.1h  1.83% Infomercial
    5822.1h  1.76% Animationsserie
    5456.3h  1.65% Comedyserie
    4625.8h  1.40% Morgenmagazin
    4377.1h  1.33% Religionsmagazin
    4373.3h  1.32% Talkshow
    3925.9h  1.19% Magazin
    3858.4h  1.17% Programmende
    3267.6h  0.99% E-Sport
    3130.1h  0.95% Sitcom
    3083.1h  0.93% Wetterbericht
    2962.9h  0.90% Börsenmagazin
    2631.5h  0.80% Quiz
    2589.1h  0.78% Musikmagazin
    2552.6h  0.77% Wirtschaftsmagazin
    2524.8h  0.76% Wissensmagazin
    2507.9h  0.76% Komödie
    2295.2h  0.69% Telenovela
    2190.2h  0.66% Sportmagazin
    2103.3h  0.64% Dramaserie
