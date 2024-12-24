# Case Gabriel Mizuno

Nesse case foquei em mostrar quais métodos e como organizar o código, visando deixar o código claro e simples.
Na útlima seção deixei alguns pontos de melhorias numa seção no final.

## Arquiterura

## Criação e Limpeza de Base
**Tratamento de valores nulos:**

1.   Transaction: Itens com preço nulo serão desconsiderado
2.   Clients: Clientes sem e-mail preenchido corretamento serão substituidos por "Sem Email", clientes sem telefone preenchido corretamento serão substituidos por "Sem Telefone",
3.   Products: Nenhum tratativa será feita nessas tabelas, pois assumisse que essa tabela terá os campos corretamente preenchidos

**Deduplicação:**

1.   Transaction: Dado um id de transação so podemos ter 1 único por pedido, ou seja, a chave primária será a concatenação do id com Product. No exemplo a abaixo o segundo item será desconsiderado

| id | Product | Quantity | Date       |
|----|---------|----------|------------|
| 1  | XXX     | 1        | 2024-10-01 |
| 1  | XXX     | 2        | 2024-10-02 |


2.   Clients: Como o objetivo desssa tabela será manter um canal de contato mais atualizado em caso de id duplica será deletado o registro mais antigo.

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

Para automação do job foi utilizado o GCloud e Cloud Run para execução, existem duas possibilidades; Terraform ou Gcloud (linha de comando). Para
esse case usarei o Gcloud.

OBS: link para [Terraform](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_job) e [GCloud](https://cloud.google.com/run/docs/create-jobs)

```bash

gcloud run jobs deploy job-case-gabriel-mizuno \
    --source . \
    --tasks 1 \
    --max-retries 5 \
    --region us-east1 \
    --project=case-445517 \
    --set-secrets=API_SECERT_KEY=aiqfome_password:1,API_USER_KEY=aiqfome_host_api:1,SFPT_KEY=aiqfom_keysftp:1
```

![Log_Cloud_Run.png](assets/Log_Cloud_Run.png)


Como esse código conseguimos criar um job SEM agendamento. Para realizar um agendamento basta executar o seguinte codigo

```bash

gcloud scheduler jobs create http test-job --schedule "5 9 * * *" \
       --location='us-east1' \
       --http-method='POST' \
       --uri="https://us-east1-run.googleapis.com/apis/run.googleapis.com/v1/namespaces/case-445517/jobs/job-case-gabriel-mizuno:run" \
       --oidc-service-account-email=953749029646-compute@developer.gserviceaccount.com  \
       --oidc-token-audience="https://us-east1-run.googleapis.com/apis/run.googleapis.com/v1/namespaces/case-445517/jobs/job-case-gabriel-mizuno:run" 
```

![Cloud_Run_Scheduler.png](assets/Cloud_Run_Scheduler.png)

Após a execução dos comandos, será necessário criar um alerta manualmente no Cloud Monitoring, como mostrando na imagem abaixo

![Alerta_Cloud_Run.png](assets/Alerta_Cloud_Run.png)

Pensando em melhorias e maior automação;

- [Artifact Registry](https://cloud.google.com/artifact-registry/docs)
- Github ou Gitlab
- Uso de outros Vaults

## Guardrails e Monitoramento

Em caso de falha um email será enviado para uma lista de emails, previamente definida. 
Quanto aos alertas será necessário criar umas configurações no Cloud Monitoring. Como mostra as imagens abaixo

![Alerta_Cloud_Run.png](assets/Alerta_Cloud_Run.png)

## Pontos de melhoria

- Uso do Terraform para automatizar todas as etapas (Deploy, Agendamento e Monitoramento)
- Separação das responsabilidades