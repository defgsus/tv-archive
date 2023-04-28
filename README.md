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

**96** channels, **184,861.0** hours playtime between **2023-01-17** and **2023-04-29**


### playtime per genre (top 30)

    12614.8h 6.82% Nachrichten
    9115.5h  4.93% Verkaufsshow
    7575.1h  4.10% Krimiserie
    6150.8h  3.33% Werbesendung
    5932.2h  3.21% Dokureihe
    5495.2h  2.97% Dokusoap
    5376.4h  2.91% Regionalmagazin
    4634.6h  2.51% Dokumentation
    4462.6h  2.41% *unknown*
    3411.7h  1.85% Zeichentrickserie
    3388.3h  1.83% Infomercial
    3382.2h  1.83% Animationsserie
    3085.2h  1.67% Comedyserie
    2593.8h  1.40% Morgenmagazin
    2547.2h  1.38% Programmende
    2421.2h  1.31% Talkshow
    2400.6h  1.30% Religionsmagazin
    2042.0h  1.10% Magazin
    1869.3h  1.01% E-Sport
    1747.2h  0.95% Sitcom
    1687.5h  0.91% Börsenmagazin
    1672.3h  0.90% Wetterbericht
    1479.8h  0.80% Wirtschaftsmagazin
    1450.9h  0.78% Wissensmagazin
    1430.3h  0.77% Quiz
    1415.3h  0.77% Musikmagazin
    1315.5h  0.71% Telenovela
    1282.8h  0.69% Gesundheitsmagazin
    1268.5h  0.69% Sportmagazin
    1257.0h  0.68% Dramaserie
