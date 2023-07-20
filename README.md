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

**96** channels, **333,910.3** hours playtime between **2023-01-17** and **2023-07-21**


### playtime per genre (top 30)

    22234.0h 6.66% Nachrichten
    15969.1h 4.78% Verkaufsshow
    13417.6h 4.02% Krimiserie
    11198.9h 3.35% Werbesendung
    10893.5h 3.26% Dokureihe
    10113.8h 3.03% Dokusoap
    9583.2h  2.87% Regionalmagazin
    8403.2h  2.52% Dokumentation
    8152.8h  2.44% *unknown*
    6352.7h  1.90% Zeichentrickserie
    6102.6h  1.83% Infomercial
    5887.7h  1.76% Animationsserie
    5526.4h  1.66% Comedyserie
    4692.8h  1.41% Morgenmagazin
    4420.3h  1.32% Talkshow
    4417.2h  1.32% Religionsmagazin
    3972.8h  1.19% Magazin
    3886.2h  1.16% Programmende
    3309.2h  0.99% E-Sport
    3169.7h  0.95% Sitcom
    3120.7h  0.93% Wetterbericht
    3002.6h  0.90% Börsenmagazin
    2664.8h  0.80% Quiz
    2616.5h  0.78% Musikmagazin
    2588.1h  0.78% Wirtschaftsmagazin
    2553.4h  0.76% Wissensmagazin
    2524.8h  0.76% Komödie
    2319.2h  0.69% Telenovela
    2207.3h  0.66% Sportmagazin
    2126.7h  0.64% Politikmagazin
