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

**96** channels, **135,496.9** hours playtime between **2023-01-17** and **2023-04-02**


### playtime per genre (top 30)

    9490.9h 7.00% Nachrichten
    6759.2h 4.99% Verkaufsshow
    5652.5h 4.17% Krimiserie
    4581.5h 3.38% Werbesendung
    4265.8h 3.15% Dokureihe
    4173.5h 3.08% Dokusoap
    3986.7h 2.94% Regionalmagazin
    3352.4h 2.47% Dokumentation
    3088.4h 2.28% *unknown*
    2563.6h 1.89% Animationsserie
    2499.0h 1.84% Infomercial
    2481.6h 1.83% Zeichentrickserie
    2226.0h 1.64% Comedyserie
    1934.5h 1.43% Morgenmagazin
    1885.1h 1.39% Programmende
    1798.5h 1.33% Talkshow
    1754.7h 1.30% Religionsmagazin
    1429.2h 1.05% Magazin
    1409.2h 1.04% E-Sport
    1298.5h 0.96% Sitcom
    1272.7h 0.94% Börsenmagazin
    1213.5h 0.90% Wetterbericht
    1101.8h 0.81% Wirtschaftsmagazin
    1061.3h 0.78% Wissensmagazin
    1029.7h 0.76% Quiz
    1021.3h 0.75% Musikmagazin
    970.9h  0.72% Dramaserie
    954.1h  0.70% Telenovela
    934.1h  0.69% Gesundheitsmagazin
    931.0h  0.69% Sportmagazin
