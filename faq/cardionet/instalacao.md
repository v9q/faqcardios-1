---
id: cardionet-instalacao
categoria: CardioNet
produtos: [CardioNet Client, CardioNet Server]
titulo: "Como instalar o CardioNet (Client/Server) e principais erros de instalação"
volume_suri: "208 casos em 3 meses — 2º maior tema depois do cartão do Holter"
fontes: ["Anexo_SW CardioNET-CNC (ficha técnica)", "Anexo_SW CardioNET-CNS (ficha técnica)", "Folheto CardioNet"]
video: "https://www.youtube.com/watch?v=Onu59nKFLc4"
status: "⚠️ rascunho — validar passo a passo técnico com Filipe antes de publicar"
---

## O que é o CardioNet (contexto para quem for responder)

O CardioNet é o software de transmissão de exames de Holter/MAPA via Internet, dispensando a troca física de cartão de memória entre quem grava o exame e quem analisa (central de análise). Existem duas pontas:

- **CardioNet Client** — instalado no local que grava e envia o exame (consultório, clínica, hospital).
- **CardioNet Server** — instalado na central de análise, que recebe os exames enviados.

Ambos dependem também do **Portal CardioNet** (área web) para consulta de relatórios e estatísticas de transmissão.

## Resposta rápida (bot / primeira mensagem) — versão preliminar

1. Confirmar qual dos dois o cliente está instalando: **Client** (quem grava/envia) ou **Server** (quem recebe/analisa) — os instaladores e o fluxo de configuração inicial são diferentes.
2. Confirmar que o computador tem acesso à Internet liberado para o software (portas/URLs do CardioNet não devem estar bloqueadas por firewall/antivírus corporativo).
3. Confirmar que o cliente tem as credenciais do Portal CardioNet em mãos — são as mesmas usadas para a conta do serviço de saúde no portal.

## ⚠️ Pontos que precisam de confirmação técnica antes de virar resposta final
- Passo a passo exato do instalador atual (tela a tela) — os anexos técnicos disponíveis são fichas comerciais, não um guia de instalação passo a passo.
- Requisitos de sistema operacional/hardware atualizados (o que está documentado é antigo).
- Lista de URLs/portas que precisam estar liberadas no firewall, para orientar o TI do cliente.

## Quando escalar para atendimento humano

- Qualquer erro de instalação que não seja "sem internet" ou "sem credencial" — nível 1 não deve tentar diagnosticar erros de instalador sem checklist validado.

## Fonte / observações

Baseado nas fichas técnicas comerciais do CardioNet Client/Server e no Folheto CardioNet. **Este artigo precisa de uma passada com o Filipe** para virar um guia de instalação de verdade — hoje é mais um roteiro de triagem do que um passo a passo técnico completo.
