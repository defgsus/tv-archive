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

**96** channels, **335,700.0** hours playtime between **2023-01-17** and **2023-07-22**


### playtime per genre (top 30)

    22355.5h 6.66% Nachrichten
    16049.8h 4.78% Verkaufsshow
    13487.3h 4.02% Krimiserie
    11257.8h 3.35% Werbesendung
    10950.5h 3.26% Dokureihe
    10170.7h 3.03% Dokusoap
    9646.8h  2.87% Regionalmagazin
    8444.2h  2.52% Dokumentation
    8192.6h  2.44% *unknown*
    6381.7h  1.90% Zeichentrickserie
    6134.8h  1.83% Infomercial
    5921.4h  1.76% Animationsserie
    5561.2h  1.66% Comedyserie
    4725.1h  1.41% Morgenmagazin
    4451.9h  1.33% Talkshow
    4437.3h  1.32% Religionsmagazin
    3999.1h  1.19% Magazin
    3899.2h  1.16% Programmende
    3325.8h  0.99% E-Sport
    3184.9h  0.95% Sitcom
    3139.6h  0.94% Wetterbericht
    3030.2h  0.90% Börsenmagazin
    2680.3h  0.80% Quiz
    2628.8h  0.78% Musikmagazin
    2604.0h  0.78% Wirtschaftsmagazin
    2560.6h  0.76% Wissensmagazin
    2536.4h  0.76% Komödie
    2332.8h  0.69% Telenovela
    2214.8h  0.66% Sportmagazin
    2144.0h  0.64% Dramaserie
