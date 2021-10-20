# Company API :office:

## Descrição :scroll:

Uma API feita em Django e DRF para acessar organizações e seus funcionários. A ideia é criar empresas e seus
funcionários, onde estes funcionários seriam os usuários da plataforma, um usuário pode pertencer a mais de uma empresa.

## Implementação :hammer_and_wrench:

Foram criadas duas models, `Company` e `Employee`, e um relacionamento M2M entre elas. Como não havia nada muito
complexo nas operações de crud dessas API's foram implementadas duas API's utilizando `ModelViewSet`. O metodo destroy
foi ajustado para não excluir os itens, e sim apenas alterar sua situação para excluído, tendo isso em vista o
get_queryset também foi alterado para não listar registros excluídos, mas ainda é possível acessar um registro
individualmente. Para ver o nome dos funcionários que trabalham em uma empresa ou das empresas em que um funcionário
trabalha foi adicionado o lookfield. Nos serializers é realidade uma validação nos nomes tanto do funcionário quanto no
da empresa para impedir que possam ser criados dois funcionários com nomes iguais porém com cases diferentes
como `Malfoy`e `malfoy`, facilitando a pesquisa por um funcionário.

## Uso

A documentação da API foi gerada utilizando Swagger e está disponível na raiz do site da
api: https://company-apiv1.herokuapp.com/
Lá é possível verificar os métodos permitidos e os endpoints bem como os dados que precisam ser enviados na requisição.
![image](https://user-images.githubusercontent.com/22118060/138163974-d1872fef-8c8b-4e75-86b3-bf46e78f8ba7.png)
![image](https://user-images.githubusercontent.com/22118060/138164141-196d859f-d945-486b-a22a-006f53442bc1.png)

### Company

Para criar uma `Company` é possível `trading_name`, `name` e `situation` onde name precisa ser único e é um campo
obrigatório, `situation` tem como default a opção ativo mas pode ser passada outras opções como `I` de inactive e `E` de
excluded. Exemplo:

```json
{
  "trading_name": "Ravenclaw",
  "name": "ravenclaw",
  "situation": "A"
}
```

### Employee

Para criar um `Employee` é possível informar `first_name`, `last_name`, `username`, `situation` e `company` onde
username precisa ser único e é um campo obrigatório, além de ter seus espaços removidos no serializer para ser
adicionado ao banco de dados. Também é possível passar opções de situation (A,I,E), porém a default é A, também é
possíve informar id de uma ou mais companies no campo `company`. Exemplo:

```json
{
  "first_name": "Draco",
  "last_name": "Malfoy",
  "username": "ihatemuggles",
  "situation": "A",
  "company": [
    1,
    2
  ]
}
```

## FIM :coffin:

![potter](https://media2.giphy.com/media/sOnJKMg1xKfUBgvdPJ/giphy.gif)
