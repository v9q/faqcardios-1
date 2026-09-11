---
id: mapa-cabo-usb-rs232
categoria: MAPA
produtos: [CardioMAPA, Dyna-MAPA AOP, Dyna-MAPA NG]
titulo: "O computador não reconhece o cabo/adaptador RS232-USB do meu MAPA"
volume_suri: "88 casos em 3 meses"
fontes: ["QuickSteps Cabo Adaptador RS232/USB e Adaptador IR/USB (REV006)", "Manual do Usuário Dyna-MAPA AOP VER003/FEV2025"]
status: pronto para revisão
---

## Resposta rápida (bot / primeira mensagem)

A causa mais comum de falha de conexão do cabo adaptador RS232/USB é o **driver não instalado corretamente** ou o **Windows atribuindo a porta COM errada**. Passos:

1. Confirmar que o driver do Cabo Adaptador RS232/USB foi instalado (CD/instalador que acompanha o acessório).
2. Se o cliente também usa o Adaptador IR/USB (para gravadores digitais de Holter) no mesmo computador, atenção: **cada adaptador deve ficar sempre na mesma porta USB física** — se for trocado de porta, o Windows atribui uma nova porta COM e a configuração do software (CardioSmart) precisa ser refeita.
3. Verificar no Gerenciador de Dispositivos do Windows qual porta COM foi atribuída ao adaptador, e conferir se essa é a mesma porta selecionada no CardioSmart.

## Passo a passo para orientar o cliente

1. Perguntar se o cabo já funcionou antes ou se é a primeira instalação.
2. Se for a primeira vez: confirmar instalação do driver específico do Cabo Adaptador RS232/USB (não confundir com o driver do Adaptador IR/USB — são drivers diferentes).
3. Se já funcionou antes e parou: perguntar se o cabo foi trocado de porta USB, ou se outro adaptador Cardios foi conectado depois. Orientar a reconectar na mesma porta original ou reconfigurar a porta COM no CardioSmart.
4. Confirmar compatibilidade do sistema operacional (driver homologado para Windows; versões muito antigas ou muito novas podem exigir atenção extra — validar com suporte técnico se necessário).

## Quando escalar para atendimento humano

- Driver instalado corretamente, porta COM confirmada, e ainda assim sem comunicação — pode ser defeito no cabo ou na porta do monitor.
- Cliente em sistema operacional não coberto pela documentação atual (confirmar compatibilidade com o time técnico).

## Fonte / observações

Baseado no guia rápido "QuickSteps Cabo Adaptador RS232/USB e Adaptador IR/USB" (nota importante sobre troca de porta COM) e nos acessórios listados no Manual do Usuário Dyna-MAPA AOP (Adaptador RS-232/USB).
