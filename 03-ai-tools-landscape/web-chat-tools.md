# Web Chat AI Tools

The tools most people start with. All of them work in a browser, require no setup, and are useful immediately.

---

## Claude (claude.ai)

**Made by:** Anthropic
**Models:** Claude Haiku, Sonnet, Opus (various speed/cost tradeoffs)
**Free tier:** Yes — limited messages, slower model

**Strengths:**
- Very strong at following complex instructions
- Excellent at long documents — large context window
- Good at coding, analysis, and writing
- Claude 3.7 Sonnet introduced "extended thinking" — reasoning through hard problems step by step
- Claude Code (covered in section 04) uses the same models but in your terminal/IDE

**Limitations:**
- Web interface has no memory by default (Projects feature adds persistent context)
- A chat window can't read or write files on your machine — that's what section 04 sets up
- Claude Code is a separate tool (covered in section 04) and is included with a Claude Pro or Max subscription

**Best for:** Complex tasks, long documents, coding questions, tasks where you want thoughtful, careful responses.

**Claude Projects:** Claude.ai has a "Projects" feature that lets you upload documents and maintain context across conversations. This is the closest web-based equivalent to context engineering — you upload your CLAUDE.md and relevant docs, and the AI keeps them in context. Worth exploring before committing to a full IDE setup.

---

## ChatGPT (chat.openai.com)

**Made by:** OpenAI
**Models:** GPT-4o, GPT-4o mini, o1, o3
**Free tier:** Yes — limited to GPT-4o mini; GPT-4o with limits

**Strengths:**
- Very broad capability across tasks
- Strong at math and coding (especially o1/o3 "reasoning" models)
- Good image generation (DALL-E integration)
- Memory feature: can remember facts about you across conversations
- Plugin/tool ecosystem (can browse the web, run Python code in a sandbox)

**Limitations:**
- Memory can be inconsistent or surface unhelpful facts
- Response style can be verbose
- Web browsing is inconsistent

**Best for:** General tasks, math/reasoning problems (o1/o3 models), image generation alongside text.

---

## Gemini (gemini.google.com)

**Made by:** Google DeepMind
**Models:** Gemini Flash, Pro, Ultra
**Free tier:** Yes

**Strengths:**
- Very large context window (1M tokens on Pro/Ultra)
- Deep Google integration (can read your Gmail, Docs, Drive with permission)
- Excellent at summarizing large documents
- Gemini Advanced includes Google Workspace features

**Limitations:**
- Reasoning can be less precise than Claude or GPT-4o on complex tasks
- Google integration is useful but raises privacy considerations

**Best for:** Tasks involving Google Workspace, summarizing very long documents, users already embedded in the Google ecosystem.

---

## Comparison table

| Tool | Context window | Free tier | Best strength | Google integration |
|---|---|---|---|---|
| Claude | Up to 200K tokens | Yes (limited) | Complex instructions, long docs | No |
| ChatGPT | 128K tokens | Yes (limited) | Math/reasoning, broad tasks | No |
| Gemini | Up to 1M tokens | Yes | Long docs, Google Workspace | Yes |

---

## What they all can't do

- **Access your local files** — you'd have to paste the content in
- **Run code on your machine** — ChatGPT can run Python in a sandbox, but not on your system
- **Commit to Git** — no awareness of your project history
- **Remember your project** reliably — each session starts fresh (Projects/Memory features help, but aren't persistent context engineering)

This is why IDE-based AI tools exist. The next section covers them.
