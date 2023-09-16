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

**97** channels, **437,792.8** hours playtime between **2023-01-17** and **2023-09-17**


### playtime per genre (top 30)

    28896.1h 6.60% Nachrichten
    20800.5h 4.75% Verkaufsshow
    17734.0h 4.05% Krimiserie
    14771.2h 3.37% Werbesendung
    14419.8h 3.29% Dokureihe
    13305.8h 3.04% Dokusoap
    12609.0h 2.88% Regionalmagazin
    11031.3h 2.52% Dokumentation
    10378.9h 2.37% *unknown*
    8257.2h  1.89% Zeichentrickserie
    7989.0h  1.82% Infomercial
    7762.7h  1.77% Animationsserie
    7093.4h  1.62% Comedyserie
    6193.5h  1.41% Morgenmagazin
    5851.7h  1.34% Religionsmagazin
    5801.5h  1.33% Talkshow
    5473.6h  1.25% Magazin
    4687.6h  1.07% Programmende
    4328.8h  0.99% E-Sport
    4132.2h  0.94% Wetterbericht
    4119.9h  0.94% Sitcom
    3954.2h  0.90% Börsenmagazin
    3628.1h  0.83% Quiz
    3427.3h  0.78% Musikmagazin
    3400.6h  0.78% Komödie
    3314.5h  0.76% Wirtschaftsmagazin
    3273.8h  0.75% Wissensmagazin
    3094.9h  0.71% Telenovela
    2885.9h  0.66% Reportagereihe
    2861.4h  0.65% Politikmagazin
