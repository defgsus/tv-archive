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

**96** channels, **22,823.6** hours playtime between **2023-01-17** and **2023-01-29**


### playtime per genre (top 30)

    1608.7h 7.05% Nachrichten
    1237.1h 5.42% Verkaufsshow
    952.3h  4.17% Krimiserie
    784.8h  3.44% Dokusoap
    738.4h  3.24% Werbesendung
    695.7h  3.05% Dokureihe
    668.4h  2.93% Regionalmagazin
    593.1h  2.60% Dokumentation
    581.2h  2.55% *unknown*
    448.0h  1.96% Infomercial
    443.6h  1.94% Zeichentrickserie
    394.6h  1.73% Animationsserie
    386.0h  1.69% Comedyserie
    308.6h  1.35% Morgenmagazin
    299.3h  1.31% Talkshow
    287.2h  1.26% Religionsmagazin
    283.0h  1.24% Magazin
    266.4h  1.17% Programmende
    250.8h  1.10% E-Sport
    208.7h  0.91% Sitcom
    195.3h  0.86% Wirtschaftsmagazin
    189.4h  0.83% Wetterbericht
    181.4h  0.80% Börsenmagazin
    180.4h  0.79% Dramaserie
    179.8h  0.79% Tennis
    179.5h  0.79% Wissensmagazin
    176.9h  0.77% Quiz
    167.6h  0.73% Realityshow
    164.9h  0.72% Gesundheitsmagazin
    164.5h  0.72% Musikmagazin
