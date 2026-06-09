# AI Setup Prompt: Beyond the Chatbox

This is a guided orientation. You do not need to know how to code. You will get this guide in front of an AI assistant, paste one prompt, and get a personalized starting point instead of a generic "read from the beginning."

It takes about five minutes.

---

## Before you start: what you need

This repo is a learning guide, so this step is about reading and orientation, not editing files on your computer. That means you can paste the prompt below into almost any Claude window, including the free one in your browser at https://claude.ai . You do not need anything installed yet.

You will install heavier tools (Claude Desktop or Claude Code) later. That is exactly what this guide teaches, starting in section 00 and section 04. For now, any Claude works.

You get the best, most specific orientation if the assistant can actually read the repo files (Claude Code or Claude Desktop with this folder open). If you are in a browser chat, the prompt still works; the advice is just a little more general.

---

## Step 1: Get the guide

Pick whichever sounds easier.

**Option A, just read it on GitHub (nothing to install):**
Open the repo on GitHub and start reading. The whole guide is right there in your browser. If you only want orientation, you can paste the Step 3 prompt into a browser Claude window without downloading anything.

**Option B, download a ZIP (so your assistant can read it):**
1. On the repo page, click the green **Code** button near the top right.
2. Click **Download ZIP**.
3. Find the file in your Downloads folder and unzip it. You now have a `beyond-the-chatbox` folder. Move it somewhere you will remember.

**Option C, clone with git (if you have git):**
Run `git clone https://github.com/Mfrostbutter/beyond-the-chatbox.git` in your terminal.

Not sure? Option A is fine. You can always download it later.

---

## Step 2: Point your assistant at the guide (optional but better)

If you downloaded the folder in Step 1:

- **Claude Desktop:** make sure the folder is in your assistant's allowed file locations so it can read the guide.
- **Claude Code:** open a session inside the `beyond-the-chatbox` folder.

If you are using a browser chat, skip this. The prompt still works.

---

## Step 3: Paste this prompt to your assistant

Copy everything in the box and send it. The assistant will ask you a few short questions, then tell you exactly where to start.

```
I am getting started with the "beyond-the-chatbox" learning guide. It teaches
people how to stop just chatting with AI and start using it in their real work:
their files, their knowledge, and their workflows. If you can read my files,
read the README and the section folders first so your advice is specific. If you
cannot, that is fine, use what you know about the repo from this prompt.

Help me get oriented. Ask me these questions one at a time, wait for each answer,
and keep it friendly. Assume I am smart but new to this.

1. Where are you now? For example: "I use Claude in the browser daily and want to
   go deeper," "I work in IT and want more from AI tools," or "I have a little
   coding experience and want to use an AI coding tool properly."

2. What do you want to be able to do after working through this guide?

3. Have you set up the prerequisites yet (a Claude Pro account, and the tools in
   section 00)? It is fine if you have not.

Based on my answers, tell me:

1. Which section to start with, and why, based on what I told you. Do not just say
   "start at 01."
2. Any prerequisite I should do first if I have not.
3. The one thing that will make the biggest difference for what I am trying to do.
4. The section that will give me something practical and usable today.

Keep it short. I want to start, not read a roadmap.
```

---

## After orientation

Once the assistant has pointed you somewhere, ask it to walk you through that section. For most people that is context engineering:

```
Walk me through 05-context-engineering. Start with what-is-claude-md.md and help
me apply it to my own work.
```

Swap the section number for whatever the assistant recommended.

---

## If something goes wrong

- **"The assistant gives vague answers."** It probably cannot see the repo files. Either download the folder (Step 1, Option B) and open it in Claude Desktop or Claude Code, or just tell it which section you are curious about and ask it to explain that one.
- **"I do not have any AI tool set up."** You do not need one to read this guide. Open it on GitHub and start at `01-foundations/`. Section 00 and section 04 will get you set up with the bigger tools when you are ready.
- **"I am completely stuck."** Open an issue on the repo and describe what happened. Plain language is fine.
