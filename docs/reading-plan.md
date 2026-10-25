# Ścieżka nauki

Plan sześciu etapów, orientacyjnie po tygodniu każdy. Wszystkie odnośniki prowadzą do [katalogu publikacji](../publications/BIBLIOGRAPHY.md), który zawiera źródła, stan dostępu i lokalizacje plików. Etapy można wydłużyć zależnie od znajomości rachunku prawdopodobieństwa i algebry liniowej.

| Etap | Lektura | Ćwiczenie i rezultat |
| --- | --- | --- |
| 1. Proces skokowy | [Gillespie](../publications/BIBLIOGRAPHY.md#gillespie), [van Kampen](../publications/BIBLIOGRAPHY.md#stochastic-book) jeśli masz dostęp | Wyprowadź Q i rozwiązanie układu dwóch stanów; uruchom testy i porównaj symulację z propagacją |
| 2. Estymacja i identyfikowalność | [Neural MJP](../publications/BIBLIOGRAPHY.md#neural-mjp), [Foundation MJP](../publications/BIBLIOGRAPHY.md#foundation-mjp), [Ljung](../publications/BIBLIOGRAPHY.md#sysid-book) jeśli dostępny | Wyprowadź MLE i składnik survival; pokaż, co psuje pominięcie końcowego odcinka bez skoku |
| 3. Reprezentacje i relacje | [PRAGMA](../publications/BIBLIOGRAPHY.md#pragma), [Hamilton](../publications/BIBLIOGRAPHY.md#graph-book), [NRI](../publications/BIBLIOGRAPHY.md#nri), [TGN](../publications/BIBLIOGRAPHY.md#tgn) | Opisz kontrakt tokenu i stanu; rozdziel embedding od intensywności; zaprojektuj test permutacji ID |
| 4. Transfer i procesy | [MiNT](../publications/BIBLIOGRAPHY.md#mint), [teoria transferu](../publications/BIBLIOGRAPHY.md#graph-transfer), [model in-context dla procesów](../publications/BIBLIOGRAPHY.md#process-incontext) | Zapisz podział po systemach, baseline'y i ablacjami odróżnij pamiętanie encji od transferu |
| 5. Ścieżki i cykle | [Period folding](../publications/BIBLIOGRAPHY.md#period-folding), [Structural Path Analysis](../publications/BIBLIOGRAPHY.md#spa), [Trajectory Balance](../publications/BIBLIOGRAPHY.md#trajectory-balance) | Zestaw definicje trajektorii, wag i reszt; wyjaśnij, dlaczego uniformizacja, TTA i GFlowNet nie są tym samym |
| 6. Zastosowanie i przyczynowość | [Production Networks: A Primer](../publications/BIBLIOGRAPHY.md#production-primer), [Leontief Meets Markov](../publications/BIBLIOGRAPHY.md#leontief-markov), [What If](../publications/BIBLIOGRAPHY.md#causal-book), [Forecasting](../publications/BIBLIOGRAPHY.md#forecasting-book) | Przygotuj jeden model obserwacji gospodarczej, schemat walidacji czasowej i listę założeń potrzebnych do interpretacji interwencji |

Po każdym etapie zapisz: pytanie badawcze, definicje, założenia, równanie celu, dane, baseline, ograniczenia oraz jeden mały przykład liczbowy. Własne notatki można dodawać jako Markdown do `docs/`; pełne publikacje pozostają w ignorowanym `publications/files/`.
