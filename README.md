# Curriculo HTML

Projeto de curriculo responsivo desenvolvido com HTML e CSS, publicado pelo GitHub Pages.

## Arquivos principais

- `index.html`: pagina principal do curriculo e arquivo usado pelo GitHub Pages.
- `template.html`: modelo Jinja2 usado para gerar o `index.html`.
- `gerar_curriculo.py`: script Python com os dados do curriculo.
- `style.css`: estilos visuais e regras de responsividade.
- `requirements.txt`: dependencia Python usada pelo gerador.
- `.gitignore`: arquivos e pastas locais que nao devem ir para o Git.

## Como gerar

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python gerar_curriculo.py
```

O script atualiza o `index.html`, que e a pagina publicada no GitHub Pages.

## Como visualizar

Abra `index.html` no navegador ou acesse a pagina publicada pelo GitHub Pages.

## Git

O projeto ja inclui `.gitignore` para manter fora do repositorio arquivos locais como `.venv/`, arquivos de ambiente e configuracoes de editor.
