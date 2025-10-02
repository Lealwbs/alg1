# Algoritmos em Grafos - Resumo Completo

## DFS e BFS

### Busca em Profundidade (DFS) e Busca em Largura (BFS)

- **DFS** usa **PILHA** (STACK → DFSTACK)
- **BFS** usa **FILA** (QUEUE → BARBEQUEUE)

**Estruturas de dados:**
- Vetor `[MARCADOS]`
- Vetor `[ANTECESSORES]`

**Representações:**
- Matriz de Adjacência: `V × V = O(V²)`
- Lista de Adjacência: `V + d(v) = O(V + E)`

### Aplicações

- **DFS**: Retorna um caminho **QUALQUER** (se houver) entre 2 vértices
- **BFS**: Retorna o caminho **MAIS CURTO** (se houver) entre 2 vértices
- Ordem de execução de tarefas com interdependência
- Verificar se há ciclos no gráfico

### Tipos de Arestas

**Na DFS:**
- **Aresta de Árvore**: `V.marcado → V.não_marcado`
- **Aresta de Retorno** (Indica Ciclos): `V.marcado → V.marcado`
  - Um grafo direcionado é acíclico se, e somente se, a DFS não encontra nenhuma aresta de retorno

**Classificação completa:**
- **Aresta de árvore**: `V.em_exploração → V.não_explorado`
- **Aresta de retorno**: `V.em_exploração → V.antecessor`
- **Arestas de avanço**: `V.em_exploração → finalizado` (descendente)
- **Arestas de cruzamento**: `V.em_exploração → finalizado` (não descendente)

### Identificar Componentes Conexos

```
[ID_COMPONENTES]
COMPONENTES_COUNT++ para cada loopada de vértice
```

---

## Grafo Bipartido

**Propriedade:** Um grafo é bipartido se, e somente se, **não contém um ciclo de tamanho ímpar**.

**Algoritmo de verificação:**
1. BFS `O(V+E)` colorindo cada nível (raiz: vermelho, n1: azul, n2: vermelho...)
2. Verificar se uma aresta possui os terminais da mesma cor `O(E)`

**Custo total:** `O(V+E) + O(E) = O(V+E)`

---

## Usos das Buscas

- **Achar vértices que alcançam V**: Rodar busca no grafo reverso

---

## DAGs (Grafos Direcionados Acíclicos)

Grafos direcionados sem ciclos (quase árvores).

### Ordenação Topológica

**Definição:** Ordenação horizontal `(u → v)` dos vértices tal que, para toda aresta `(u,v)`, `u < v`.

> Um grafo direcionado com ciclo não pode ser ordenado topologicamente (porque teria `u ← v`).

**Como gerar:**
1. Vértices terminais ficam por último na ordenação
2. DFS no grafo
3. Ao terminar de explorar um vértice (vértice terminal), inserir no início de uma lista encadeada
4. Terminando a busca, retorna a lista com os vértices em ordem

**Custo:** DFS + Inserção no início da lista encadeada = `O(V + E) + O(1) = O(V + E)`

> Se é um DAG, então o algoritmo encontra uma ordenação topológica.

---

## Componentes Fortemente Conexos (CFCs)

**Definição:** Partição do conjunto de vértices. Subconjunto maximal de vértices tal que há:
- **Reflexividade**: Todo vértice alcança a si mesmo
- **Transitividade**: Se `u→v` e `v→z`, então `u→z`
- **Simetria**: Todo `u` e `v` são mutuamente alcançáveis

### Algoritmo de Kosaraju-Sharir

**Objetivo:** Descobrir os componentes conexos de um grafo. O grafo de componentes é um DAG.

**Passos:**
1. Rode a DFS a partir de um vértice arbitrário e compute os tempos de finalização dos vértices de G
2. Obtenha GR (grafo reverso)
3. Rode a DFS em GR escolhendo vértices em ordem decrescente do tempo de finalização obtido em (1)
4. Retorne as árvores obtidas em (3) como CFCs separados

> O algoritmo explora os componentes na ordem topológica do grafo de componentes.

**Custo:** `2 × DFS O(V + E) + Calcular Grafo Reverso O(V + E) = O(V + E)`

---

## Árvore Geradora Mínima (MST)

**Definição:** Subgrafo de um grafo com todos seus vértices e um subconjunto máximo de arestas que não formam ciclos.

Uma árvore é **geradora mínima** (ou tem custo mínimo) se incluir somente as arestas de menor peso possível que ligam todos os vértices.

**Algoritmos gulosos:** Buscam uma solução ótima global a partir de soluções ótimas locais.

### Algoritmo Genérico para MST

Começa com um vértice, e o conjunto de arestas `S = {}`. Seleciona uma aresta, e se ela for segura, adiciona a S.

### Corte e Cutset

- **Corte (cut)**: Partição do conjunto de vértices de G
- **Cutset**: Conjunto de arestas cuja remoção desconecta o corte do grafo
- **Aresta segura**: A menor aresta desse cutset pertence a uma árvore geradora mínima

---

## Algoritmo de Prim

**Descrição:** Modificação do algoritmo genérico que a todo instante escolhe a aresta de menor peso do cut-set entre os vértices atualmente da árvore e os demais.

Encontra uma árvore geradora mínima (MST) em um grafo ponderado conexo e não direcionado.

**Estruturas de dados:**
- Vetor `[ANTECESSORES]` → `[todos] = -1`
- Vetor `[VISITADOS]` → `[todos] = False`
- Vetor `[RÓTULOS]` → `[raiz] = 0` e `[todos] = ∞`
- HEAP (usando os valores dos rótulos como chave)

**Algoritmo:**
1. Inicia de uma origem
2. Enquanto o heap não estiver vazio:
   - Remove o menor elemento e marca ele
   - Para cada vértice V adjacente ao atual U:
     - Se não estiver marcado e se o peso de UV for menor que o rótulo em V:
       - Atualiza o antecessor
       - Atualiza o rótulo
       - Atualiza a chave no heap

`[ANTECESSORES]` descreve a MST.

**Análise de complexidade:**
- Construção do Heap: `O(V)`
- Laço principal: `O(V)` × Cada loop remove o menor elemento do heap `O(log V)`
- Todas as arestas são avaliadas para atualizar o custo mínimo: `O(E)` × cada atualização `O(log V)`

**Custo:** `O(V) × O(log V) + O(E) × O(log V) = O(V + E) × O(log V)`

Como `E` é muito maior que `V`, então: **`O(E × log V)`**

---

## Algoritmo de Kruskal

**Descrição:** Parecido com Prim, porém usa DSU (Estrutura para conjuntos disjuntos - união-busca).

Todos os vértices viram árvores individuais. Enquanto tiver mais que uma árvore, ele escolhe a aresta de menor custo do grafo e une as 2 árvores que a aresta encosta.

### Estruturas Disjuntas

#### Quick-Find
- Armazena os conjuntos em uma lista encadeada
- `Make-set`: `O(n)` (cada uma das n listas requer `O(1)` para ser criada)
- `Find-set`: `O(1)` (retorna o primeiro elemento da lista - representante)
- `Union`: `O(n²)` em geral (n elementos, realizando até n-1 operações)
  - Pode ser reduzido para `O(m + n log n)` (m = operações, n = elementos)

#### Quick-Union
- Árvore em que cada nó de um elemento aponta para seu pai na árvore
- A raiz aponta para si mesma
- O `find-set` segue os nós da árvore até encontrar a raiz (representante)
- `Make-set`: `O(n)` (cria uma árvore por elemento = `O(1) × V` com a raiz apontando para si mesma)
- `Find-set`: `O(n)` (já que a árvore pode degenerar para uma lista encadeada)
- `Union`: `O(1)` (a união faz com que a raiz de uma árvore aponte para a raiz da outra)

**Otimizações:**
- **União pela altura**: mantém a árvore melhor balanceada
- **Compressão de caminhos**: evita o pior caso do `find-set`, tornando-o `O(m × k)` com crescimento bem lento

**Análise de complexidade:**
- Ordenar as arestas: `O(E × log E)`, `E < V²`, como `log E = O(log V)`, logo fica `O(E × log V)`
- V operações de `make-set`: `O(V) × 1 = O(V)`
- E operações de `find-set` e `union` para cada aresta: `E × (find-set + union)`
- Com Union-Find com as 2 otimizações: `find-set + union = k(V) + O(1) = k(V)` (crescimento quase constante)
- Fica: `O(E) × O(k(V))`

Como `E < V²` e `O(log E) = O(log V)`, então:

**Custo:** `O(E log V) + O(V) + O(E × k(V)) = O(E × log V)` (igual a Prim)

---

## Caminhos Mínimos

> **Propriedade:** Todo subcaminho de um caminho mais curto é um caminho mais curto.

---

## Algoritmo de Dijkstra

**Restrição:** Não admite arestas negativas.

**Aplicações:**
- Caminhos mais curtos a partir de uma única origem
- Encontrar o caminho mais curto para um único destino
- Encontrar o menor caminho entre um par de vértices
- Encontrar o menor caminho entre todos os pares de vértices

É parecido com Prim, usa estratégia gulosa e encontra a solução ótima.

**Estruturas de dados:**
- Vetor `[PESOS_ESTIMADOS]`: todos = infinito, exceto `[0] = 0`
  - Estimativa (limite superior) de menor caminho entre S e os demais
  - Caso exista um caminho mais curto para V que a estimativa atual, o antecessor e a estimativa de V são atualizados (relaxados)
- Vetor `[ANTECESSORES]`: todos = -1
- MINHEAP com os `PESOS_ESTIMADOS` como chave

**Algoritmo:**
1. Enquanto o heap não estiver vazio:
   - Pega o menor (inicialmente o 0:start)
   - Para cada vértice adjacente, relaxa o vértice
   - Se o caminho atual de `start → vértice_v` for menor que algum outro caminho guardado anteriormente, troca e muda o pai

**Análise de complexidade:**
- Vetor de antecessores: `O(V)`
- Laço, todos os vértices: `O(V)` × cada chamada remove o menor elemento do heap `O(log V)` = `O(V × log V)`
- Todas as arestas são avaliadas: no pior caso `O(E)` relaxamentos × `O(log V)` cada um = `O(E × log V)`

**Custo:** `O(V × log V + E × log V) = O((V + E) × log V) = O(E × log V)`

---

## Algoritmo de Bellman-Ford

**Vantagem:** Admite arestas negativas.

**Aplicações:**
- Computa o caminho mais curto
- Detecta ciclos negativos (retorna falso caso exista ciclo negativo)

**Algoritmo:**
Relaxa as arestas do grafo V-1 vezes. Se depois de todas as iterações existirem vértices relaxáveis, então existe ciclo negativo no grafo.

**Estruturas de dados:**
- Vetor `[PESOS_ESTIMADOS]`: todos = infinito, exceto `[0] = 0`
- Vetor `[ANTECESSORES]`: todos = -1

**Passos:**
1. Loopa V-1 vezes: Para cada aresta do grafo, relaxa ela
2. Depois, para cada aresta:
   - Se for possível relaxar mais uma vez, tem ciclo negativo e retorna falso
   - Se não houver ciclos, retorna verdadeiro

**Custo:** `O(V × E)`, pois executa `O(V)` relaxações em todas as arestas.

> É mais caro que Dijkstra, mas não assume que os pesos são positivos.

---

## Fluxo Máximo

### Algoritmo de Ford-Fulkerson

**Objetivo:** Determinar fluxo máximo em: `Origem S → Intermediários → Destino T`

Os pesos associados às arestas são chamados de **capacidade**.

**Propriedades:**
- **Conservação de fluxo**: Fluxo de entrada = Fluxo de saída
  - Fluxo transmitido por uma rede = Fluxo que sai por S
- **Restrição de capacidade**: O fluxo de uma aresta não pode ultrapassar a capacidade máxima

**Conceitos:**
- **Aresta para frente (Forward Edges)**: Aumentar o fluxo na direção da aresta `(u,v)`
- **Aresta para trás (Backward Edges)**: "Devolver" o fluxo na aresta `(u,v)`
- **P = Caminho aumentante**: Caminho simples entre S e T no grafo residual Gf
- **R = Gargalo de P**: Menor capacidade das arestas

**Aumentar Fluxo:**
- Se `(u,v)` é uma aresta para frente: `fluxo += R`
- Se `(u,v)` é para trás: `fluxo(v,u) -= R`

**Algoritmo:**
1. Para todo vértice do grafo, `fluxo = 0`
2. Enquanto existir caminho aumentante (no grafo residual, enquanto S conseguir chegar a T):
   - Aumenta o fluxo das arestas do caminho aumentante
3. Repete até não existir mais caminho aumentante (de S até T)

> Se as capacidades forem irracionais, o algoritmo pode não chegar num resultado, mas se forem inteiras, ele converge.

**Análise de complexidade:**
- Inicializar todos fluxos com zero: `O(E)`
- Fluxo máximo = F, o incremento é pelo menos ≥ 1, logo o ciclo principal é executado no máximo F vezes
- Computar um caminho com DFS ou BFS em Gf: `O(E)`
- Aumentar fluxo avalia todas as arestas do caminho simples: `O(V)`
- Construção do gráfico residual: `O(E)`

**Custo:** `O(F × E)`, pois `V ≤ E`

---

### Teorema Max-Flow Min-Cut

> Em todo fluxo em redes, o valor do fluxo máximo é igual ao valor da menor capacidade de um corte s-t.

---

### Algoritmo Capacity-Scaling

**Estratégia:** Eleger o caminho aumentante com o maior gargalo, buscando caminhos com gargalos, no mínimo, iguais a um parâmetro Δ.

Busca um caminho aumentante num subconjunto do grafo residual com somente as arestas com capacidade ≥ Δ.

**Inicialização:** `Δ = 2^⌊lg(maior_capacidade_de_saída_de_S)⌋`

Depois reduz pela metade. O ciclo repete enquanto `Δ ≥ 1`.

**Algoritmo:**
1. Para cada aresta, seta `fluxo = 0`
2. Faz o grafo residual
3. Enquanto `Δ ≥ 1`:
   - Enquanto existir caminho aumentante no `Gf(Δ)` (grafo residual que contém só as arestas dentro do parâmetro):
     - Acha o caminho (de s a t) nessas arestas
     - Aumenta o fluxo
     - Faz o grafo residual novamente
   - Divide o parâmetro `Δ` por 2

> Na última iteração com `Δ=1`, o algoritmo é idêntico a Ford-Fulkerson.

**Análise de complexidade:**
- O laço externo controlando o parâmetro é executado no máximo `O(lg C)`

**Custo:** `O(E² × lg C)`

---

### Algoritmo de Edmonds-Karp

**Descrição:** Modificação do algoritmo de Ford-Fulkerson.

O caminho é recuperado através de uma modificação da busca em largura, ou seja, ele é o **menor caminho aumentante** (em número de arestas): `O(E)`.

Os caminhos podem ter tamanho de 1 a V. Cada aresta pode participar de um caminho de tamanho k, logo existem no máximo `O(V × E)` caminhos aumentantes.

Essa modificação faz com que o custo seja: **`O(E² × V)`**

---

## Tabela Resumo dos Algoritmos

| Algoritmo | Objetivo principal | Complexidade | Observação / Lógica principal |
|-----------|-------------------|--------------|-------------------------------|
| **DFS (Depth-First Search)** | Explorar todos os vértices/arestas, verificar conectividade, detectar ciclos | O(V + E) | Vai "profundamente" até não poder mais; útil para componentes conexos, topological sort etc. |
| **BFS (Breadth-First Search)** | Explorar vértices por camadas, achar caminho mais curto em grafo não ponderado | O(V + E) | Visita primeiro os vértices mais próximos; gera árvore de camadas. |
| **Kosaraju-Sharir** | Encontrar componentes fortemente conexos | O(V + E) | 2 DFS: uma em G, outra em GR em ordem decrescente de finalização. |
| **Prim** | Encontrar Árvore Geradora Mínima (MST) | O(E log V) (com heap) | Expande a MST a partir de um vértice, sempre pegando a aresta mais barata que conecta. |
| **Kruskal** | Encontrar Árvore Geradora Mínima (MST) | O(E log V) | Ordena arestas e une componentes com Union-Find; cresce pela menor aresta global. |
| **Dijkstra** | Caminho mínimo a partir de uma origem (sem pesos negativos) | O((V + E) log V) (com heap) | Relaxa arestas, escolhendo sempre o vértice de menor distância ainda não processado. |
| **Bellman-Ford** | Caminho mínimo com pesos negativos (sem ciclos negativos) | O(V × E) | Relaxa todas as arestas V-1 vezes; detecta ciclos negativos. |
| **Ford-Fulkerson** | Fluxo máximo em grafos com capacidades | O(E × F), onde F = fluxo máximo | Aumenta fluxo via caminhos aumentantes; complexidade depende do valor de F. |
| **Capacity Scaling** | Fluxo máximo otimizado com escalonamento de capacidade | O(E² log U), onde U = capacidade máxima | Busca caminhos aumentantes só com arestas de capacidade ≥ Δ; Δ diminui exponencialmente. |
| **Edmonds-Karp** | Fluxo máximo com escolha do menor caminho aumentante (BFS) | O(V × E²) | Garante polinomial; cada aresta pode saturar/dessaturar O(V) vezes. |

---

