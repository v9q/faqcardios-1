# Análise dos dados de suporte (base para a priorização da FAQ)

_Fonte original: análise feita no projeto "Cardios Support", consolidada aqui para acompanhar o repositório._

## 1. Sobre os dados do Suri

Export de atendimentos do Suri cobrindo **30/06/2026 a 11/09/2026 — 6.490 atendimentos, 100% via WhatsApp**. Volume semanal estável, entre ~550 e ~690 atendimentos/semana, sem tendência de crescimento ou queda relevante no período.

## 2. Volume por departamento

| Departamento | Atendimentos | % do total | Espera média (min) | Atendimento médio (min) | Resposta média (min) |
|---|---|---|---|---|---|
| Suporte Técnico | 5.025 | 77,4% | 198 | 84,8 | 28,4 |
| Comercial | 831 | 12,8% | 67 | 321 | 76,5 |
| Assistência Técnica | 515 | 7,9% | 79 | 363 | 123 |
| Financeiro | 118 | 1,8% | 61 | 188 | 48,5 |

**Achado-chave**: dentro de Suporte Técnico, a nota de satisfação cai de forma quase perfeitamente monotônica conforme aumenta o tempo de resposta durante o atendimento — nota 5 tem resposta média de 9,1 min, nota 1 tem 74,6 min (8x mais lento). O tempo de espera para começar o atendimento segue o mesmo padrão (nota 5: 127 min de espera; nota 1: 294 min). A insatisfação está ligada à demora em ser atendido/respondido, não ao tempo total ou à complexidade do caso — o argumento central para investir em autoatendimento instantâneo.

Taxa de resposta à pesquisa de satisfação: 34,6% (2.246 de 6.490).

## 3. Temas mais recorrentes (tags do Suri)

| Produto/Tema | Ocorrências |
|---|---|
| Holter | 1.540 |
| MAPA / MAPAs | 1.012 |
| CardioNet | 823 |
| Dúvida de utilização (genérica) | 525 |
| Cartão de memória (Holter) | 389 |
| Instalação (CardioNet) | 210 |
| CardioSmart | 209 |
| Representante | 202 |
| Pressão Central | 140 |
| Configurar analista (CardioNet) | 122 |
| Conexão CNet (CardioNet) | 102 |
| ECG | 92 |
| Cabo USB/RS232 (MAPA) | 88 |
| Bluetooth (MAPA) | 32 |
| Walk Free onboarding | 24 |
| Reset Senha | 16 |

Combinações mais frequentes: Holter + Cartão de memória (389), Holter + Dúvida de utilização (288), CardioNet + Instalação (208), CardioNet + Configurar analista (122), CardioNet + Conexão CNet (102), MAPA + Cabo USB/RS232 (88), MAPA + Dúvida de utilização (66), CardioNet + Dúvida de utilização (47), Pressão Central + Dúvida de utilização (45), MAPA + Bluetooth (32).

## 4. Modelo de referência: Central de Ajuda do Jusbrasil

Estrutura observada em suporte.jusbrasil.com.br: uma Central de Ajuda com busca em destaque, categorias claras de artigos organizadas por área, e o chat como camada adicional sobre essa base — o usuário é direcionado primeiro ao autoatendimento, com opção de continuar para atendimento humano/bot quando não resolve.

## 5. Reclame Aqui — reclamações públicas sobre a Cardios

Reputação geral: 9,0/10 ("Ótima"), 100% de resposta, 100% de resolução, 88,9% de retorno do cliente. Reclamações individuais recentes seguem o mesmo padrão dos dados do Suri: defeito de comunicação em MAPA de 24h, dificuldade de contato sobre o cartão do Holter, Arteris desconectando sem conseguir reconectar, e reclamações genéricas de "péssimo suporte técnico". Confirma que os temas técnicos mais sensíveis são conectividade (MAPA/Arteris) e Holter (cartão), e que a dor inclui não conseguir ser atendido rápido.

## 6. Inventário de material-fonte

- **Manuais vigentes** (pasta "Produtos/Manuais"): Arteris AOP, CardioLight, CardioLight+, CardioLoop, CardioMAPA, Cardioseven, Dyna-MAPA AOP, Dyna-MAPA NG, Dynamis.
- **Folhetos e anexos vigentes** (pasta "Cardios Home - Folhetos vigentes"): folhetos comerciais de toda a linha, quick-steps de cabo/pilha/cartão, e uma subpasta ANEXOS com fichas técnicas de 2026 (incluindo CardioNet CNC/CNS e CardioSmart 530/540/550).
- **Vídeos** (canal @cardiosmkt): série de treinamento técnico por produto (CardioMAPA + preparação do cartão, CardioLight, Dyna-MAPA Plus, CardioNet Client), além de conteúdo institucional e depoimentos científicos (fora do escopo da FAQ).
- **Números de contato oficiais encontrados nos manuais** (a confirmar se ainda são os vigentes): Geral (11) 3883-3000, Vendas (11) 3883-3030, SSC/Suporte ao Cliente (11) 3883-3010, Fax (11) 3883-3060.

## 7. Categorias propostas para a FAQ

1. Holter (CardioLight, CardioLight+, CardioLoop) — cartão de memória, instalação/uso
2. MAPA (CardioMAPA, Dyna-MAPA AOP/NG) — cabo USB/RS232, Bluetooth, dúvidas de uso
3. CardioNet (software) — instalação, configurar analista, conexão CNet, reset de senha
4. CardioSmart (software 530/540/550) — inclui diferenças entre versões
5. Pressão Central (Arteris AOP) — conectividade, instalação
6. ECG (Cardioseven, Dynamis)
7. Comercial (planos, representantes, orçamento)
8. Financeiro
9. Assistência Técnica (hardware — escalonamento)

Fora do volume de tickets atual, mas no escopo do projeto: Vireo ARK, MindBeat (produtos novos).
