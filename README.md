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

**96** channels, **148,323.6** hours playtime between **2023-01-17** and **2023-04-09**


### playtime per genre (top 30)

    10258.2h 6.92% Nachrichten
    7361.4h  4.96% Verkaufsshow
    6145.3h  4.14% Krimiserie
    4981.4h  3.36% Werbesendung
    4723.5h  3.18% Dokureihe
    4490.1h  3.03% Dokusoap
    4333.9h  2.92% Regionalmagazin
    3727.8h  2.51% Dokumentation
    3469.8h  2.34% *unknown*
    2786.2h  1.88% Animationsserie
    2719.6h  1.83% Zeichentrickserie
    2718.1h  1.83% Infomercial
    2423.2h  1.63% Comedyserie
    2090.4h  1.41% Morgenmagazin
    2059.3h  1.39% Programmende
    1930.6h  1.30% Religionsmagazin
    1930.3h  1.30% Talkshow
    1587.6h  1.07% Magazin
    1536.8h  1.04% E-Sport
    1418.0h  0.96% Sitcom
    1364.6h  0.92% Börsenmagazin
    1330.4h  0.90% Wetterbericht
    1200.8h  0.81% Wirtschaftsmagazin
    1158.1h  0.78% Wissensmagazin
    1120.6h  0.76% Quiz
    1120.1h  0.76% Musikmagazin
    1036.4h  0.70% Telenovela
    1030.9h  0.70% Dramaserie
    1028.2h  0.69% Gesundheitsmagazin
    1017.9h  0.69% Sportmagazin
