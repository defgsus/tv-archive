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

**96** channels, **48,331.1** hours playtime between **2023-01-17** and **2023-02-12**


### playtime per genre (top 30)

    3368.8h 6.97% Nachrichten
    2504.2h 5.18% Verkaufsshow
    2040.1h 4.22% Krimiserie
    1692.3h 3.50% Dokusoap
    1632.8h 3.38% Werbesendung
    1454.5h 3.01% Dokureihe
    1396.1h 2.89% Regionalmagazin
    1235.6h 2.56% Dokumentation
    1228.3h 2.54% *unknown*
    924.8h  1.91% Zeichentrickserie
    899.9h  1.86% Infomercial
    874.6h  1.81% Animationsserie
    803.8h  1.66% Comedyserie
    681.2h  1.41% Morgenmagazin
    635.6h  1.32% Programmende
    628.7h  1.30% Talkshow
    627.3h  1.30% Religionsmagazin
    555.2h  1.15% Magazin
    509.3h  1.05% E-Sport
    454.0h  0.94% Sitcom
    419.1h  0.87% Wetterbericht
    409.4h  0.85% Börsenmagazin
    403.1h  0.83% Wirtschaftsmagazin
    381.7h  0.79% Wissensmagazin
    376.0h  0.78% Quiz
    364.6h  0.75% Dramaserie
    359.9h  0.74% Musikmagazin
    347.2h  0.72% Gesundheitsmagazin
    344.3h  0.71% Telenovela
    327.1h  0.68% Wirtschaftstalk
