# 🧪 Testes das Estruturas de Dados

Este repositório organiza os **TADs** em pastas separadas (`list/`, `queue/`, `stack/`, `avl_tree/`, etc.), e cada um possui seus próprios arquivos `.cpp` e `.hpp`. Os **testes unitários** ficam na pasta `tests/`, seguindo o padrão:

```
data_structures/
├── list/
│   ├── list.cpp 
│   └── list.hpp
├── queue/
│   ├── queue.cpp
│   └── queue.hpp
├── stack/
│   ├── stack.cpp
│   └── stack.hpp
├── avl_tree/
│   ├── avl_tree.cpp
│   └── avl_tree.hpp
├── dsu/
│   ├── dsu.cpp
│   └── dsu.hpp
├── graph/
│   ├── graph.cpp
│   └── graph.hpp
├── hash_table/
│   ├── hash_table.cpp
│   └── hash_table.hpp
├── min_heap/
│   ├── min_heap.cpp
│   └── min_heap.hpp
├── tests/
│   ├── Makefile
│   ├── list_test.cpp
│   ├── queue_test.cpp
│   ├── stack_test.cpp
│   ├── avl_tree_test.cpp
│   ├── dsu_test.cpp
│   ├── graph_test.cpp
│   ├── hash_table_test.cpp
│   ├── min_heap_test.cpp
│   ├── bin/          # Binários compilados (criado automaticamente)
│   └── obj/          # Arquivos objeto (criado automaticamente)
```

O `Makefile` foi configurado para:
- **Compilar todos os testes automaticamente** (sem precisar editar o arquivo quando novos forem adicionados)
- **Detectar automaticamente** novos arquivos `*_test.cpp`
- **Rodar todos os testes** de uma vez ou os testes de um TAD específico
- **Organizar os binários** em `tests/bin/` e os objetos em `tests/obj/`
- **Compilação incremental** (só recompila o que foi modificado)

<br>

## 📋 Estruturas de Dados Disponíveis

| Estrutura | Arquivo de Teste | Status |
|-----------|------------------|--------|
| 📝 **Lista** | `list_test.cpp` | ✅ |
| 🔄 **Fila (Queue)** | `queue_test.cpp` | ✅ |
| 📚 **Pilha (Stack)** | `stack_test.cpp` | ✅ |
| 🌳 **Árvore AVL** | `avl_tree_test.cpp` | ✅ |
| 🔗 **DSU (Disjoint Set Union)** | `dsu_test.cpp` | ✅ |
| 🕸️ **Grafo** | `graph_test.cpp` | ✅ |
| #️⃣ **Tabela Hash** | `hash_table_test.cpp` | ✅ |
| ⬆️ **Min Heap** | `min_heap_test.cpp` | ✅ |

<br>

# ▶️ Comandos Makefile

### 🏃‍♂️ Executar Testes

#### Rodar todos os testes
```bash
make test_all
```

#### Rodar testes específicos
```bash
make test_list        # Testa Lista
make test_queue       # Testa Fila
make test_stack       # Testa Pilha
make test_avl_tree    # Testa Árvore AVL
make test_dsu         # Testa DSU
make test_graph       # Testa Grafo
make test_hash_table  # Testa Tabela Hash
make test_min_heap    # Testa Min Heap
```

### 🔧 Utilitários

#### Compilar sem executar
```bash
make compile
```

#### Limpar arquivos compilados
```bash
make clean
```

#### Ver ajuda
```bash
make help
```

<br>

## 🚀 Como Usar

1. **Clone o repositório** e navegue até a pasta de testes:
   ```bash
   cd data_structures/tests
   ```

2. **Execute todos os testes**:
   ```bash
   make test_all
   ```

3. **Ou execute um teste específico**:
   ```bash
   make test_stack
   ```

<br>

## ➕ Adicionando Novos Testes

Para adicionar uma nova estrutura de dados:

1. **Crie a pasta da estrutura**:
   ```bash
   mkdir data_structures/nova_estrutura
   ```

2. **Adicione os arquivos** `.cpp` e `.hpp` na pasta

3. **Crie o arquivo de teste**:
   ```bash
   touch data_structures/tests/nova_estrutura_test.cpp
   ```

4. **Compile e teste**:
   ```bash
   make test_nova_estrutura
   ```

O Makefile **detectará automaticamente** o novo teste! 🎉

<br>

## 🛠️ Configurações Técnicas

- **Compilador**: `g++`
- **Padrão**: C++17
- **Flags**: `-Wall -Wextra -g` (warnings e debug)
- **Detecção automática** de arquivos `*_test.cpp`
- **Compilação incremental** para melhor performance
- **Organização automática** de binários e objetos

<br>

## 📖 Estrutura do Makefile

O Makefile utiliza wildcards e pattern matching para:
- Detectar automaticamente todos os `*_test.cpp`
- Encontrar e compilar todas as estruturas em `../*/`
- Criar targets dinâmicos para cada teste
- Gerenciar dependências automaticamente

Isso significa que você pode adicionar quantas estruturas quiser sem precisar modificar o Makefile! 🔄