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

**96** channels, **258,674.8** hours playtime between **2023-01-17** and **2023-06-09**


### playtime per genre (top 30)

    17276.9h 6.68% Nachrichten
    12474.9h 4.82% Verkaufsshow
    10356.2h 4.00% Krimiserie
    8588.4h  3.32% Werbesendung
    8434.5h  3.26% Dokureihe
    7752.2h  3.00% Dokusoap
    7392.6h  2.86% Regionalmagazin
    6620.9h  2.56% Dokumentation
    6448.5h  2.49% *unknown*
    4880.0h  1.89% Zeichentrickserie
    4736.9h  1.83% Infomercial
    4602.9h  1.78% Animationsserie
    4309.3h  1.67% Comedyserie
    3594.6h  1.39% Morgenmagazin
    3396.2h  1.31% Talkshow
    3389.9h  1.31% Religionsmagazin
    3306.9h  1.28% Programmende
    3019.9h  1.17% Magazin
    2589.9h  1.00% E-Sport
    2434.1h  0.94% Sitcom
    2367.2h  0.92% Wetterbericht
    2326.6h  0.90% Börsenmagazin
    2037.6h  0.79% Wirtschaftsmagazin
    2016.0h  0.78% Musikmagazin
    2012.5h  0.78% Quiz
    1998.3h  0.77% Wissensmagazin
    1918.1h  0.74% Komödie
    1840.2h  0.71% Telenovela
    1767.0h  0.68% Sportmagazin
    1692.9h  0.65% Gesundheitsmagazin
