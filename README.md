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

**96** channels, **312,391.9** hours playtime between **2023-01-17** and **2023-07-09**


### playtime per genre (top 30)

    20821.2h 6.67% Nachrichten
    14966.1h 4.79% Verkaufsshow
    12528.1h 4.01% Krimiserie
    10465.8h 3.35% Werbesendung
    10142.0h 3.25% Dokureihe
    9467.6h  3.03% Dokusoap
    8938.5h  2.86% Regionalmagazin
    7858.5h  2.52% Dokumentation
    7707.4h  2.47% *unknown*
    5951.4h  1.91% Zeichentrickserie
    5720.3h  1.83% Infomercial
    5501.4h  1.76% Animationsserie
    5186.1h  1.66% Comedyserie
    4373.8h  1.40% Morgenmagazin
    4135.9h  1.32% Talkshow
    4118.6h  1.32% Religionsmagazin
    3720.2h  1.19% Programmende
    3698.8h  1.18% Magazin
    3086.2h  0.99% E-Sport
    2960.8h  0.95% Sitcom
    2899.4h  0.93% Wetterbericht
    2779.7h  0.89% Börsenmagazin
    2471.9h  0.79% Quiz
    2450.2h  0.78% Musikmagazin
    2428.8h  0.78% Wirtschaftsmagazin
    2394.2h  0.77% Wissensmagazin
    2368.8h  0.76% Komödie
    2198.6h  0.70% Telenovela
    2080.2h  0.67% Sportmagazin
    1996.9h  0.64% Wirtschaftstalk
