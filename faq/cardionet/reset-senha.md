---
id: cardionet-reset-senha
categoria: CardioNet
produtos: [Portal CardioNet]
titulo: "Esqueci/preciso trocar a senha do Portal CardioNet"
volume_suri: "16 casos em 3 meses — tema novo, bom candidato a resposta 100% automática"
fontes: ["Notas internas do projeto de integração DICOM/CardioNet"]
status: "⚠️ rascunho — confirmar fluxo exato de recuperação com Filipe"
---

## Resposta rápida (bot / primeira mensagem) — versão preliminar

As credenciais de acesso ao Portal CardioNet são as mesmas da conta do serviço de saúde do cliente. Este é um dos temas mais simples de resolver 100% pelo bot, sem precisar de atendente — vale ser um dos primeiros fluxos totalmente automatizados.

## ⚠️ Pontos que precisam de confirmação técnica antes de virar resposta final
- URL exata da tela de "esqueci minha senha" do Portal CardioNet.
- Se a recuperação é por e-mail cadastrado, ou se depende de contato com o suporte para reset manual.
- Se há um responsável/administrador por conta que pode resetar a senha de outros usuários da mesma clínica.

## Quando escalar para atendimento humano

- Cliente não tem mais acesso ao e-mail cadastrado.
- Conta bloqueada por tentativas — pode exigir reset manual pelo suporte.

## Fonte / observações

Assim que o fluxo de recuperação for confirmado com o Filipe, este artigo tem potencial de virar uma resposta 100% automática do bot (sem necessidade de atendente humano) — baixo volume mas alta automatização possível.
