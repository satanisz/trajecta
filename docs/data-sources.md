# Mapa potencjalnych źródeł danych

To osobna lista serwisów i standardów wskazanych w rozmowie, a nie lista pobranych publikacji. Repozytorium nie zawiera jeszcze konektorów ani pobranych zbiorów. Adresy są punktami startowymi; przed integracją trzeba sprawdzić aktualny zakres danych, warunki dostępu, jednostki i historię rewizji.

| Źródło | Potencjalna rola | Kluczowe pytanie przy integracji |
| --- | --- | --- |
| [OCEL 2.0](https://www.ocel-standard.org/) | Logi zdarzeń z wieloma obiektami | Jak zdefiniować stan i czas dostępności zdarzenia? |
| [Stanford Supply Chains](https://snap.stanford.edu/supplychains/) | Sieci produkcyjne i punkt odniesienia dla grafów | Jakie relacje są obserwowane, a jakie rekonstruowane? |
| [CEPII BACI](https://www.cepii.fr/CEPII/en/bdd_modele/bdd_modele_item.asp?id=37) | Handel kraj–produkt | Jak zachować wersje klasyfikacji towarów i rewizje? |
| [OECD ICIO](https://www.oecd.org/en/data/datasets/inter-country-input-output-tables.html) | Powiązania input-output między gospodarkami | Jakie agregacje sektorów i lata są porównywalne? |
| [BIS CBS](https://data.bis.org/topics/CBS) | Skonsolidowane ekspozycje bankowe | Czy kierunek ekspozycji i konsolidacja odpowiadają modelowanemu przepływowi? |
| [IMF PortWatch](https://portwatch.imf.org/) | Ruch morski i przybliżenia aktywności handlowej | Jaka jest relacja sygnału AIS do wartości i wolumenu handlu? |
| [MarineCadastre](https://marinecadastre.gov/) | Dane AIS i geografia morska | Jakie są braki pokrycia i ograniczenia przestrzenne? |
| [UN Comtrade](https://comtradeplus.un.org/) | Oficjalne statystyki handlu | Jak obsłużyć opóźnienia raportowania i asymetrie partnerów? |
| [Eurostat Comext](https://ec.europa.eu/eurostat/web/international-trade-in-goods/database) | Szczegółowy handel towarowy | Jak przechowywać korekty i zmiany nomenklatur? |
| [JODI](https://www.jodidata.org/) | Dane o ropie i gazie | Jak odróżnić brak danych od zera oraz uzgodnić jednostki? |
| [FRED](https://fred.stlouisfed.org/) / [ALFRED](https://alfred.stlouisfed.org/) | Szeregi makro i ich historyczne wersje | Czy model widzi wyłącznie wersję dostępną w chwili prognozy? |
| [World Bank Commodity Markets](https://www.worldbank.org/en/research/commodity-markets) | Ceny surowców | Czy ceny są nominalne/realne i w jakiej walucie? |
| [IATA](https://www.iata.org/) | Kontekst i statystyki transportu lotniczego | Które konkretne zbiory są dostępne i na jakich warunkach? |
| [DCSA](https://dcsa.org/) | Standardy zdarzeń transportu kontenerowego | Czy istnieje źródło rzeczywistych zdarzeń zgodne ze standardem? |

Proponowany lokalny układ danych: `data/raw/<source>/<release>/`, `data/processed/<schema-version>/` i manifest zawierający URL, datę pobrania, datę udostępnienia, jednostki oraz hash. Cały `data/` jest ignorowany. Sam standard lub strona organizacji nie jest jeszcze zbiorem treningowym.
