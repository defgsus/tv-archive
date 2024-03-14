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

**101** channels, **757,134.3** hours playtime between **2023-01-17** and **2024-03-15**


### playtime per genre (top 30)

    49300.5h 6.51% Nachrichten
    36372.0h 4.80% Verkaufsshow
    30873.1h 4.08% Krimiserie
    26248.0h 3.47% Werbesendung
    24117.0h 3.19% Dokureihe
    22881.0h 3.02% Dokusoap
    22009.8h 2.91% Regionalmagazin
    19532.8h 2.58% Dokumentation
    19417.7h 2.56% *unknown*
    13984.5h 1.85% Zeichentrickserie
    13771.2h 1.82% Infomercial
    13381.9h 1.77% Animationsserie
    11495.6h 1.52% Comedyserie
    10755.5h 1.42% Morgenmagazin
    10320.4h 1.36% Magazin
    10220.9h 1.35% Religionsmagazin
    10078.9h 1.33% Talkshow
    7471.6h  0.99% E-Sport
    7151.9h  0.94% Programmende
    7110.1h  0.94% Sitcom
    6732.1h  0.89% Börsenmagazin
    6726.4h  0.89% Wetterbericht
    6439.7h  0.85% Quiz
    6387.5h  0.84% Komödie
    5656.2h  0.75% Wissensmagazin
    5488.7h  0.72% Realityshow
    5482.3h  0.72% Politikmagazin
    5477.7h  0.72% Wirtschaftsmagazin
    5421.1h  0.72% Telenovela
    5160.9h  0.68% Musikmagazin
