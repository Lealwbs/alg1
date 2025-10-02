##### **DFS e BFS:**

**Busca em Profundidade (Depth First Search) e Busca em largura (Breadth First Search)**

DFS usa PILHA (STACK -> DFSTACK)

BFS usa FILA (QUEUE -> BARBEQUEUE)

VETOR \[MARCADOS]

VETOR \[ANTECESSORES]



MatrixAdj = V \* V = O(V²) 

ListaAdj = V + d(v) = O(V + E) 



* **DFS: Retornar um Caminho QUALQUER (se houver) entre 2 vertices**
* **BFS: Retorna o Caminho MAIS CURTO (se houver) entre 2 vertices**
* **Ordem de execução de tarefas com interdependência**
* **Se Há ciclos no gráfico**

Aresta de Árvore: V.marcado -> V.não\_marcado

Aresta de Retorno (Indica Ciclos): V.marcado -> V.marcado

(Um grafo direcionado é acíclico se, e somente se, a DFS não encontra nenhuma aresta de retorno)

* **Identificar componentes conexos**

\[ID\_COMPONENTES]

COMPONENTES\_COUNT++ para cada loopada de vertice



##### **GRAFO BIPARTIDO**

* Se, e somente se, não contém um ciclo de tamanho ímpar
* BFS O(V+E) colorindo cada nivel (raiz: verm, n1: azul, n2: verm...), depois verificar se uma aresta possui os terminais da mesma cor O(E).
* Custo: O(V+E) + O(E) = O(V+E)





##### **USOS DAS BUSCAS**

* Achar vértices que alcançam V: Rodar busca no grafo reverso



**Aresta de árvore:** V.em\_exploracao -> V.nao\_explorado

**Aresta de retorno:** V.em\_exploracao -> V.antecessor

**Arestas de avanço:** V.em\_exploracao -> finalizado (descendente)

**Arestas de cruzamento:** V.em\_exploracao -> finalizado (n descendente)



**DAGs =** Grafos direcionados sem ciclos (Quase árvores)



###### **Ordenação Topológica**

Ordenação horizontal (u -> v) dos vértices tal que, para toda aresta (u,v), u < v.

Um grafo direcionado com ciclo não pode ser ordenado topologicamente (pq ia ter u <- v)



**Como gerar:** Vertices terminais ficam por último na ordenação, DFS no grafo, ao terminar de explorar um vertice (vertice terminal), inserir no inicio de uma lista encadeada), terminando a busca, retorna a lista com os vértices em ordem.



**Custo:** Mesmo da DFS + Inserção no inicio da lista encadead = O(V + E) + O(1) = O(V + E)

\*Se é um DAG, então o algoritimo encontra uma ordenação topológica



###### **Componentes Fortemente Conexos**

**(Partição do conjunto de vértices) Subconjunto maximal de vértices tal que há:**

Relfexividade: Todo vértice alcança a si mesmo

Transitividade: Se u->v, e v->z, então u->z

Simetria: Tal que todo u e v são mutualmente alcançáveis



##### **Algoritmo de Kosaraju-Sharir**

**Serve para descobir os componentes conexos de um grafo. O grafo de componentes é um DAG.**

1. Rode a DFS a partir de um vértice arbitrário e compute os tempo de finalização dos vértices de G
2. Obtenha GR (grafo reverso)
3. Rode a DFS em GR escolhendo vértices em ordem decrescente do tempo de finalização obtido em 1
4. Retorne as árvores obtidas em 3 como CFCs separados

O algoritmo explora os componentes na ordem topológica do grafo de componentes



**Custo: 2 DFS O(V + E) + Calcular Grafo Reverso O(V + E) = O(V + E)**





###### **Arvore Geradora**

**É Subgrafo de um grafo com todos seus vértices e um subconjunto máximo de arestas que não formam ciclos.**

Uma árvore é geradora mínima (ou tem custo mínimo) se incluir somente as arestas de menor peso possível que ligam todos os vértices.



**Algoritmos gulosos:** Buscam uma solução ótima global a partir de soluções ótimas locais.



###### **Algoritmo Genérico para MST**

Começa com um vértice, e o conjunto de arestas S = {}, seleciona uma aresta, e se ela for segura adiciona à S



###### **Corte e Cutset**

Corte (cut) é uma partição do conjunto de vértices de G.

Cutset é um conjunto de arestas cuja remoção desconecta o corte do grafo.

A menor aresta (Aresta segura) desse cutset pertence a uma árvore geradora mínima.





##### **Algoritmo de Prim**

**Modificação do algoritmo genérico que a todo instante escolhe a aresta de menor peso do cut-set entre os vertices atualmente da árvore e os demais.**

Encontra uma árvore geradora mínima (MST) em um  grafo ponderado conexo e não direcionado.



VETOR \[ANTECESSORES] -> \[todos] = -1

VETOR \[VISITADOS] -> \[todos] = False

VETOR \[ROTULOS] -> \[raiz] = 0 e \[todos] = ∞

HEAP \[Usando os valores dos rótulos como chave]



Inicia duma origem, e enquanto o heap não tiver vazio, remove o menor elemento e marca ele.

Pra cada vértice V adjacente ao atual U, se não tiver marcado e se o peso de UV for menor que o rótulo em V:

Ele atualiza o antecessor, atualiza o rótulo, e atualiza a chave no heap.

\[ANTECESORES] Descreve a MST



Construção do Heap: O(V)

Laço principal O(V) e Cada loop remove o menor elemento do heap O(log(V))

Ao todo, todas as arestas são avaliadas para atualizar o custo mínimo O(E) e cada atualização é O(log(V))

**Custo:** O(V) \* O(log(V)) + O(E) \* O(log(V)) = O(V + E) \* O(log(V)). Como E é muito maior que V, então = O(E \* log(V))





##### **Algoritmo de Kruskal**

**Parecido com Prim, porém ele usa DSU (Estrutura para conjuntos disjuntos (união-busca)**

Todas os vertices viram arvores individuais, e enquanto tiver mais que uma árvore, ele escolhe a aresta de menor custo do grafo e uni as 2 arvores que a aresta encosta.



* **Quick-Find**

Armazena-se os conjuntos em uma lista encadeada, no inicio cada elemento é associado numa lista que tem só ele

Make-set O(n), (cada uma das n listas requer O(1) para ser criada).

Fund-set O(1), retorna o primeiro elemento da lista (representante),

Union O(n²), em geral (n elementos, realizando até n-1 operações)

pode ser reduzido para O(m + nlog(n)) m = operações, n = elementos



* **Quick-Union**

Arvore em que cada nó de um elemento aponta para seu pai na árvore, a raiz aponta pra si mesmo. O find-set segue os nós da árvore até encontrar a raiz (representante).

Make-set O(n), (cria uma arvore por elemento = O(1) \* V com a raiz apontando para si mesma)

Find-set O(n), já que a árvore pode degenerar para uma lista encadeada

Union O(1), a união faz com que a raiz de uma árvore aponte para a raiz da outra, 

Para o find, pode-se aplicar união pela altura, para manter a árvore melhor balanceada e compressão de caminhos para evitar o pior caso do find-set, tornando ele O(m \* k), com m = operações, e n = elementosm, k = f(n) com um crescimento bem lento.



Ordenar as arestas O(E \* log(E)), E < V², como log(E) = O(log(V)), logo fica O(E \* log(V))

V operações de make-set = O(V) \* 1 = O(V)

E operações de find-set e union para cada aresta = E \* (find-set + union)

com Union-Find com as 2 otimizações, temos que find-set + union = k(V), onde o crescimento é quase constante, assim fica: O(E) \* O(k(V))

Como E < V², O (log(E) = O(log(V)), então:

**Custo:** O(E log(V)) + O(V) + O(E \* k(V)) = O(E log(V)), igual a prim







