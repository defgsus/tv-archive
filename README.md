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

**96** channels, **111,917.8** hours playtime between **2023-01-17** and **2023-03-19**


### playtime per genre (top 30)

    7866.6h 7.03% Nachrichten
    5618.0h 5.02% Verkaufsshow
    4689.7h 4.19% Krimiserie
    3790.4h 3.39% Werbesendung
    3570.2h 3.19% Dokusoap
    3404.7h 3.04% Dokureihe
    3291.8h 2.94% Regionalmagazin
    2748.8h 2.46% Dokumentation
    2631.5h 2.35% *unknown*
    2141.4h 1.91% Animationsserie
    2057.4h 1.84% Infomercial
    2018.3h 1.80% Zeichentrickserie
    1822.2h 1.63% Comedyserie
    1595.8h 1.43% Morgenmagazin
    1536.6h 1.37% Programmende
    1479.3h 1.32% Talkshow
    1454.1h 1.30% Religionsmagazin
    1171.8h 1.05% Magazin
    1153.2h 1.03% E-Sport
    1072.0h 0.96% Sitcom
    1028.4h 0.92% Börsenmagazin
    995.9h  0.89% Wetterbericht
    913.8h  0.82% Wirtschaftsmagazin
    878.6h  0.79% Wissensmagazin
    836.9h  0.75% Quiz
    829.3h  0.74% Musikmagazin
    813.9h  0.73% Dramaserie
    781.5h  0.70% Telenovela
    777.2h  0.69% Gesundheitsmagazin
    743.5h  0.66% Sportmagazin
