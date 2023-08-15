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

**96** channels, **380,508.8** hours playtime between **2023-01-17** and **2023-08-16**


### playtime per genre (top 30)

    25176.5h 6.62% Nachrichten
    17982.9h 4.73% Verkaufsshow
    15406.0h 4.05% Krimiserie
    12815.8h 3.37% Werbesendung
    12558.2h 3.30% Dokureihe
    11496.7h 3.02% Dokusoap
    10902.2h 2.87% Regionalmagazin
    9605.4h  2.52% Dokumentation
    9237.2h  2.43% *unknown*
    7181.2h  1.89% Zeichentrickserie
    6950.4h  1.83% Infomercial
    6716.8h  1.77% Animationsserie
    6227.2h  1.64% Comedyserie
    5343.1h  1.40% Morgenmagazin
    5060.3h  1.33% Religionsmagazin
    5008.3h  1.32% Talkshow
    4675.6h  1.23% Magazin
    4235.6h  1.11% Programmende
    3777.3h  0.99% E-Sport
    3591.8h  0.94% Wetterbericht
    3565.5h  0.94% Sitcom
    3462.4h  0.91% Börsenmagazin
    3056.3h  0.80% Quiz
    2998.1h  0.79% Musikmagazin
    2952.9h  0.78% Komödie
    2909.6h  0.76% Wirtschaftsmagazin
    2856.0h  0.75% Wissensmagazin
    2640.7h  0.69% Telenovela
    2480.8h  0.65% Reportagereihe
    2456.8h  0.65% Sportmagazin
