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

**96** channels, **348,252.8** hours playtime between **2023-01-17** and **2023-07-29**


### playtime per genre (top 30)

    23157.1h 6.65% Nachrichten
    16622.8h 4.77% Verkaufsshow
    14018.6h 4.03% Krimiserie
    11696.3h 3.36% Werbesendung
    11380.0h 3.27% Dokureihe
    10540.5h 3.03% Dokusoap
    10016.0h 2.88% Regionalmagazin
    8760.6h  2.52% Dokumentation
    8473.2h  2.43% *unknown*
    6600.2h  1.90% Zeichentrickserie
    6370.5h  1.83% Infomercial
    6147.3h  1.77% Animationsserie
    5752.8h  1.65% Comedyserie
    4900.8h  1.41% Morgenmagazin
    4610.1h  1.32% Religionsmagazin
    4602.4h  1.32% Talkshow
    4166.8h  1.20% Magazin
    3996.3h  1.15% Programmende
    3440.8h  0.99% E-Sport
    3291.1h  0.95% Sitcom
    3265.8h  0.94% Wetterbericht
    3155.8h  0.91% Börsenmagazin
    2783.0h  0.80% Quiz
    2723.6h  0.78% Musikmagazin
    2692.9h  0.77% Wirtschaftsmagazin
    2661.2h  0.76% Komödie
    2636.6h  0.76% Wissensmagazin
    2408.5h  0.69% Telenovela
    2284.4h  0.66% Sportmagazin
    2224.8h  0.64% Reportagereihe
