# alg1
Algoritmos I - UFMG

##### **DFS e BFS:**

DFS usa PILHA (STACK -> DFSTACK)

BFS usa FILA (QUEUE -> BARBEQUEUE)

\[MARCADOS]

\[ANTECESSORES]



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



###### **Algoritmo de Kosaraju-Sharir**

**Serve para descobir os componentes conexos de um grafo. O grafo de componentes é um DAG.**

1. Rode a DFS a partir de um vértice arbitrário e compute os tempo de finalização dos vértices de G
2. 2\. Obtenha GR (grafo reverso)
3. 3\. Rode a DFS em GR escolhendo vértices em ordem decrescente do tempo de finalização obtido em 1
4. 4\. Retorne as árvores obtidas em 3 como CFCs separados

O algoritmo explora os componentes na ordem topológica do grafo de componentes



**Custo: 2 DFS O(V + E) + Calcular Grafo Reverso O(V + E) = O(V + E)**













