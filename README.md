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

**96** channels, **162,959.8** hours playtime between **2023-01-17** and **2023-04-17**


### playtime per genre (top 30)

    11118.4h 6.82% Nachrichten
    8056.8h  4.94% Verkaufsshow
    6699.1h  4.11% Krimiserie
    5462.8h  3.35% Werbesendung
    5292.8h  3.25% Dokureihe
    4886.5h  3.00% Dokusoap
    4703.1h  2.89% Regionalmagazin
    4124.6h  2.53% Dokumentation
    3845.6h  2.36% *unknown*
    3021.1h  1.85% Animationsserie
    2989.9h  1.83% Zeichentrickserie
    2967.3h  1.82% Infomercial
    2660.2h  1.63% Comedyserie
    2265.6h  1.39% Programmende
    2246.8h  1.38% Morgenmagazin
    2129.2h  1.31% Religionsmagazin
    2109.8h  1.29% Talkshow
    1761.2h  1.08% Magazin
    1667.9h  1.02% E-Sport
    1533.1h  0.94% Sitcom
    1501.8h  0.92% Börsenmagazin
    1468.3h  0.90% Wetterbericht
    1303.4h  0.80% Wirtschaftsmagazin
    1275.0h  0.78% Wissensmagazin
    1245.2h  0.76% Musikmagazin
    1217.8h  0.75% Quiz
    1122.8h  0.69% Sportmagazin
    1120.4h  0.69% Gesundheitsmagazin
    1114.2h  0.68% Telenovela
    1110.6h  0.68% Dramaserie
