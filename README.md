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

**97** channels, **421,682.8** hours playtime between **2023-01-17** and **2023-09-08**


### playtime per genre (top 30)

    27863.3h 6.61% Nachrichten
    19975.5h 4.74% Verkaufsshow
    17110.0h 4.06% Krimiserie
    14231.5h 3.37% Werbesendung
    13898.7h 3.30% Dokureihe
    12822.0h 3.04% Dokusoap
    12156.5h 2.88% Regionalmagazin
    10644.0h 2.52% Dokumentation
    10072.8h 2.39% *unknown*
    7962.1h  1.89% Zeichentrickserie
    7698.5h  1.83% Infomercial
    7466.9h  1.77% Animationsserie
    6856.9h  1.63% Comedyserie
    5966.5h  1.41% Morgenmagazin
    5631.5h  1.34% Religionsmagazin
    5554.1h  1.32% Talkshow
    5270.1h  1.25% Magazin
    4565.3h  1.08% Programmende
    4161.6h  0.99% E-Sport
    3987.6h  0.95% Wetterbericht
    3958.6h  0.94% Sitcom
    3809.9h  0.90% Börsenmagazin
    3468.2h  0.82% Quiz
    3334.6h  0.79% Musikmagazin
    3285.5h  0.78% Komödie
    3204.2h  0.76% Wirtschaftsmagazin
    3151.0h  0.75% Wissensmagazin
    2975.8h  0.71% Telenovela
    2777.0h  0.66% Reportagereihe
    2742.9h  0.65% Politikmagazin
