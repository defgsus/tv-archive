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

**96** channels, **264,081.4** hours playtime between **2023-01-17** and **2023-06-12**


### playtime per genre (top 30)

    17567.0h 6.65% Nachrichten
    12734.3h 4.82% Verkaufsshow
    10557.6h 4.00% Krimiserie
    8777.0h  3.32% Werbesendung
    8641.6h  3.27% Dokureihe
    7907.4h  2.99% Dokusoap
    7508.3h  2.84% Regionalmagazin
    6768.4h  2.56% Dokumentation
    6601.0h  2.50% *unknown*
    4996.9h  1.89% Zeichentrickserie
    4837.4h  1.83% Infomercial
    4692.0h  1.78% Animationsserie
    4372.4h  1.66% Comedyserie
    3639.2h  1.38% Morgenmagazin
    3483.9h  1.32% Talkshow
    3477.5h  1.32% Religionsmagazin
    3348.7h  1.27% Programmende
    3076.7h  1.17% Magazin
    2646.3h  1.00% E-Sport
    2480.1h  0.94% Sitcom
    2416.4h  0.92% Wetterbericht
    2369.3h  0.90% Börsenmagazin
    2072.8h  0.78% Wirtschaftsmagazin
    2055.6h  0.78% Musikmagazin
    2043.0h  0.77% Quiz
    2037.7h  0.77% Wissensmagazin
    1991.1h  0.75% Komödie
    1859.6h  0.70% Telenovela
    1802.7h  0.68% Sportmagazin
    1719.2h  0.65% Gesundheitsmagazin
