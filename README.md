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

**101** channels, **755,371.1** hours playtime between **2023-01-17** and **2024-03-14**


### playtime per genre (top 30)

    49167.4h 6.51% Nachrichten
    36280.7h 4.80% Verkaufsshow
    30773.7h 4.07% Krimiserie
    26185.7h 3.47% Werbesendung
    24093.3h 3.19% Dokureihe
    22830.7h 3.02% Dokusoap
    21947.9h 2.91% Regionalmagazin
    19489.3h 2.58% Dokumentation
    19374.5h 2.56% *unknown*
    13957.1h 1.85% Zeichentrickserie
    13738.9h 1.82% Infomercial
    13343.8h 1.77% Animationsserie
    11466.8h 1.52% Comedyserie
    10723.1h 1.42% Morgenmagazin
    10284.4h 1.36% Magazin
    10201.5h 1.35% Religionsmagazin
    10061.0h 1.33% Talkshow
    7446.0h  0.99% E-Sport
    7137.9h  0.94% Programmende
    7096.1h  0.94% Sitcom
    6721.8h  0.89% Börsenmagazin
    6710.5h  0.89% Wetterbericht
    6415.9h  0.85% Quiz
    6381.1h  0.84% Komödie
    5646.0h  0.75% Wissensmagazin
    5478.8h  0.73% Realityshow
    5465.9h  0.72% Politikmagazin
    5462.9h  0.72% Wirtschaftsmagazin
    5401.2h  0.72% Telenovela
    5153.6h  0.68% Musikmagazin
