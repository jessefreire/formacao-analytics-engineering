# MCP Servers

## powerbi-modeling-mcp

Servidor MCP para modelagem semântica do Power BI (formato PBIP/TMDL) via Analysis Services.

### Instalação

1. Instalar a extensão **Power BI Modeling MCP** no VS Code Insiders
2. Localizar o executável em:
   ```
   C:\Users\<seu-usuario>\.vscode-insiders\extensions\analysis-services.powerbi-modeling-mcp-<versao>-win32-x64\server\powerbi-modeling-mcp.exe
   ```
3. Configurar na sua IDE com IA:
   - **Claude Code**: usa `.mcp.json` na raiz do projeto (já incluído)
   - **OpenCode**: configurar em `~/.config/opencode/opencode.json` (ver `mcp-exemplo.json`)

### Operações Disponíveis (16)

| Operação | Descrição |
|----------|-----------|
| `table_operations` | Criar/editar tabelas |
| `column_operations` | Criar/editar colunas |
| `measure_operations` | Criar/editar medidas DAX |
| `relationship_operations` | Criar/editar relacionamentos |
| `calculation_group_operations` | Calculation groups |
| `calendar_operations` | Calendários |
| `culture_operations` | Culturas e traduções |
| `dax_query_operations` | Executar/validar consultas DAX |
| `partition_operations` | Partições e refresh |
| `security_role_operations` | Roles e RLS |
| `user_hierarchy_operations` | Hierarquias de usuário |
| `perspective_operations` | Perspectivas |
| `database_operations` | Import/export TMDL |
| `model_operations` | Stats, refresh, rename |
| `connection_operations` | Conectar ao modelo |
| `trace_operations` | Capturar eventos |
| `transaction_operations` | Transações Analysis Services |

### Arquivos

- `mcp-exemplo.json` — template de configuração (formato OpenCode; para Claude Code ver `.mcp.json` na raiz)
- `README.md` (este arquivo) — documentação

### Atenção

> O caminho do executável contém o número de versão da extensão. Se o MCP parar de conectar após atualização, confira o caminho atual com `ls ~/.vscode-insiders/extensions` e ajuste na config da sua IDE.
