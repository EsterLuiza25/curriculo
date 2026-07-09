# Curriculo HTML

Projeto de curriculo responsivo desenvolvido com HTML e CSS, com geração do arquivo final a partir de um template Jinja2 em Python.

## Arquivos principais

- `gerar_curriculo.py`: concentra os dados do curriculo e renderiza o HTML.
- `template.html`: modelo usado pelo Jinja2.
- `curriculo.html`: pagina final gerada para abrir no navegador ou publicar.
- `style.css`: estilos visuais e regras de responsividade.

## Como executar

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python gerar_curriculo.py
```

Depois, abra `curriculo.html` no navegador.

## Git

O projeto ja inclui `.gitignore` para manter fora do repositorio arquivos locais como `.venv/`, caches Python, arquivos de ambiente e configuracoes de editor.
