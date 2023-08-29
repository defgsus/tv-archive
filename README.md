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

**97** channels, **405,555.0** hours playtime between **2023-01-17** and **2023-08-30**


### playtime per genre (top 30)

    26767.7h 6.60% Nachrichten
    19162.9h 4.73% Verkaufsshow
    16483.4h 4.06% Krimiserie
    13673.6h 3.37% Werbesendung
    13419.8h 3.31% Dokureihe
    12302.6h 3.03% Dokusoap
    11647.6h 2.87% Regionalmagazin
    10273.7h 2.53% Dokumentation
    9780.1h  2.41% *unknown*
    7652.9h  1.89% Zeichentrickserie
    7407.6h  1.83% Infomercial
    7166.4h  1.77% Animationsserie
    6604.8h  1.63% Comedyserie
    5709.9h  1.41% Morgenmagazin
    5419.1h  1.34% Religionsmagazin
    5336.1h  1.32% Talkshow
    5047.9h  1.24% Magazin
    4440.4h  1.09% Programmende
    4024.1h  0.99% E-Sport
    3837.0h  0.95% Wetterbericht
    3793.9h  0.94% Sitcom
    3678.8h  0.91% Börsenmagazin
    3303.5h  0.81% Quiz
    3217.4h  0.79% Musikmagazin
    3165.6h  0.78% Komödie
    3079.8h  0.76% Wirtschaftsmagazin
    3033.3h  0.75% Wissensmagazin
    2837.6h  0.70% Telenovela
    2664.6h  0.66% Reportagereihe
    2612.5h  0.64% Politikmagazin
