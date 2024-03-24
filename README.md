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

**101** channels, **774,671.9** hours playtime between **2023-01-17** and **2024-03-25**


### playtime per genre (top 30)

    50409.4h 6.51% Nachrichten
    37222.6h 4.80% Verkaufsshow
    31585.2h 4.08% Krimiserie
    26939.7h 3.48% Werbesendung
    24645.4h 3.18% Dokureihe
    23382.7h 3.02% Dokusoap
    22504.3h 2.91% Regionalmagazin
    19985.0h 2.58% Dokumentation
    19886.4h 2.57% *unknown*
    14274.2h 1.84% Zeichentrickserie
    14096.2h 1.82% Infomercial
    13742.3h 1.77% Animationsserie
    11746.5h 1.52% Comedyserie
    10980.3h 1.42% Morgenmagazin
    10582.5h 1.37% Magazin
    10476.9h 1.35% Religionsmagazin
    10355.2h 1.34% Talkshow
    7630.1h  0.98% E-Sport
    7289.8h  0.94% Programmende
    7236.3h  0.93% Sitcom
    6882.8h  0.89% Börsenmagazin
    6874.6h  0.89% Wetterbericht
    6608.6h  0.85% Quiz
    6516.9h  0.84% Komödie
    5788.8h  0.75% Wissensmagazin
    5626.8h  0.73% Politikmagazin
    5588.3h  0.72% Realityshow
    5583.7h  0.72% Wirtschaftsmagazin
    5537.3h  0.71% Telenovela
    5256.0h  0.68% Musikmagazin
