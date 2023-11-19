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

**97** channels, **552,447.2** hours playtime between **2023-01-17** and **2023-11-20**


### playtime per genre (top 30)

    36330.6h 6.58% Nachrichten
    26398.6h 4.78% Verkaufsshow
    22266.8h 4.03% Krimiserie
    18749.8h 3.39% Werbesendung
    18039.5h 3.27% Dokureihe
    16720.8h 3.03% Dokusoap
    15941.2h 2.89% Regionalmagazin
    14095.6h 2.55% Dokumentation
    13445.7h 2.43% *unknown*
    10244.2h 1.85% Zeichentrickserie
    10070.3h 1.82% Infomercial
    9851.6h  1.78% Animationsserie
    8649.6h  1.57% Comedyserie
    7844.7h  1.42% Morgenmagazin
    7467.6h  1.35% Religionsmagazin
    7388.6h  1.34% Talkshow
    7049.1h  1.28% Magazin
    5568.7h  1.01% Programmende
    5401.8h  0.98% E-Sport
    5296.2h  0.96% Sitcom
    5072.4h  0.92% Wetterbericht
    5007.6h  0.91% Börsenmagazin
    4602.3h  0.83% Quiz
    4325.5h  0.78% Komödie
    4190.8h  0.76% Wissensmagazin
    4143.6h  0.75% Wirtschaftsmagazin
    4077.7h  0.74% Musikmagazin
    3978.2h  0.72% Telenovela
    3856.5h  0.70% Politikmagazin
    3809.0h  0.69% Realityshow
