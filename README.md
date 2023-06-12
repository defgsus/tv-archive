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

**96** channels, **265,845.3** hours playtime between **2023-01-17** and **2023-06-13**


### playtime per genre (top 30)

    17697.8h 6.66% Nachrichten
    12816.4h 4.82% Verkaufsshow
    10617.9h 3.99% Krimiserie
    8837.7h  3.32% Werbesendung
    8687.3h  3.27% Dokureihe
    7968.8h  3.00% Dokusoap
    7570.6h  2.85% Regionalmagazin
    6807.8h  2.56% Dokumentation
    6650.8h  2.50% *unknown*
    5034.9h  1.89% Zeichentrickserie
    4869.9h  1.83% Infomercial
    4720.4h  1.78% Animationsserie
    4409.3h  1.66% Comedyserie
    3674.0h  1.38% Morgenmagazin
    3504.8h  1.32% Talkshow
    3495.2h  1.31% Religionsmagazin
    3362.0h  1.26% Programmende
    3091.7h  1.16% Magazin
    2657.3h  1.00% E-Sport
    2499.7h  0.94% Sitcom
    2434.7h  0.92% Wetterbericht
    2394.6h  0.90% Börsenmagazin
    2090.0h  0.79% Wirtschaftsmagazin
    2073.8h  0.78% Quiz
    2065.2h  0.78% Musikmagazin
    2050.5h  0.77% Wissensmagazin
    1982.5h  0.75% Komödie
    1877.2h  0.71% Telenovela
    1811.7h  0.68% Sportmagazin
    1729.2h  0.65% Gesundheitsmagazin
