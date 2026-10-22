# Free(ish) Claude Code Setup Guide — via AgentRouter + DeepSeek
> Tested on macOS (zsh). Routes Claude Code through AgentRouter's Anthropic-compatible endpoint to the `deepseek-v4-flash` model.

---

## How It Works

AgentRouter is a **third-party API gateway** — not an official Anthropic product. It exposes an Anthropic-compatible endpoint, so Claude Code can be pointed at it instead of `api.anthropic.com`, and it will route your requests to whichever model you specify (Claude, DeepSeek, GLM, etc.), billed against your AgentRouter account balance.

```
Claude Code (CLI) ──► AgentRouter (https://agentrouter.org) ──► deepseek-v4-flash
```

> ⚠️ **Heads up:** Because this routes through a third party, avoid using it on private repos, credentials, or sensitive client data — treat it the same way you'd treat any external relay.

---

## 1. Create an AgentRouter Account and Get an API Key

- Go to [agentrouter.org/login](https://agentrouter.org/login) and sign in (GitHub login supported).
- Once logged in, open **Console → API Token** in the left sidebar.
- Generate a new token and give it a clear name, e.g. `claude-code`.
- Copy the key — it starts with `sk-...`. Keep it private; don't commit it to git.

---

## 2. Install Node.js (needed for Claude Code)

Check if you already have it:

```bash
node -v
npm -v
```

If you get `command not found`, install Node via **nvm** (works even when Homebrew isn't available):

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
export NVM_DIR="$HOME/.nvm"
source "$NVM_DIR/nvm.sh"
nvm install --lts
```

Verify:
```bash
node -v
npm -v
```

> Tip: you can also install [uv](https://astral.sh/uv) (a Python package manager) at the same time if your workflow needs it — it's unrelated to Claude Code but commonly bundled into setup scripts:
> ```bash
> curl -LsSf https://astral.sh/uv/install.sh | sh
> source ~/.zshrc
> ```

---

## 3. Install Claude Code

```bash
npm install -g @anthropic-ai/claude-code
claude --version
```

You should see a version number like `2.1.252 (Claude Code)`.

---

## 4. Set Environment Variables

```bash
export ANTHROPIC_BASE_URL="https://agentrouter.org/"
export ANTHROPIC_AUTH_TOKEN="YOUR_AGENTROUTER_API_KEY"
export ANTHROPIC_MODEL="deepseek-v4-flash"
```

> ⚠️ **Important:** Do **not** also set `ANTHROPIC_API_KEY`. Having both `ANTHROPIC_AUTH_TOKEN` and `ANTHROPIC_API_KEY` set at the same time causes an auth conflict and can trigger errors like `Budget pool quota has been exhausted` even when your account has balance. Use `ANTHROPIC_AUTH_TOKEN` only.

If you had `ANTHROPIC_API_KEY` set previously, unset it:
```bash
unset ANTHROPIC_API_KEY
```

---

## 5. Launch and Test

```bash
claude
```

Inside Claude Code, test the connection with a safe, minimal prompt:
```
Reply with only OK
```

If it replies `OK`, the connection works. Then test a read-only tool action:
```
List the files in the current directory and tell me if a README exists. Do not modify anything.
```

---

## 6. Make the Settings Permanent

So you don't have to re-export every session, add the variables to your shell config:

```bash
echo 'export ANTHROPIC_BASE_URL="https://agentrouter.org/"' >> ~/.zshrc
echo 'export ANTHROPIC_AUTH_TOKEN="YOUR_AGENTROUTER_API_KEY"' >> ~/.zshrc
echo 'export ANTHROPIC_MODEL="deepseek-v4-flash"' >> ~/.zshrc
source ~/.zshrc
```

---

## Switching Models

AgentRouter's Anthropic-compatible endpoint supports other models too — just check **Console → API Token** on the AgentRouter site for the current list (e.g. `claude-opus-5`, `glm-5.3`). To switch:

```bash
export ANTHROPIC_MODEL="glm-5.3"
claude
```

`deepseek-v4-flash` is confirmed working with Claude Code's chat and basic tool calls as of this guide. Other models may vary in reliability, since Claude Code's tool-calling format was built around Claude models specifically.

---

## Troubleshooting

| Problem | Likely Cause | Fix |
|---|---|---|
| `command not found: npm` | Node.js not installed | Install Node via Homebrew or nvm (Step 2) |
| `Both ANTHROPIC_AUTH_TOKEN and ANTHROPIC_API_KEY set` warning | Both env vars set at once | `unset ANTHROPIC_API_KEY` |
| `402 Budget pool quota has been exhausted` | Per-token/model budget cap, dual-auth conflict, or account-level default group cap | Check token quota in AgentRouter console; ensure only `ANTHROPIC_AUTH_TOKEN` is set; try a different model; check "Account Binding"/"Other Settings" for a group/budget-pool selector |
| Model replies but fails on file/tool actions | Non-Claude models weren't trained on Claude Code's tool-calling format | Expected limitation — retry the action, or switch models |

---

## Quick Reference Card

```
GET API KEY
─────────────────────────────────────
https://agentrouter.org/login → Console → API Token

SET VARIABLES (per session, or once via ~/.zshrc)
─────────────────────────────────────
export ANTHROPIC_BASE_URL="https://agentrouter.org/"
export ANTHROPIC_AUTH_TOKEN="YOUR_AGENTROUTER_API_KEY"
export ANTHROPIC_MODEL="deepseek-v4-flash"
unset ANTHROPIC_API_KEY

LAUNCH
─────────────────────────────────────
claude

TEST
─────────────────────────────────────
Reply with only OK
```