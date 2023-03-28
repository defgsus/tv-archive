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

**96** channels, **128,213.3** hours playtime between **2023-01-17** and **2023-03-29**


### playtime per genre (top 30)

    8981.4h 7.01% Nachrichten
    6411.5h 5.00% Verkaufsshow
    5348.0h 4.17% Krimiserie
    4329.2h 3.38% Werbesendung
    4000.0h 3.12% Dokureihe
    3988.1h 3.11% Dokusoap
    3768.4h 2.94% Regionalmagazin
    3165.2h 2.47% Dokumentation
    2951.8h 2.30% *unknown*
    2435.6h 1.90% Animationsserie
    2361.2h 1.84% Infomercial
    2342.2h 1.83% Zeichentrickserie
    2097.6h 1.64% Comedyserie
    1825.2h 1.42% Morgenmagazin
    1766.2h 1.38% Programmende
    1704.5h 1.33% Talkshow
    1666.1h 1.30% Religionsmagazin
    1346.2h 1.05% Magazin
    1326.5h 1.03% E-Sport
    1221.2h 0.95% Sitcom
    1207.2h 0.94% Börsenmagazin
    1149.3h 0.90% Wetterbericht
    1048.5h 0.82% Wirtschaftsmagazin
    1002.2h 0.78% Wissensmagazin
    972.6h  0.76% Quiz
    970.6h  0.76% Musikmagazin
    925.7h  0.72% Dramaserie
    900.5h  0.70% Telenovela
    882.6h  0.69% Sportmagazin
    881.8h  0.69% Gesundheitsmagazin
