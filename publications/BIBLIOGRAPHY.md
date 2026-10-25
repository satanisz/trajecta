# Bibliografia TRAJECTA

Źródło: czat „Pragma i Master Equation”. Audyt i lokalny stan plików: **2026-10-25**.

**49 pozycji: 39 PDF-ów, 2 książki jako tekst HTML, 8 braków pełnego tekstu.**

Pliki publikacji są ignorowane przez Git. Poniższy stan opisuje bibliotekę lokalną w dniu audytu; samo sklonowanie repozytorium ich nie pobiera.

Krótkie opisy wskazują rolę materiału w projekcie. Nie są recenzją naukową ani potwierdzeniem wyników. Zasady audytu: [README](README.md).

## Brakujące pełne teksty

| ID | Publikacja | Przyczyna |
| --- | --- | --- |
| `tides` | [Disentangling Dynamics: A Compositional Framework for Temporal Graph Foundation Models](https://eic-emerge.eu/resources/publications-details/disentangling-dynamics-a-compositional-framework-for-temporal-graph-foundation-models) | PDF OpenReview zwracał blokadę dostępu/CAPTCHA; zachowano rekord i odnośnik. Brak lokalnego pełnego tekstu. |
| `input-output-book` | [Input-Output Analysis: Foundations and Extensions](https://www.cambridge.org/core/books/inputoutput-analysis/431D85A5E459AB078479852169EA77D7) | Nie znaleziono otwartej pełnej książki; wydawca oferuje dostęp zakupiony lub instytucjonalny. |
| `data-driven-book` | [Data-Driven Science and Engineering](https://www.databookuw.com/) | Nie znaleziono publicznej kopii pełnego tekstu książki. |
| `chaos-book` | [Making Sense of Chaos: A Better Economics for a Better World](https://www.jstor.org/stable/jj.16971561) | Nie znaleziono publicznej kopii pełnego tekstu książki. |
| `stochastic-book` | [Stochastic Processes in Physics and Chemistry](https://www.sciencedirect.com/book/9780444529657/stochastic-processes-in-physics-and-chemistry) | Nie znaleziono publicznej kopii pełnego tekstu książki. |
| `sysid-book` | [System Identification: Theory for the User](https://www.control.isy.liu.se/books/sysid/) | Nie znaleziono publicznej kopii pełnego tekstu książki. |
| `agentic-twins` | [Agentic digital twins: bridging model-based and AI-driven decision-making support for a new era of supply chain and operations management](https://www.tandfonline.com/doi/full/10.1080/00207543.2026.2630277) | Dostęp wydawcy zablokowany; rekord bibliograficzny wskazuje dostęp subskrypcyjny. Nie znaleziono kopii otwartej. |
| `supplier-recommendation` | [Using Knowledge Graph-Enhanced Relational Graph Convolutional Network for Potential Supplier Recommendation](https://www.sciencedirect.com/science/article/pii/S1568494626019836) | Strona wydawcy dostępna bibliograficznie; nie znaleziono publicznego pełnego PDF. |

## Procesy Markowa, Master Equation i trajektorie

<a id="neural-mjp"></a>

### Neural Markov Jump Processes (2023)

ID: `neural-mjp` · [Źródło](https://proceedings.mlr.press/v202/seifner23a.html) · Weryfikacja: `fulltext_title_verified`.

Autorzy: Patrick Seifner; Ramses J Sanchez.

Neuronowa inferencja procesów skokowych; punkt odniesienia dla uczenia intensywności i modelu obserwacji.

Lokalnie: `publications/files/markov-and-master-equation/neural-mjp.pdf` · 30 stron · [Pobrana kopia](https://proceedings.mlr.press/v202/seifner23a/seifner23a.pdf).

SHA-256: `02f9e414495593136beb625e8c987421cff6961c444257c0be9c9a36d51c8f51`.

<a id="foundation-mjp"></a>

### Foundation Inference Models for Markov Jump Processes (2024)

ID: `foundation-mjp` · [Źródło](https://arxiv.org/abs/2406.06419) · Weryfikacja: `fulltext_title_verified`.

Autorzy: Berghaus, David; Cvejoski, Kostadin; Seifner, Patrick; Ojeda, Cesar; Sanchez, Ramses J..

Inferencja generatorów na podstawie zaszumionych obserwacji; istotna dla transferu między przestrzeniami stanów.

Lokalnie: `publications/files/markov-and-master-equation/foundation-mjp.pdf` · 36 stron · [Pobrana kopia](https://arxiv.org/pdf/2406.06419).

SHA-256: `d1409c688a739573feb1ed7e21ee0abd684b5f82947d01945d546c5588592d1e`.

Uwaga: Rok odnosi się do pierwszej publikacji preprintu (2024); pobrano aktualną rewizję arXiv, nie zamrożoną wersję v1.

<a id="trajectory-balance"></a>

### Trajectory balance: Improved credit assignment in GFlowNets (2022)

ID: `trajectory-balance` · [Źródło](https://arxiv.org/abs/2201.13259) · Weryfikacja: `fulltext_title_verified`.

Autorzy: Whitammer, Esmeralda S.; Jain, Moksh; Bengio, Emmanuel; Sun, Chen; Bengio, Yoshua.

Cel uczenia całych trajektorii GFlowNet. Nie jest równoważny ciągłoczasowemu TTA.

Lokalnie: `publications/files/markov-and-master-equation/trajectory-balance.pdf` · 18 stron · [Pobrana kopia](https://arxiv.org/pdf/2201.13259).

SHA-256: `9ec163c22df6f6fa5b4951bb0fbbd2d5f122f0a55d804dabb415d0c51c68ddb5`.

Uwaga: W czacie wskazano pracę z 2022 jako Malkin et al. Katalog zachowuje listę autorów z aktualnego rekordu arXiv i pobranej wersji.

<a id="gflownet-training"></a>

### Towards Understanding and Improving GFlowNet Training (2023)

ID: `gflownet-training` · [Źródło](https://proceedings.mlr.press/v202/shen23a.html) · Weryfikacja: `fulltext_title_verified`.

Autorzy: Max W Shen; Emmanuel Bengio; Ehsan Hajiramezanali; Andreas Loukas; Kyunghyun Cho; Tommaso Biancalani.

Dodatkowa publikacja rzeczywiście podlinkowana w czacie pod etykietą GFlowNets — Trajectory Balance.

Lokalnie: `publications/files/markov-and-master-equation/gflownet-training.pdf` · 20 stron · [Pobrana kopia](https://proceedings.mlr.press/v202/shen23a/shen23a.pdf).

SHA-256: `5d1db8e92a0a8cc78e3b5f2870e891c3ba0a2d1c6d77b9c3461fce706afc7731`.

Uwaga: W czacie podpisane jako GFlowNets — Trajectory Balance (ICML 2023); adres wskazuje Shen et al., nie Malkin et al. 2022. Zachowano obie odrębne prace.

<a id="transformer-dynamics"></a>

### Learning stochastic dynamics and predicting emergent behavior using transformers (2024)

ID: `transformer-dynamics` · [Źródło](https://www.nature.com/articles/s41467-024-45629-w) · Weryfikacja: `fulltext_title_verified`.

Uczenie dynamiki stochastycznej z trajektorii; porównanie z narzucaniem generatora Markowa.

Lokalnie: `publications/files/markov-and-master-equation/transformer-dynamics.pdf` · 12 stron · [Pobrana kopia](https://arxiv.org/pdf/2202.08708).

SHA-256: `4e31a8da13c62d26fe7a7eefdf72bc91f17ba2e4c89bb795b806099b3f602b94`.

Uwaga: Publikacja czasopismowa z 2024; pobrano odpowiadający jej preprint arXiv 2202.08708.

<a id="gillespie"></a>

### Exact Stochastic Simulation of Coupled Chemical Reactions (1977)

ID: `gillespie` · [Źródło](https://pubs.acs.org/doi/10.1021/j100540a008) · Weryfikacja: `fulltext_title_verified`.

Autorzy: Daniel T. Gillespie.

Symulacja realizacji procesu skokowego; referencja do walidacji rozkładu trajektorii.

Lokalnie: `publications/files/markov-and-master-equation/gillespie.pdf` · 22 stron · [Pobrana kopia](https://www.ma.imperial.ac.uk/~nsjones/gillespie_1977.pdf).

SHA-256: `c3358767c5ef2774c8f656f710e3836ced0ad098ba72d5577aa639e5ddecbc0f`.

<a id="neural-jump-sde"></a>

### Neural Jump Stochastic Differential Equations (2019)

ID: `neural-jump-sde` · [Źródło](https://papers.neurips.cc/paper_files/paper/2019/hash/59b1deff341edb0b76ace57820cef237-Abstract.html) · Weryfikacja: `fulltext_title_verified`.

Autorzy: Jia, Junteng; Benson, Austin R..

Ciągła ewolucja stanu połączona z dyskretnymi skokami.

Lokalnie: `publications/files/markov-and-master-equation/neural-jump-sde.pdf` · 12 stron · [Pobrana kopia](https://proceedings.neurips.cc/paper_files/paper/2019/file/59b1deff341edb0b76ace57820cef237-Paper.pdf).

SHA-256: `2c8bc840407e707a7756cace0b7aae34827049f1372251748e88b432b901f25f`.

<a id="period-folding"></a>

### Development of a Trajectory Period Folding Method for Burnup Calculations (2022)

ID: `period-folding` · [Źródło](https://www.mdpi.com/1996-1073/15/6/2245) · Weryfikacja: `fulltext_title_verified`.

Autorzy: Paweł Stanisz; Mikołaj Oettingen; Jerzy Cetnar.

Stanisz–Oettingen–Cetnar: składanie trajektorii kolejnych okresów i kontrola bilansu.

Lokalnie: `publications/files/markov-and-master-equation/period-folding.pdf` · 15 stron · [Pobrana kopia](https://psecommunity.org/wp-content/plugins/wpor/includes/file/2303/LAPSE-2023.14792-1v1.pdf).

SHA-256: `2bff258f52ab1b70a7cd3694173630445a7e8e689c2fc76e7b642474f27f0693`.

Uwaga: Praca Stanisza, Oettingena i Cetnara o period folding w obliczeniach wypalania. Nie utożsamiać z uniformizacją CTMC ani z GFlowNet Trajectory Balance.


## Modele zdarzeń, procesów i grafów czasowych

<a id="pragma"></a>

### PRAGMA: Revolut Foundation Model (2026)

ID: `pragma` · [Źródło](https://arxiv.org/abs/2604.08649) · Weryfikacja: `fulltext_title_verified`.

Autorzy: Ostroukhov, Maxim; Mikhailov, Ruslan; Iashin, Vladimir; Sokolov, Artem; Akshonov, Andrei; Protasov, Vitaly; Goncharov, Andrey; Beloborodov, Dmitrii; Mullin, Vince; Enzmann, Roman Yokunda; Kolovos, Georgios; Renders, Jason; Nesterov, Pavel; Repushko, Anton.

Hierarchiczna reprezentacja zdarzeń key–value–time; punkt odniesienia dla tokenizacji stanów i historii.

Lokalnie: `publications/files/process-and-temporal-models/pragma.pdf` · 20 stron · [Pobrana kopia](https://arxiv.org/pdf/2604.08649).

SHA-256: `22f38367d2fe7e745a4e4d4003f7f523a9c29122dac1d0ff87370dc0703a2df1`.

<a id="dyrep"></a>

### Dyrep: Learning Representations over Dynamic Graphs. (2019)

ID: `dyrep` · [Źródło](https://research.google/pubs/dyrep-learning-representations-over-dynamic-graphs/) · Weryfikacja: `fulltext_title_verified`.

Autorzy: Rakshit Trivedi; Mehrdad Farajtabar; Prasenjeet Biswal; Hongyuan Zha.

Wspólne modelowanie zmian topologii i interakcji przez procesy punktowe.

Lokalnie: `publications/files/process-and-temporal-models/dyrep.pdf` · 25 stron · [Pobrana kopia](https://openreview.net/references/pdf?id=SJiOMX0BE).

SHA-256: `b9e5ee905288feaa1ab72307a9ca9e10f83242098c362b7d27a836ccbe96d4e6`.

<a id="nri"></a>

### Neural Relational Inference for Interacting Systems (2018)

ID: `nri` · [Źródło](https://proceedings.mlr.press/v80/kipf18a.html) · Weryfikacja: `fulltext_title_verified`.

Autorzy: Thomas Kipf; Ethan Fetaya; Kuan-Chieh Wang; Max Welling; Richard Zemel.

Uczenie ukrytych relacji i dynamiki; konkurent dla odzyskiwania grafu z obserwacji.

Lokalnie: `publications/files/process-and-temporal-models/nri.pdf` · 10 stron · [Pobrana kopia](https://proceedings.mlr.press/v80/kipf18a/kipf18a.pdf).

SHA-256: `4638a8b9e66e21cde97ad6b3f801acc2041abff96d7649270a57e6e11ab76ebb`.

<a id="tgn"></a>

### Temporal Graph Networks for Deep Learning on Dynamic Graphs (2020)

ID: `tgn` · [Źródło](https://arxiv.org/abs/2006.10637) · Weryfikacja: `fulltext_title_verified`.

Autorzy: Rossi, Emanuele; Chamberlain, Ben; Frasca, Fabrizio; Eynard, Davide; Monti, Federico; Bronstein, Michael.

Pamięć węzłów i reprezentacja strumienia zdarzeń; baseline grafu temporalnego.

Lokalnie: `publications/files/process-and-temporal-models/tgn.pdf` · 16 stron · [Pobrana kopia](https://arxiv.org/pdf/2006.10637).

SHA-256: `580113858f363b80388bbf7c1b2a42482cfb9b6debdb3db2cdde8cb6db8166c0`.

<a id="tides"></a>

### Disentangling Dynamics: A Compositional Framework for Temporal Graph Foundation Models (2026)

ID: `tides` · [Źródło](https://eic-emerge.eu/resources/publications-details/disentangling-dynamics-a-compositional-framework-for-temporal-graph-foundation-models) · Weryfikacja: `landing_page_verified`.

TIDES rozdziela reprezentację czasu i struktury; punkt odniesienia dla generalizacji na nowe grafy.

**Brak pełnego tekstu:** PDF OpenReview zwracał blokadę dostępu/CAPTCHA; zachowano rekord i odnośnik. Brak lokalnego pełnego tekstu.

Uwaga: EIC EMERGE podaje ICML 2026, natomiast opis repozytorium autorów wskazuje GFM Workshop @ ICML 2026. Nie potwierdzono publikacji w głównym tracku; zachowano rozbieżność.

<a id="dg-gen"></a>

### A Deep Probabilistic Framework for Continuous Time Dynamic Graph Generation (2025)

ID: `dg-gen` · [Źródło](https://ojs.aaai.org/index.php/AAAI/article/view/33896) · Weryfikacja: `fulltext_title_verified`.

Generowanie grafów dynamicznych i zdarzeń; alternatywny model generatywny.

Lokalnie: `publications/files/process-and-temporal-models/dg-gen.pdf` · 9 stron · [Pobrana kopia](https://ojs.aaai.org/index.php/AAAI/article/download/33896/36051).

SHA-256: `5ed06e6a8e005c5e3dac3428c96737ce9d1a9fc036d90087e88428623a5fc06f`.

<a id="causal-process"></a>

### Causal Process Models: Reframing Dynamic Causal Graph Discovery as a Reinforcement Learning Problem (2026)

ID: `causal-process` · [Źródło](https://proceedings.mlr.press/v323/orujlu26a.html) · Weryfikacja: `fulltext_title_verified`.

Autorzy: Turan Orujlu; Christian Gumbsch; Martin V. Butz; Charley M Wu.

Odkrywanie dynamicznych grafów przyczynowych jako problem RL; osobny kierunek względem inferencji CTMC.

Lokalnie: `publications/files/process-and-temporal-models/causal-process.pdf` · 31 stron · [Pobrana kopia](https://raw.githubusercontent.com/mlresearch/v323/main/assets/orujlu26a/orujlu26a.pdf).

SHA-256: `36abcf4f944d539c0dc7c783a08f732d46c87aa91253ac41f72ae1377281dfc2`.

<a id="event-foundation"></a>

### Foundation Models for Event Prediction Across Heterogeneous Event Logs (2026)

ID: `event-foundation` · [Źródło](https://arxiv.org/abs/2610.17503) · Weryfikacja: `fulltext_title_verified`.

Autorzy: Spaeh, Fabian; Jaffe, Sean; Zhe, Shandian; Shen, Bin.

Foundation Event Predictor: predykcja zdarzeń i generalizacja między logami; preprint.

Lokalnie: `publications/files/process-and-temporal-models/event-foundation.pdf` · 25 stron · [Pobrana kopia](https://arxiv.org/pdf/2610.17503).

SHA-256: `556e5b92db0844e7585d4eb794b004d975cafe02985f1f8df319c1039b332bcb`.

Uwaga: Preprint z października 2026; wpis nie oznacza potwierdzenia recenzji konferencyjnej.

<a id="mint"></a>

### MiNT: Multi-Network Transfer Benchmark for Temporal Graph Learning (2025)

ID: `mint` · [Źródło](https://proceedings.neurips.cc/paper_files/paper/2025/hash/c5548168cb7324f714365a971dfe76d1-Abstract-Datasets_and_Benchmarks_Track.html) · Weryfikacja: `fulltext_title_verified`.

Autorzy: Shamsi, Kiarash; Ngo, Tran Gia Bao; Shirzadkhani, Razieh; Huang, Shenyang; Poursafaei, Farimah; Azad, Poupak; Rabbany, Reihaneh; Coskunuzer, Baris; Rabusseau, Guillaume; Akcora, Cuneyt.

Benchmark transferu temporalnego między sieciami; wskazuje jak dzielić dane.

Lokalnie: `publications/files/process-and-temporal-models/mint.pdf` · 35 stron · [Pobrana kopia](https://proceedings.neurips.cc/paper_files/paper/2025/file/c5548168cb7324f714365a971dfe76d1-Paper-Datasets_and_Benchmarks_Track.pdf).

SHA-256: `6676346d493a4baa3425f3882a61695ad0078fd84f6b32f5c41f0e9362c5257c`.

<a id="graph-transfer"></a>

### When Do Graph Foundation Models Transfer? A Data-Centric Theory (2026)

ID: `graph-transfer` · [Źródło](https://proceedings.mlr.press/v306/zhu26e.html) · Weryfikacja: `fulltext_title_verified`.

Autorzy: Jiajun Zhu; Ying Chen; Peihao Wang; Yixuan He; Pan Li; Aditya Akella; Zhangyang Wang.

Teoria przesunięcia reprezentacji między domenami grafowymi.

Lokalnie: `publications/files/process-and-temporal-models/graph-transfer.pdf` · 21 stron · [Pobrana kopia](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhu26e/zhu26e.pdf).

SHA-256: `b78576a0a8da391d3e6c0ad5a9269b0615daa162ea1211eb3a7d3af5488607fc`.

<a id="process-incontext"></a>

### An In-Context Foundation Model for Predictive Process Monitoring on Event Logs (2026)

ID: `process-incontext` · [Źródło](https://publications.rwth-aachen.de/record/1029172/) · Weryfikacja: `fulltext_title_verified`.

Autorzy: Alessandro Berti; Wil M. P. van der Aalst.

In-context learning dla monitorowania procesów; porównanie transferu między logami.

Lokalnie: `publications/files/process-and-temporal-models/process-incontext.pdf` · 26 stron · [Pobrana kopia](https://www.alessandroberti.it/new_papers/2025_Berti_ICL_FM.pdf).

SHA-256: `56743ee5c482f39c2ec664b0af7a004ae091dfa146263d001ea6cba267fb035b`.

Uwaga: Pobrano publiczną kopię autorską z serwera Alessandro Bertiego, bez końcowej paginacji wydawcy.

<a id="agentic-twins"></a>

### Agentic digital twins: bridging model-based and AI-driven decision-making support for a new era of supply chain and operations management (2026)

ID: `agentic-twins` · [Źródło](https://www.tandfonline.com/doi/full/10.1080/00207543.2026.2630277) · Weryfikacja: `metadata_verified`.

Autorzy: Dmitry Ivanov.

Łączenie modeli, symulacji i AI we wspomaganiu decyzji.

**Brak pełnego tekstu:** Dostęp wydawcy zablokowany; rekord bibliograficzny wskazuje dostęp subskrypcyjny. Nie znaleziono kopii otwartej.

Uwaga: Pełny tekst u wydawcy wymaga dostępu subskrypcyjnego według rekordu RePEc; nie znaleziono otwartej kopii autorskiej.

<a id="object-world-model"></a>

### Object-Centric World Models for Causality-Aware Reinforcement Learning (2026)

ID: `object-world-model` · [Źródło](https://ojs.aaai.org/index.php/AAAI/article/view/39642) · Weryfikacja: `fulltext_title_verified`.

Reprezentacja obiektów i zależności w modelach świata dla RL.

Lokalnie: `publications/files/process-and-temporal-models/object-world-model.pdf` · 9 stron · [Pobrana kopia](https://ojs.aaai.org/index.php/AAAI/article/download/39642/43603).

SHA-256: `e7fa4159929505781e012333a86ab646e9e942486aa340c172b5b552eaf15a16`.

<a id="memexplainer"></a>

### Towards the Explainability of Temporal Graph Networks via Memory Backtracking and Topological Attribution (2026)

ID: `memexplainer` · [Źródło](https://proceedings.mlr.press/v306/liu26gd.html) · Weryfikacja: `fulltext_title_verified`.

Autorzy: Yazheng Liu; Xi Zhang; Sihong Xie; Hui Xiong.

Atrybucja topologii i pamięci TGN; ważny konkurent dla wyjaśnień trajektoryjnych.

Lokalnie: `publications/files/process-and-temporal-models/memexplainer.pdf` · 30 stron · [Pobrana kopia](https://raw.githubusercontent.com/mlresearch/v306/main/assets/liu26gd/liu26gd.pdf).

SHA-256: `eb48db2e2134ce157aa2d92bbdfd8fa66f127e1faea54a27c52029867a3f7b83`.

<a id="kronos"></a>

### Kronos: A Foundation Model for the Language of Financial Markets (2026)

ID: `kronos` · [Źródło](https://ojs.aaai.org/index.php/AAAI/article/view/39730) · Weryfikacja: `fulltext_title_verified`.

Tokenizacja i modelowanie szeregów finansowych; potencjalny baseline rynkowy.

Lokalnie: `publications/files/process-and-temporal-models/kronos.pdf` · 8 stron · [Pobrana kopia](https://ojs.aaai.org/index.php/AAAI/article/download/39730/43691).

SHA-256: `3758294c7fc1373b4dbf10aefddb6e0dcaf53b6e5a2094422ccf47970e3574cd`.

<a id="tgm"></a>

### TGM: A Modular and Efficient Library for Machine Learning on Temporal Graphs (2026)

ID: `tgm` · [Źródło](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d978cd64d598bbaf6a2fff1d6864d601-Abstract-Conference.html) · Weryfikacja: `fulltext_title_verified`.

Autorzy: Chmura, Jacob; Huang, Shenyang(Andy); Ngo, Tran Gia Bao; Parviz, Ali; Poursafaei, Farimah; Leskovec, Jure; Bronstein, Michael; Rabusseau, Guillaume; Fey, Matthias; Rabbany, Reihaneh.

Biblioteka do eksperymentów na grafach temporalnych.

Lokalnie: `publications/files/process-and-temporal-models/tgm.pdf` · 50 stron · [Pobrana kopia](https://proceedings.iclr.cc/paper_files/paper/2026/file/d978cd64d598bbaf6a2fff1d6864d601-Paper-Conference.pdf).

SHA-256: `09e34e05c91eab1fc0f698dbef35e8ba8d2b2f85fcf273a9d811535ad94af4ee`.


## Sieci gospodarcze, handel i zastosowania

<a id="production-gnn"></a>

### Learning Production Functions for Supply Chains with Graph Neural Networks (2025)

ID: `production-gnn` · [Źródło](https://ojs.aaai.org/index.php/AAAI/article/view/35004) · Weryfikacja: `fulltext_title_verified`.

Uczenie funkcji produkcji i zapasów; powiązany benchmark SupplySim.

Lokalnie: `publications/files/economics-and-applications/production-gnn.pdf` · 9 stron · [Pobrana kopia](https://ojs.aaai.org/index.php/AAAI/article/download/35004/37159).

SHA-256: `ed000e025efeee93b0e069fbe2be204a3bbd5d95fba6bd469f9e80fdf91f3008`.

<a id="global-trade-gnn"></a>

### Global trade network prediction based on spatiotemporal graph neural network and gradient boosting model (2026)

ID: `global-trade-gnn` · [Źródło](https://www.nature.com/articles/s41598-026-72209-3) · Weryfikacja: `fulltext_title_verified`.

Grafowy model predykcji handlu; punkt odniesienia dla zastosowania gospodarczego.

Lokalnie: `publications/files/economics-and-applications/global-trade-gnn.pdf` · 18 stron · [Pobrana kopia](https://www.nature.com/articles/s41598-026-72209-3_reference.pdf).

SHA-256: `649b30c1f36bfbec2b72c9c69e08fdbf760af721f032bfb6e009111454156388`.

Uwaga: Pobrano wersję Article in Press od wydawcy. Wyników autorów nie replikowano.

<a id="network-origins"></a>

### The Network Origins of Aggregate Fluctuations (2012)

ID: `network-origins` · [Źródło](https://doi.org/10.3982/ECTA9623) · Weryfikacja: `fulltext_title_verified`.

Teoria zależności między strukturą sieci produkcyjnej a agregacją szoków.

Lokalnie: `publications/files/economics-and-applications/network-origins.pdf` · 41 stron · [Pobrana kopia](https://economics.mit.edu/sites/default/files/publications/The%20Network%20Origins%20of%20Aggregate%20Fluctuations.pdf).

SHA-256: `26e7df4e7d350f2650b134e5291e9df17b32fbd3654c1e04eabb78c727480ca4`.

<a id="oecd-shocks"></a>

### Shocks in a highly interlinked global economy (2024)

ID: `oecd-shocks` · [Źródło](https://www.oecd.org/en/publications/shocks-in-a-highly-interlinked-global-economy_4a2f0127-en.html) · Weryfikacja: `fulltext_title_verified`.

Powiązania gospodarcze, ekspozycja na szoki i mechanizmy dostosowań.

Lokalnie: `publications/files/economics-and-applications/oecd-shocks.pdf` · 59 stron · [Pobrana kopia](https://www.oecd.org/content/dam/oecd/en/publications/reports/2024/06/shocks-in-a-highly-interlinked-global-economy_e10fdec7/4a2f0127-en.pdf).

SHA-256: `3e0f7fa813f0b8a6b733a362fb9dfe4863a26fe157f9de9e6b12eb82559e1051`.

<a id="pandemic-shocks"></a>

### Forecasting the propagation of pandemic shocks with a dynamic input-output model (2022)

ID: `pandemic-shocks` · [Źródło](https://www.sciencedirect.com/science/article/pii/S0165188922002317) · Weryfikacja: `fulltext_title_verified`.

Dynamiczny model input-output; konkurent dla propagacji z zapasami i produkcją.

Lokalnie: `publications/files/economics-and-applications/pandemic-shocks.pdf` · 35 stron · [Pobrana kopia](https://discovery.ucl.ac.uk/id/eprint/10218120/1/Forecasting%20the%20propagation%20of%20pandemic%20shocks%20with%20a%20dynamic%20input-output%20model.pdf).

SHA-256: `1be00b590a374c50607caccc4cf819b1fa912f2006ab69eb6321c9ea97c45750`.

<a id="imf-seaborne"></a>

### World Seaborne Trade in Real Time: A Proof of Concept for Building AIS-based Nowcasts from Scratch (2020)

ID: `imf-seaborne` · [Źródło](https://www.imf.org/en/publications/wp/issues/2020/05/14/world-seaborne-trade-in-real-time-a-proof-of-concept-for-building-ais-based-nowcasts-from-49393) · Weryfikacja: `fulltext_title_verified`.

Metodyka rekonstrukcji podróży i handlu z danych AIS.

Lokalnie: `publications/files/economics-and-applications/imf-seaborne.pdf` · 44 stron · [Pobrana kopia](https://www.imf.org/-/media/files/publications/wp/2020/english/wpiea2020057-print-pdf.pdf).

SHA-256: `7f85958d52826ba6148b9cbe0a45669ceee85139d54b0a87a6a423602f266c51`.

<a id="imf-space"></a>

### Nowcasting Global Trade from Space (2025)

ID: `imf-space` · [Źródło](https://www.imf.org/en/publications/wp/issues/2025/05/16/nowcasting-global-trade-from-space-566957) · Weryfikacja: `fulltext_title_verified`.

Nowcasting handlu na podstawie obserwacji ruchu statków.

Lokalnie: `publications/files/economics-and-applications/imf-space.pdf` · 37 stron · [Pobrana kopia](https://www.imf.org/-/media/files/publications/wp/2025/english/wpiea2025093-print-pdf.pdf).

SHA-256: `28ec6524760bdb266e4e605913b56b7592da7536a8e2502e0673220d18436673`.

<a id="oecd-products"></a>

### Monitoring global trade by products, using big data (2026)

ID: `oecd-products` · [Źródło](https://www.oecd.org/en/publications/monitoring-global-trade-by-products-using-big-data_e0447f00-en.html) · Weryfikacja: `fulltext_title_verified`.

Mapowanie transportu na grupy towarowe i ograniczenia obserwowalności ładunków.

Lokalnie: `publications/files/economics-and-applications/oecd-products.pdf` · 67 stron · [Pobrana kopia](https://www.oecd.org/content/dam/oecd/en/publications/reports/2026/05/monitoring-global-trade-by-products-using-big-data_56f2bf58/e0447f00-en.pdf).

SHA-256: `2882f920f2532c62477001498350ea50c20d6d087e538eeb9a14e04a0ede5055`.

<a id="production-primer"></a>

### Production Networks: A Primer (2019)

ID: `production-primer` · [Źródło](https://www.annualreviews.org/doi/10.1146/annurev-economics-080218-030212) · Weryfikacja: `fulltext_title_verified`.

Autorzy: Vasco M. Carvalho; Alireza Tahbaz-Salehi.

Wprowadzenie do sieci produkcyjnych i transmisji szoków; fundament zastosowań ekonomicznych.

Lokalnie: `publications/files/economics-and-applications/production-primer.pdf` · 38 stron · [Pobrana kopia](https://vasco-m-carvalho.github.io/pdfs/ProductionNetworks.pdf).

SHA-256: `2d2e87a6f859ef019363ed7f43886c2ec4149f149e2f0f640620f932781db73b`.

Uwaga: Artykuł z 2019; pobrana kopia autorska jest datowana na grudzień 2018.

<a id="spa"></a>

### Structural Path Analysis and Multiplier Decomposition within a Social Accounting Matrix Framework (1984)

ID: `spa` · [Źródło](https://ideas.repec.org/a/ecj/econjl/v94y1984i373p111-36.html) · Weryfikacja: `fulltext_title_verified`.

Klasyczny rozkład mnożników ekonomicznych na ścieżki; niezbędne porównanie z TTA.

Lokalnie: `publications/files/economics-and-applications/spa.pdf` · 30 stron · [Pobrana kopia](https://orbi.uliege.be/bitstream/2268/90536/1/Structural%20Path%20Analysis%20and%20Multiplier%20Decomposition%20within%20a%20Social%20Accounting%20Matrix%20Framework.pdf).

SHA-256: `f706e1314a1b3b8ac02c0664ef61678d4bf6e04f76997f04d55925af19db7746`.

<a id="leontief-markov"></a>

### Leontief Meets Markov: Sectoral Vulnerabilities Through Circular Connectivity (2022)

ID: `leontief-markov` · [Źródło](https://link.springer.com/article/10.1007/s11067-021-09551-8) · Weryfikacja: `fulltext_title_verified`.

Związek sieci input-output z łańcuchami Markowa i czasami pierwszego przejścia.

Lokalnie: `publications/files/economics-and-applications/leontief-markov.pdf` · 32 stron · [Pobrana kopia](https://research.gold.ac.uk/id/eprint/30489/1/Wirkierman2021_Article_LeontiefMeetsMarkov.pdf).

SHA-256: `afb598cdc039a595f1d32ad822ec258f8155c895892c0ad887bb0d8e5dcb8cab`.

Uwaga: Publikacja online w 2021, rok tomu 2022.

<a id="path-decomposition"></a>

### Structural path decomposition (2009)

ID: `path-decomposition` · [Źródło](https://www.sciencedirect.com/science/article/abs/pii/S0140988308001680) · Weryfikacja: `fulltext_title_verified`.

Autorzy: Richard Wood; Manfred Lenzen.

Rozkład zmian struktury gospodarczej na wkłady ścieżek.

Lokalnie: `publications/files/economics-and-applications/path-decomposition.pdf` · 7 stron · [Pobrana kopia](https://richardw.folk.ntnu.no/papers/Wood%2C%20Lenzen_2009_Structural%20path%20decomposition.pdf).

SHA-256: `056273921779823e39c36060f34e73c8a6f16c112790c82df31aa11d70193b59`.

<a id="earthquake"></a>

### Supply Chain Disruptions: Evidence from the Great East Japan Earthquake (2021)

ID: `earthquake` · [Źródło](https://www.repository.cam.ac.uk/items/abbc0ebd-b7cc-47bc-af72-b08d9b82f06c) · Weryfikacja: `fulltext_title_verified`.

Autorzy: Pereira Marques de Carvalho, Vasco; Nirei, Makoto; Saito, Yukiko; Tahbaz-Salehi, Alireza.

Empiryczna transmisja zaburzeń przez sieć dostaw po trzęsieniu ziemi.

Lokalnie: `publications/files/economics-and-applications/earthquake.pdf` · 51 stron · [Pobrana kopia](https://api.repository.cam.ac.uk/server/api/core/bitstreams/3568c3a2-dafc-49cc-a220-56fe2b633a95/content).

SHA-256: `f1461985e2e1cf4ba7de203834e73b1d28c0308b3c7dae9a15245a85289eca90`.

Uwaga: Wersja opublikowana w 2021; pobrana kopia autorska jest datowana na listopad 2020.

<a id="supply-resilience"></a>

### Supply Chain Resilience Prediction and Industrial Economic Shock Transmission Path Analysis Integrating Knowledge Graphs and Deep Reinforcement Learning (2026)

ID: `supply-resilience` · [Źródło](https://www.nature.com/articles/s41598-026-72753-y) · Weryfikacja: `fulltext_title_verified`.

Knowledge graph i RL w analizie odporności oraz ścieżek szoków.

Lokalnie: `publications/files/economics-and-applications/supply-resilience.pdf` · 26 stron · [Pobrana kopia](https://www.nature.com/articles/s41598-026-72753-y_reference.pdf).

SHA-256: `68361316a33b3f37e9327ab5cfa1b95e48ac2589ac074160f5553463381ed77b`.

Uwaga: Pobrano wersję Article in Press od wydawcy. Wyników autorów nie replikowano.

<a id="supplier-recommendation"></a>

### Using Knowledge Graph-Enhanced Relational Graph Convolutional Network for Potential Supplier Recommendation (2026)

ID: `supplier-recommendation` · [Źródło](https://www.sciencedirect.com/science/article/pii/S1568494626019836) · Weryfikacja: `metadata_verified`.

Rekomendacje alternatywnych dostawców na podstawie grafu relacji.

**Brak pełnego tekstu:** Strona wydawcy dostępna bibliograficznie; nie znaleziono publicznego pełnego PDF.

<a id="imf-portwatch"></a>

### Nowcasting Country-Level Trade Estimates Using IMF PortWatch (2026)

ID: `imf-portwatch` · [Źródło](https://www.imf.org/en/publications/wp/issues/2026/05/19/nowcasting-country-level-trade-estimates-using-imf-portwatch-576176) · Weryfikacja: `fulltext_title_verified`.

Nowcasting handlu krajowego; przykład wąskiego zastosowania danych transportowych.

Lokalnie: `publications/files/economics-and-applications/imf-portwatch.pdf` · 39 stron · [Pobrana kopia](https://www.imf.org/-/media/files/publications/wp/2026/english/wpiea2026099-source-pdf.pdf).

SHA-256: `54444eecd8eb61916e4c33aafd779af8baf32c61a44b3f99a370a0f6389b6c37`.


## Książki i materiały przekrojowe

<a id="input-output-book"></a>

### Input-Output Analysis: Foundations and Extensions (2022)

ID: `input-output-book` · [Źródło](https://www.cambridge.org/core/books/inputoutput-analysis/431D85A5E459AB078479852169EA77D7) · Weryfikacja: `metadata_verified`.

Autorzy: Ronald E. Miller; Peter D. Blair.

Podręcznik Miller–Blair: współczynniki techniczne, mnożniki i modele input-output.

**Brak pełnego tekstu:** Nie znaleziono otwartej pełnej książki; wydawca oferuje dostęp zakupiony lub instytucjonalny.

Uwaga: Trzecie wydanie (2022). Odnośnik w czacie prowadził do spisu treści, a nie do pełnego tekstu.

<a id="data-driven-book"></a>

### Data-Driven Science and Engineering (2022)

ID: `data-driven-book` · [Źródło](https://www.databookuw.com/) · Weryfikacja: `landing_page_verified`.

Autorzy: Steven L. Brunton; J. Nathan Kutz.

Brunton–Kutz: identyfikacja dynamiki, redukcja wymiaru i sterowanie.

**Brak pełnego tekstu:** Nie znaleziono publicznej kopii pełnego tekstu książki.

Uwaga: Drugie wydanie (2022). Strona autora udostępnia materiały i kod; nie znaleziono pełnej otwartej książki.

<a id="graph-book"></a>

### Graph Representation Learning (2020)

ID: `graph-book` · [Źródło](https://www.cs.mcgill.ca/~wlh/grl_book/) · Weryfikacja: `fulltext_title_verified`.

Autorzy: William L. Hamilton.

Hamilton: reprezentacje węzłów, relacji i grafów; podstawa projektowania enkodera.

Lokalnie: `publications/files/books/graph-book.pdf` · 141 stron · [Pobrana kopia](https://www.cs.mcgill.ca/~wlh/grl_book/files/GRL_Book.pdf).

SHA-256: `bc25ed42b3cc2d5663f1f83172404bec8927e9b09546f69c1fdc914860b3955e`.

Uwaga: Publicznie udostępniony przez autora nieedytowany draft przed publikacją, 141 stron. Nie jest to finalny skład wydawcy.

<a id="chaos-book"></a>

### Making Sense of Chaos: A Better Economics for a Better World (2024)

ID: `chaos-book` · [Źródło](https://www.jstor.org/stable/jj.16971561) · Weryfikacja: `metadata_verified`.

Autorzy: J. Doyne Farmer.

Farmer: perspektywa ekonomii złożoności; kontekst projektu, nie specyfikacja algorytmu.

**Brak pełnego tekstu:** Nie znaleziono publicznej kopii pełnego tekstu książki.

<a id="stochastic-book"></a>

### Stochastic Processes in Physics and Chemistry (2007)

ID: `stochastic-book` · [Źródło](https://www.sciencedirect.com/book/9780444529657/stochastic-processes-in-physics-and-chemistry) · Weryfikacja: `metadata_verified`.

Autorzy: N. G. van Kampen.

van Kampen: procesy stochastyczne, równanie master i przybliżenia.

**Brak pełnego tekstu:** Nie znaleziono publicznej kopii pełnego tekstu książki.

Uwaga: Trzecie wydanie (2007).

<a id="sysid-book"></a>

### System Identification: Theory for the User (1999)

ID: `sysid-book` · [Źródło](https://www.control.isy.liu.se/books/sysid/) · Weryfikacja: `landing_page_verified`.

Autorzy: Lennart Ljung.

Ljung: identyfikowalność, estymacja i walidacja dynamiki.

**Brak pełnego tekstu:** Nie znaleziono publicznej kopii pełnego tekstu książki.

Uwaga: Drugie wydanie (1999). Materiały towarzyszące nie są pełnym tekstem książki.

<a id="causal-book"></a>

### Causal Inference: What If (2020)

ID: `causal-book` · [Źródło](https://miguelhernan.org/whatifbook) · Weryfikacja: `fulltext_title_verified`.

Autorzy: Miguel A. Hernán; James M. Robins.

Hernán–Robins: warunki interpretacji przyczynowej i identyfikacji efektów interwencji.

Lokalnie: `publications/files/books/causal-book.pdf` · 365 stron · [Pobrana kopia](https://static1.squarespace.com/static/675db8b0dd37046447128f5f/t/6a86cf7ecfcb6b4ca8eea5cb/1787219838424/hernanrobins_WhatIf_19aug26.pdf).

SHA-256: `a1067af923e9156bb95fbe4b0d18699bd0723e9c902bdc74465cf7782820b1b5`.

Uwaga: Wydanie bazowe: 2020; pobrany plik zawiera aktualizację z 19 sierpnia 2026.

<a id="forecasting-book"></a>

### Forecasting: Principles and Practice, the Pythonic Way (2026)

ID: `forecasting-book` · [Źródło](https://otexts.com/fpppy/) · Weryfikacja: `landing_page_verified`.

Baseline'y prognoz i walidacja czasowa; książka internetowa.

Lokalnie: `publications/files/books/forecasting-book/index.html` · 24 dokumentów HTML; multimedia mogą wymagać internetu.

Uwaga: Żywa edycja internetowa; 2026 oznacza rok konsultacji. Lokalnie zapisano teksty HTML, bez kompletnego archiwum obrazów i interaktywnych zasobów.

<a id="network-book"></a>

### Network Science (2016)

ID: `network-book` · [Źródło](https://www.networksciencebook.com/) · Weryfikacja: `landing_page_verified`.

Autorzy: Albert-László Barabási.

Barabási: struktura, centralność i odporność sieci.

Lokalnie: `publications/files/books/network-book/index.html` · 12 dokumentów HTML; multimedia mogą wymagać internetu.

Uwaga: Książka wydana w 2016; lokalny zapis internetowej wersji rozdziałów z 2026-10-25, bez wszystkich zasobów multimedialnych.
