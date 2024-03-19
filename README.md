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

**101** channels, **765,851.8** hours playtime between **2023-01-17** and **2024-03-20**


### playtime per genre (top 30)

    49854.2h 6.51% Nachrichten
    36774.6h 4.80% Verkaufsshow
    31229.7h 4.08% Krimiserie
    26581.7h 3.47% Werbesendung
    24367.7h 3.18% Dokureihe
    23145.2h 3.02% Dokusoap
    22257.0h 2.91% Regionalmagazin
    19775.1h 2.58% Dokumentation
    19650.7h 2.57% *unknown*
    14133.6h 1.85% Zeichentrickserie
    13935.4h 1.82% Infomercial
    13563.3h 1.77% Animationsserie
    11624.5h 1.52% Comedyserie
    10867.7h 1.42% Morgenmagazin
    10451.0h 1.36% Magazin
    10357.3h 1.35% Religionsmagazin
    10210.0h 1.33% Talkshow
    7538.9h  0.98% E-Sport
    7220.0h  0.94% Programmende
    7175.7h  0.94% Sitcom
    6807.7h  0.89% Börsenmagazin
    6803.1h  0.89% Wetterbericht
    6527.2h  0.85% Quiz
    6444.4h  0.84% Komödie
    5719.1h  0.75% Wissensmagazin
    5559.9h  0.73% Politikmagazin
    5538.4h  0.72% Realityshow
    5525.3h  0.72% Wirtschaftsmagazin
    5478.1h  0.72% Telenovela
    5210.8h  0.68% Musikmagazin
