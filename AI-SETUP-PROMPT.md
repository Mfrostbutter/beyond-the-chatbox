# AI Setup Prompt — Beyond the Chatbox

Paste this into Claude Code after cloning the repo. It orients you to the learning path and helps you figure out where to start.

---

## Prompt

```
I just cloned the "beyond-the-chatbox" learning repo and I'm opening it in Claude Code for the first time.

Please help me get oriented. Ask me these questions one at a time:

1. What's your current situation? (e.g., "I use Claude.ai daily but want to go deeper", 
   "I'm an IT professional trying to get more from AI tools", "I have some coding experience 
   and want to understand how to use Claude Code properly")

2. What's your goal? What do you want to be able to do after working through this repo?

3. Have you already completed the prerequisites in 00-prerequisites/? 
   (Claude Pro account, Git, VS Code, Docker Desktop)

Based on my answers, do the following:

1. Tell me which section to start with and why — don't just say "start at section 01", 
   give me a recommendation based on what I told you
2. Flag any prerequisites I should complete first if I haven't
3. Tell me the one thing that will make the biggest difference in how I use AI tools, 
   based on what I'm trying to do
4. Point me to the section that will give me the most practical, usable output today

Keep it short. I want to start working, not reading a roadmap.
```

---

## What this does

Claude Code reads this repo (including every README and section file) as context. When you paste this prompt, it can give you a personalized starting point instead of a generic "read from the beginning" answer.

The questions are designed to surface:
- Where you are now (so Claude doesn't explain things you already know)
- What you want to build or do (so the recommendation is actually useful)
- Whether you have the tools installed (so you don't get stuck on missing prerequisites)

---

## After orientation

Once Claude Code has oriented you, ask it to walk you through your first section. For most people that means:

```
Walk me through 05-context-engineering. Start with what-is-claude-md.md and 
help me understand how to apply this to my own work.
```

Replace the section number based on what Claude recommended.
