# Case Gabriel Mizuno

## Criação e Limpeza de Base
**Tratamento de valores nulos:**

1.   Transaction: Itens com preço nulo serão desconsiderado
2.   Clients: Clientes sem email preenchido corretamento serão substituidos por "Sem Email", clientes sem telefone preenchido corretamento serão substituidos por "Sem Telefone",
3.   Products: Nenhum tratativa será feita nessas tabela pois assumisse que essa tabela terá os campos corretamente preenchidos

**Deduplicação:**

1.   Transaction: Dado um id de transação so podemos ter 1 único por pedido, ou seja, a chave primária será a concatenação do id com Product. No exemplo a abaixo o segundo item será desconsiderado

| id | Product | Quantity | Date       |
|----|---------|----------|------------|
| 1  | XXX     | 1        | 2024-10-01 |
| 1  | XXX     | 2        | 2024-10-02 |


2.   Clients: Como o objetivo desssa tabela será manter uma canal de contato mais atualizado em caso de id duplica será deletado o registro mais antigo.

| id | Emial | Date       |
|----|-------|------------|
| 1  | XXX   | 2024-10-01 |
| 1  | XXX   | 2024-10-02 |

Outro cenario possível é de clientes com id diferentes mais com mesmo email. Nesse caso séra mantido ambos registros

**Correção de inconsistências de formato:**

1.   Transaction: Transações com valores negativos será desconsideras
2.   Clients:

    *   Email que não seguirem um padrão serão substituidos por Email Inválido
    *   Telefone que não seguirem um padrão serão substituidos por Telefone Inválido


## Automação do Processo

## Guardrails e Monitoramento