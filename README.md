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

**96** channels, **150,144.2** hours playtime between **2023-01-17** and **2023-04-10**


### playtime per genre (top 30)

    10335.8h 6.88% Nachrichten
    7451.2h  4.96% Verkaufsshow
    6200.0h  4.13% Krimiserie
    5039.8h  3.36% Werbesendung
    4809.1h  3.20% Dokureihe
    4546.1h  3.03% Dokusoap
    4359.8h  2.90% Regionalmagazin
    3774.8h  2.51% Dokumentation
    3508.6h  2.34% *unknown*
    2814.0h  1.87% Animationsserie
    2748.9h  1.83% Zeichentrickserie
    2739.8h  1.82% Infomercial
    2444.6h  1.63% Comedyserie
    2094.6h  1.40% Morgenmagazin
    2090.7h  1.39% Programmende
    1968.8h  1.31% Religionsmagazin
    1957.0h  1.30% Talkshow
    1606.7h  1.07% Magazin
    1544.0h  1.03% E-Sport
    1419.5h  0.95% Sitcom
    1381.6h  0.92% Börsenmagazin
    1345.7h  0.90% Wetterbericht
    1211.2h  0.81% Wirtschaftsmagazin
    1166.8h  0.78% Wissensmagazin
    1138.8h  0.76% Musikmagazin
    1126.6h  0.75% Quiz
    1040.8h  0.69% Dramaserie
    1036.4h  0.69% Telenovela
    1036.3h  0.69% Gesundheitsmagazin
    1027.2h  0.68% Sportmagazin
