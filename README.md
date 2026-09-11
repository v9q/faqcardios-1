# Central de Ajuda Cardios — FAQ estruturada + bot de WhatsApp

Repositório de trabalho do projeto de melhoria do suporte Cardios: reestruturar a FAQ de atendimento e o bot de WhatsApp (plataforma **Suri**), inspirado na Central de Ajuda do Jusbrasil (busca + categorias de artigos, com o chat como camada adicional de escalonamento).

Este é um **primeiro rascunho** para discussão com o Filipe (Head of Product & IT) — não é conteúdo final publicado.

## Por que essas categorias, nessa ordem

O conteúdo foi priorizado com base em uma análise de **6.490 atendimentos do Suri entre 30/06 e 11/09/2026** (ver `docs/analise-dados-suporte.md` para o detalhe completo). Achados-chave:

- **Suporte Técnico** concentra 77,4% de todo o volume de atendimento.
- Os temas de maior volume isolado são, nesta ordem: **Holter (cartão de memória)**, **CardioNet (instalação)**, **MAPA (cabo/conectividade)**.
- A satisfação do cliente cai de forma quase perfeitamente proporcional ao **tempo de resposta** durante o atendimento (nota 5 = 9 min de resposta média; nota 1 = 75 min) — não à complexidade do problema. Isso é o argumento central do projeto: uma FAQ/bot que responde na hora ataca diretamente a causa da insatisfação.
- O mesmo padrão aparece nas reclamações públicas da empresa no Reclame Aqui (conectividade de MAPA/Arteris e demora no atendimento sobre o cartão do Holter).

Por isso, esta primeira leva cobre em profundidade **Holter, MAPA e CardioNet** (as três categorias de maior volume), e deixa as demais como esqueleto para a próxima rodada.

## Estrutura do repositório

```
faq/
  holter/             ← conteúdo completo (2 artigos)
  mapa/                ← conteúdo completo (3 artigos)
  cardionet/           ← conteúdo completo, mas marcado ⚠️ para revisão técnica do Filipe (4 artigos)
  cardiosmart/         ← esqueleto (próxima rodada)
  pressao-central/     ← esqueleto (próxima rodada)
  ecg/                 ← esqueleto (próxima rodada)
  comercial/           ← esqueleto (próxima rodada)
  financeiro/          ← esqueleto (próxima rodada)
  assistencia-tecnica/ ← esqueleto (fluxo de triagem, não de autoatendimento)
site/
  index.html           ← demo navegável da Central de Ajuda (busca + categorias), estilo Jusbrasil
docs/
  analise-dados-suporte.md ← análise completa dos dados do Suri, Reclame Aqui e inventário de material-fonte
```

Cada artigo em `faq/` segue o mesmo formato: frontmatter (categoria, produtos, volume no Suri, fontes, vídeo relacionado, status) + corpo com resposta rápida para o bot, passo a passo para quem for atender, critério de quando escalar para humano, e a fonte usada.

## Como ver a demonstração

Abra `site/index.html` em qualquer navegador (ou publique via GitHub Pages) para navegar pela Central de Ajuda com busca e categorias, no mesmo espírito da referência indicada (Jusbrasil).

## O que falta antes de publicar de verdade

- [ ] Validar com o Filipe os 4 artigos de CardioNet (marcados ⚠️ — hoje baseados em fichas comerciais, não em um guia de troubleshooting).
- [ ] Confirmar se os números de telefone encontrados nos manuais (Geral (11) 3883-3000, Vendas (11) 3883-3030, SSC (11) 3883-3010) ainda são os usados hoje no atendimento/WhatsApp.
- [ ] Escrever o conteúdo das 6 categorias em esqueleto.
- [ ] Depois da FAQ validada, desenhar o fluxo de conversa do bot no Suri em cima dela (menu/busca → artigo → escalonamento).

## Fontes usadas nesta rodada

- Export de atendimentos do Suri (30/06–11/09/2026, 6.490 registros).
- Manuais vigentes: Arteris AOP, CardioLight, CardioLight+, CardioLoop, CardioMAPA, Cardioseven, Dyna-MAPA AOP/NG, Dynamis.
- Folhetos e fichas técnicas vigentes (incluindo anexos de CardioNet e CardioSmart).
- Canal do YouTube @cardiosmkt (vídeos de treinamento técnico por produto).
- Reclamações públicas no Reclame Aqui.
- Central de Ajuda do Jusbrasil como modelo de referência de estrutura.
