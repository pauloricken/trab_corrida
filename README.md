# Trabalho — Log de Corridas (Padrões de Projeto)

Desenvolvido por: Paulo vitor Ricken 

Este projeto implementa os padrões solicitados:
- **Strategy**: precificação dinâmica por cidade/horário (Option A: multiplicadores por cidade; pico = 18-23h).
- **Decorator**: taxas em camadas (serviço, pedágio, aeroporto).
- **Observer**: disparo de recibo e auditoria (impressão + registro).

Como executar:
1. Criar/ativar venv (recomendado).
2. `pip install pytest` (opcional, para testes).
3. Rodar demo: `python -m app.cli`
4. Rodar testes: `pytest -q`

Arquitetura mínima: domain/, strategies/, decorators/, observers/, factory/, infra/, app/, tests/.
