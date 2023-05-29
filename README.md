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

**96** channels, **240,730.1** hours playtime between **2023-01-17** and **2023-05-30**


### playtime per genre (top 30)

    16068.6h 6.67% Nachrichten
    11640.7h 4.84% Verkaufsshow
    9660.3h  4.01% Krimiserie
    8003.2h  3.32% Werbesendung
    7844.4h  3.26% Dokureihe
    7175.8h  2.98% Dokusoap
    6856.9h  2.85% Regionalmagazin
    6167.5h  2.56% Dokumentation
    5966.1h  2.48% *unknown*
    4509.5h  1.87% Zeichentrickserie
    4404.7h  1.83% Infomercial
    4320.9h  1.79% Animationsserie
    3999.2h  1.66% Comedyserie
    3305.2h  1.37% Morgenmagazin
    3169.1h  1.32% Programmende
    3162.6h  1.31% Talkshow
    3157.8h  1.31% Religionsmagazin
    2751.9h  1.14% Magazin
    2407.5h  1.00% E-Sport
    2256.6h  0.94% Sitcom
    2191.3h  0.91% Börsenmagazin
    2187.9h  0.91% Wetterbericht
    1887.0h  0.78% Wirtschaftsmagazin
    1862.7h  0.77% Wissensmagazin
    1861.7h  0.77% Musikmagazin
    1860.4h  0.77% Quiz
    1754.4h  0.73% Komödie
    1681.8h  0.70% Telenovela
    1673.9h  0.70% Sportmagazin
    1599.1h  0.66% Gesundheitsmagazin
