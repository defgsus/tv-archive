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

**96** channels, **367,972.5** hours playtime between **2023-01-17** and **2023-08-09**


### playtime per genre (top 30)

    24361.5h 6.62% Nachrichten
    17499.3h 4.76% Verkaufsshow
    14873.1h 4.04% Krimiserie
    12394.4h 3.37% Werbesendung
    12105.9h 3.29% Dokureihe
    11112.9h 3.02% Dokusoap
    10557.9h 2.87% Regionalmagazin
    9263.2h  2.52% Dokumentation
    8952.1h  2.43% *unknown*
    6962.9h  1.89% Zeichentrickserie
    6727.1h  1.83% Infomercial
    6504.2h  1.77% Animationsserie
    6040.3h  1.64% Comedyserie
    5160.5h  1.40% Morgenmagazin
    4895.6h  1.33% Religionsmagazin
    4848.2h  1.32% Talkshow
    4408.4h  1.20% Magazin
    4146.2h  1.13% Programmende
    3642.4h  0.99% E-Sport
    3462.0h  0.94% Wetterbericht
    3456.6h  0.94% Sitcom
    3340.9h  0.91% Börsenmagazin
    2940.8h  0.80% Quiz
    2896.4h  0.79% Musikmagazin
    2827.1h  0.77% Komödie
    2820.8h  0.77% Wirtschaftsmagazin
    2771.5h  0.75% Wissensmagazin
    2542.1h  0.69% Telenovela
    2399.4h  0.65% Sportmagazin
    2379.5h  0.65% Reportagereihe
